---
layout:     post

title:      "My Photo Workflow, and Adventures in Hugo Development"
date:       2021-08-24
author:     "Patrick Lam"
tags:       ["tech", "meta"]
categories: ["development"]
image:      "/img/20210624-mount-french/20210524_012101801_more_mountains.PANO.webp"
summary:    "I finally got around to adding links to my Hugo gallery sliders. Here's how."
showtoc:    false

---

<style>
.post-heading h1  { color: #9011cf; }
.meta { color: #9011cf; }
</style>

# Setting

Let's start with a demo.
<figure>
{{< gallery-slider dir="/img/20210824-hugo-development/various-pics">}}
<figcaption style="text-align:center">South end of Matthes Crest (Yosemite), Picket Range (North Cascades),<br>me with a tufa (Kalymnos)</figcaption>
</figure>

I've been slowly evolving how I embed pictures in my blog, which is statically site generated with Hugo. I've settled on Thomas Biering's [hugo-slider-shortcode](https://github.com/tbiering/hugo-slider-shortcode) gallery slider 
with some modifications, particularly to allow multiple sliders in a page. It works well now: I dump pictures in a directory, I insert a bunch of markup which I cut-and-paste from a past entry, and I make sure that the aspect ratios
match (otherwise the text below jumps up and down; super annoying!). All I need to do to generate the above slider is to add this markup.

	<figure>
	{{</* gallery-slider dir="/img/20210824-hugo-development/various-pics" */>}}
	<figcaption style="text-align:center">South end of Matthes Crest (Yosemite), Picket Range (North Cascades),<br>me with a tufa (Kalymnos)</figcaption>
	</figure>

# My workflow 

My primary photo classification technology is
directories and filenames. I create one directory per day of photos
(e.g. ```2018/180808-mcmillan-spire```), and then use
[digikam](https://www.digikam.org/) to reject photos (rejection stored in EXIF
metadata) so that I have a manageable collection left. I rename the
keepers, preserving the camera's numbers (e.g. ```07658```) and
appending a description of the photo's contents
(e.g. ```07658_snow_to_cross```). Edited photos get ```_v1``` at the
end. 

Using default-accept rather than default-deny for photo selection
means that I end up with more pictures of lower quality, but I like to tell
myself that they tell a story, rather than being highlights. I try to not have
more than 30 pictures per gallery album, though sometimes I don't meet
that goal. Sliders are default-accept and usually no more than 8 pictures.

# The problem

But! 
The sliders aren't the authoritative version of the pictures. Some
(but not all) of the pictures exist in my
[Piwigo](https://piwigo.org/) [gallery](https://gallery.patricklam.ca), at higher resolution, and in
the context of other (less-selected) pictures. I've thought that it
would be useful to link the pictures to the gallery. I don't actually
have the storage space to put full resolution pictures in my gallery,
but I do put pictures at 3000 pixels wide, which is much better than
what we have on these pages.

Using filenames I can easily track where a file ends up in my gallery,
even if I post the photo first and then put it in the gallery second. But
it's too hard to automatically build the blog post&nbsp;&rarr;&nbsp;gallery links.
Thinking ahead, I had created lookup files for some posts, indicating the link
between the filename and the URL. They look like this:

    07658_snow_to_cross.webp ?/7230/category/1171
    20171123_144537249_plam_with_tufa.webp ?/6526/category/1147
    00432_south_end_of_matthes_crest.webp ?/5434/category/1110

## Goal
Modify the gallery-slider to automatically insert hyperlinks based on the lookup files.

# Approach

Conceptually: It's not hard! Read in the lookup file as a map (exists as a type in [Golang](https://golang.org/) which underlies Hugo), then do a map lookup when writing out the ```<img>``` link for an image (key is the image filename), 
and wrap an ```<a></a>``` tag pair with the looked-up value around the ```<img>```.

## Data source

A Google search directed me to [Data Templates](https://gohugo.io/templates/data-templates/) in the Hugo documentation. Looks like ```getCSV``` should work. (There's also ```transform.Unmarshal``` which is supposed to work, but I don't understand
how to direct input to it, because I don't understand either Hugo Pipes or Page Bundles.)  ```getCSV``` supports remote data sources which I don't want, but I don't know how to disable that.

*Main complaint:* There's no reference documentation (e.g. manpage) for ```getCSV```. All you have is the Data Templates example and the implementation's source code. 

There is reference documentation for ```transform.Unmarshal```, but it takes a ```Resource```, and there is no reference documentation for that, only links to the documentation-by-example for [Hugo Pipes](https://gohugo.io/hugo-pipes/) and [Page Bundles](https://gohugo.io/content-management/page-bundles/). OK, I guess Page Bundles are reference-documented, but I put my resources in the ```static``` directory. Maybe I shouldn't. But that's not that clear!

Of course it's ```func GetCSV``` in the source code, but hey, I don't really speak Go and I don't understand the naming conventions. The signature of ```GetCSV``` is

    func (ns *Namespace) GetCSV(sep string, args ...interface{}) (d [][]string, err error) {

which seem to lack the following details:

    url, headers := toURLAndHeaders(args)

And, sure, ```getCSV``` returns a 2D array. Trying to figure out whether there is a library function that converts arrays to
maps is challenging. So I just implemented it. Sure, I guess. Hugo templates don't quite support maps but you can use a scratch
object like this.

    {{ $links := newScratch }}
    {{ $links.Add "img" dict }}
    {{ range $i, $r := getCSV "," $csvPath }}
      {{ $links.SetInMap "img" (index $r 0) (index $r 1) }}
    {{ end }}

I also had a bit of problem-between-chair-and-keyboard where the map didn't seem to be working, but actually the filename
in the lookup file did not match the filename in the directory, because I'd migrated from jpeg to webp in my image directories.

[Edited to add:] I also added functionality to omit links where no gallery image exists. Finding "isset" is not obvious: there's no reference information for the type "dictionary". This [random page](https://bwaycer.github.io/hugo_tutorial.hugo/templates/functions/) points me in the right direction, but the main Hugo documentation doesn't? Grr.

### Filename

Required some futzing, but nothing notable. Hardcoded it first and then worked out how to get the right filename there. There was good reference documentation on the ```path``` object, e.g. [```path.Base```](https://gohugo.io/functions/path.base/). Here's part of the filename code.

    {{ $csvPath := (print "/static" ($.Get "dir") ".csv") }}

While I was doing that I realized that I didn't need to require an explicitly-specified ```id``` tag in my shortcode;
I could use ```($.Get "dir")``` as the id to disambiguate multiple sliders so that they don't all have to be in synch
(impossible when sliders have different numbers of photos!)

## Inserting the tag

Easy as (NZ slang). I just added the ```<a>``` tag with the needed lookups: first the common prefix (i.e. ```https://gallery.patricklam.ca/```), then the image-specific suffix. All conditional on existence of the lookup file.

    <div class="item active">{{ if $galleryLinks }}<a href="{{$.Scratch.Get "gallery"}}{{ index ($links.Get "img") .Name }}">{{ end }}<img class="slide-{{ $.Scratch.Get "id" }}" src="{{ $absoluteUrl }}">{{ if $galleryLinks }}</a>{{ end }}</div>

# Conclusion and next steps

Overall, not too hard; most of an evening's work to make this change, which I'd been putting off for a while. I'd guessed pretty much the right format for making this linkage doable. Hugo documentation was somewhat annoying, but the system is not so hard to pick up for someone familiar with programming but mostly unfamiliar with Hugo and Go.

The next thing that bugs me about my site is how it takes 10 seconds to build, which has been slowly creeping up. I could either set it up as a GitHub action so that it doesn't matter, or I could try to figure out what's making my site slow to build.
