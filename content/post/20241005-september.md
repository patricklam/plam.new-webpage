---
layout:     post

title:      "September: final versions of papers, course prep, Auckland, and Japan"
date:       2024-10-05
author:     "Patrick Lam"
tags:       ["retrospective"]
categories: ["work", "travel"]
published:  true
image:      "/img/20241005-september/06681_bridge.avif"
showtoc:    true
summary:    "Mostly in Wellington except for a weekend in Auckland and a week in Tokyo (the start of a busy travel month). Finalizing papers, reviewing course notes."

---

<style>
.post-heading h1  { color: white; text-shadow: 2px 2px 2px grey; }
.meta { color: white; }
</style>

Most recently I came back from a week-long trip to Japan to do the practical session of the IJF Academy Undergraduate
Certificate as Judo Instructor. Apart from that, I was pretty consistently in Wellington all September. Well, except
for a weekend in Auckland for the North Island judo championships.

I also attempted to go on two mountain trips to different parts of
Ruapehu, but there was too much wind, and the trips got canned.

Professionally, there was work on some final versions of papers, as well as reviewing course notes for ECE 459 which
I'll be teaching in Winter. As I started to write this, I was
all done and I was on my way to SCAM in Arizona to
[present](/papers/24.scam.vulnerable-dependency-analysis.slides.pdf)
our paper; as I had predicted, Mohammad didn't manage to get a US visa
unfortunately.

<ul>
  <li>Alex Le Blanc and Patrick Lam. To appear at HATRA 2024: <a href="/papers/24.hatra.rust-verification.pdf">Surveying the Rust Verification Landscape</a>. [<a href="https://arxiv.org/abs/2410.01981">arXiv</a>, <a href="/papers/24.hatra.rust-verification.bib">bib</a>]</li>
  <li>Mohammad Mahdi Abdollahpour, Jens Dietrich, and Patrick Lam. To appear in SCAM 2024: <a href="/papers/24.scam.vulnerable-dependency-analysis.pdf">Enhancing Security through Modularization: A Counterfactual Analysis of Vulnerability Propagation and Detection Precision</a>. [<a href="/papers/24.scam.vulnerable-dependency-analysis.bib">bib</a>, <a href="/papers/24.scam.vulnerable-dependency-analysis.slides.pdf">slides pdf</a>, <a href="https://docs.google.com/presentation/d/1CPr9W8wmiuxcG6HqfCCltI_2d_BJ-31oDyI-o02B9YQ/edit?usp=sharing">google slides</a>]</li>
  <li>Karoliine Holter, Juhan-Oskar Hennoste, Patrick Lam, Simmo Saan, Vesal Vojdani. To appear in Onward! 2024: <a href="/papers/24.onward.abs-debug.pdf">Abstract Debuggers: Exploring Program Behaviors Using Static Analysis Results</a>. [<a href="/papers/24.onward.abs-debug.bib">bib</a>]</li>
  <li>Karoliine Holter, Juhan-Oskar Hennoste, Simmo Saan, Patrick Lam, Vesal Vojdani. DEBT 2024: <a href="/papers/24.debt.abs-debug-demo.pdf">Abstract Debugging with GobPie (Demo)</a>. [<a href="/papers/24.debt.abs-debug-demo.slides.pdf">slides</a>, <a href="https://youtu.be/KtLFdxMAdD8">video</a>, <a href="/papers/24.debt.abs-debug-demo.bib">bib</a>]</li>
</ul>

<figure>
{{< gallery-slider dir="/img/20241005-september/2409-highlights" >}}
<figcaption style="text-align:center">Two little lambs on the Skyline walk in Wellington; veterans -66 podium at North Island Championships; birthday dessert; Edo Castle keep base; Western little egret; Chinese bushbrown; me and Khaled at the IJF Academy at the Kodokan; falls at Korakuen Gardens; "you don't need to wear shoes".</figcaption>
</figure>

# COVID

I left Japan just before the new self-amplifying vaccine became generally available, alas.

One of the things that has been shockingly bad is the recognition of SARS-CoV-19 as being
transmitted by aerosols, and hence the need for air cleaning and N95s.
* [a discussion of inexcusable UK failures](https://www.pslhub.org/learn/coronavirus-covid19/questions-around-government-governance-on/covid-19-a-risk-assessment-too-far-a-blog-by-david-osborn-r12061/)

There is a phase 4 trial of a mucosal vaccine in China which reported maybe-good results as well as a phase 1
with also maybe-good results. A US phase 1 started recruiting in July. Also some oral vector vaccines and other
vaccines still in development.
* [Absolutely Maybe on vaccines, end of September 2024](https://absolutelymaybe.plos.org/2024/09/30/more-trial-results-and-more-pancoronavirus-vaccines-nextgen-covid-vax-update-21/)

# Professional

This month I worked on revisions to the [HATRA](/papers/24.hatra.rust-verification.pdf) paper and updates to the [ECE 459 course
notes](https://www.github.com/jzarnett/ece459). With respect to HATRA, I feel like I now understand what unsafe actually means in Rust. Many people don't; I didn't before I studied it. (See Section 2 of the linked paper, but basically: you get access to 5 unsafe operations, but you also have to maintain safety properties that the compiler can't; or you can pass the buck to your callers or implementers). With respect to ECE 459, that was a lot of reading: we have around 7 pages of notes per lecture and 36 lectures. You do the math. Also passed on my thoughts about Karoliine's talk for DEBT.

Worked on 13 days this month. The IJF Academy trip took a big chunk out of the second half of the month and
I didn't do much work on that trip&mdash;I just read Mohammad's thesis. The calendar shows 20 work days, but also
being the start of the school year would typically be quite busy.

## Grad students/mentees/collaborators

Back to more normal collaboration pace with chats on 6 days, mostly my students. Also talked to 2 potential
graduate students.

## Collegiality/Service

Aspirationally, I hoped to work on the new TOSEM review in Japan. I didn't.

# Trips

North Island Championships in Auckland and IJF Academy in Tokyo. Two canned mountain trips.

## Auckland, September 13&ndash;15

Biked to WLG. Met up with Brad at Wellington Airport, who also trains at the Wellington Judo Academy, flew on the same
flight to Auckland, grabbed banh mi for lunch plus tea at a Fancy Place, and then headed to my airbnb in Avondale; somehow
Google recommended a bus rather than a train, even though Avondale has a train. I also had another banh mi
in Avondale for dinner, as well as an egg burger from Monster Kebab.

This time I fought in both veterans and seniors. I figured that since John had gone through so much trouble
to advocate for veterans -66kg categories, I should participate. I won both my fights in veterans, refereed
until seniors, and then lost my first fight and won my second fight after my opponent injured his elbow losing
to the guy I had beaten in veterans. I also refereed the kids on Sunday as usual.

<figure>
{{< gallery-slider dir="/img/20241005-september/north-islands" >}}
<figcaption style="text-align:center">Avondale; basketball at sunset; heavyweights; Wellington Judo Academy team; seafood at Yacht Chinese.</figcaption>
</figure>


The flight back was pretty routine. It was an 8pm flight which was
delayed till 830, which allowed me to switch to the 7:40 flight,
getting in just a bit earlier but trading seat 4A for 28B. The NZ PM (boo!) was
in the Air New Zealand lounge, as well as a cheerleading team, which
mobbed him for photos at some point. (I wonder how the whole team gets
in the lounge, but probably that says something about the demographics of
cheerleaders).

## Tokyo, September 21&ndash;30

Mid-length trip to Tokyo, to take the practical session of the IJF
Academy Undergraduate Certificate as Judo Instructor, which I hope
will help with getting referee grades. They seem to have one offering
every year at the Kokodan, the birthplace of judo. There will never a
better time for me than when on sabbatical. The trip was not too long, nor
too short. I flew in on the Saturday and out on the Sunday; they
wanted participants on the course to be available from Sunday through
Sunday, though activities only occurred Monday through Saturday, and
indeed some people left on Saturday evening and it was fine.

<figure>
{{< gallery-slider dir="/img/20241005-september/ijf-academy" >}}
<figcaption style="text-align:center">Snowcraft instructor Andy; MP and Ngauruhoe; lanterns at Rotorua Redwood walk; Rotorua from Forest Loop Track; Green Lake and its island; end of the mountain biking portion of Forest Loop; Tunnel Point; Pipikaretu Beach; hoiho (yellow-eyed penguin); petrified wood at Curio Bay; full moon at Wellington Judo Academy.</figcaption>
</figure>

I feel like I shouldn't really leave my bike at the airport for 9
days, so I took the bus. As with many flights connecting through
Auckland, I got the 6AM flight from Wellington, but as long as it's a
domestic flight (and AKL is), you can indeed still take the bus, as
long as you can online checkin. Otherwise you might be having to take
the taxi at 3:55AM to check in by 4:30 for an international flight,
which is highly painful.

AKL-NRT is usefully timed for sleeping. Though I was in a SkyCouch
row, there was also someone else in the row, so it was a normal seat
for this flight. That flight also had 100 Japanese students on a
school trip.  After getting off at NRT I took the Skyliner and subway
to the Kodokan.  I was surprised to find out that both the Skyliner
and the Narita Express exist and that they've been operating for
decades. Someone had an issue finding the Narita Express a few years
ago...

Sunset is early at this time of year, around 6:30, so nothing to see
the first night.  Had some convenience-store food to tide me over.

I had two free days in Tokyo this time. Which is more than I had on my
[previous trip to Japan]((/post/20230226-japan-part-i)). I guess we
often leave the big city ASAP.

### Day 1 in Tokyo: Imperial Palace, September 22

There was a heat wave just before my arrival and it was still pretty
hot on the Sunday, about 30 degrees as I recall. The primary goal was
to get a new white judogi at the Mizuno store, and I managed to do
that. Not really cheap, even without tax, like ¥41,000. But I didn't
have to wear my ratty gi all week, which was nice. Also I got to the
Imperial Palace Grounds (lots of stone fortifications), which were
free for the day (because Autumn Equinox holiday?) and Ueno Park. Saw
few birds at the Imperial Palace Grounds and a couple more at
Ueno. On my walk I observed some sort of far-right demonstration at a subway
station.

<figure>
{{< gallery-slider dir="/img/20241005-september/tokyo" >}}
<figcaption style="text-align:center">Eastern spot-billed duck; danger! do not lean; Half Moon Bridge; bamboo; urban train; Healing Baden at Spa LaQua; rollercoaster at Tokyo Dome.</figcaption>
</figure>

I also ate both at chain and non-chain places. There was a huge nan at
RB's, which also featured kofta-like meat. Back at the Kodokan, I
added myself to a dinner group and we had meats expertly grilled by
Tanor from Portland at Nikumori Horuman.

### Days 2 through 6: IJF Academy Practical Session, September 23&ndash;28

I've kvetched about the online part of the IJF Academy Undergraduate
Certificate as Judo Instructor before.  The Practical Session is
actually quite good and mostly independent from the content of the
online part.  There were 49 of us from 15 countries (the largest
course so far), including me from Canada, 10 from the US, a bunch from
Europe, and many from Asia, including Chinese Taipei and Hong
Kong. The highly-qualified instructor team was led by Mark Huizinga
and included at least 3 Olympic champions. (Huizinga had given the
Judo Quebec winter clinic in 2009; I asked him about it and he
remembered the year because it was just after his retirement from
competition).

<figure>
{{< gallery-slider dir="/img/20241005-september/ijf-academy" >}}
<figcaption style="text-align:center">"Judo spirits" sign at Kodokan hostel; pictures from Kodokan; Khaled; me and Khaled; me (the Canadian delegation) with the instructors.</figcaption>
</figure>

In some sense, there's nothing new: any black belt should have seen
the material in the course (though maybe Canadian competitive-stream
black belts might be a bit deficient in this knowledge).  But it moves
quickly over the 100 Kodokan judo techniques and we got about 5-10
minutes with each of them.  We also did the nage no kata (forms of
throwing), again seeing fundamentals, rather than as for kata
competition.  If you didn't know them ahead of time you would not be
able to follow. Such was the amount of material that we had 2× 3-hour
sessions each day Monday through Friday, with evaluations beginning
Friday afternoon. People who had done the course before said to
practice first, and it does help. More practice would have been
better, especially left side and in two directions.  The instructors
had impeccable form and clarified a lot of details in terms of the
traditional (not necessarily competitive) variants of the techniques.

You don't have to come to the course with a partner. Some people do
(e.g. Rod and Tanor from Obukan in Portland), and that would help a
bit. I worked with Khaled from the UK (near Wimbledon), who was the
correct height and weight, a fundamental knowledge of judo, and had
strong spirit to work, battling some chronic injuries (mostly not
caused by judo!). We got through the evaluation all right. (The
instructors worked to accommodate people with injuries, which is not
at all uncommon after years of judo.) The course is a bit physically
tough, with 900 breakfalls, but not as hard as a training camp.

The fee for the practical session was really quite modest, USD 360 for
a shared room, USD 420 for a private room with shared bath, and a bit
more for a private bath. This came with lunches catered by Habibi, the
restaurant in the basement of the Kodokan, which were all right.
Of course, getting to Japan isn't necessarily cheap, depending on where
you start from; New Zealand is far from everything, as I often say.

## Other activities in Tokyo (judo and eating)

There is randori (sparring) every night at Kodokan except Sunday. I
had already been working to avoid injury at the club in Wellington
even the week before the course (though I did fight at the North
Island Championships the weekend before), and I definitely wasn't
going to do randori before the end of the course.

So, I did participate on Saturday night, which has older (but skilled)
locals and an international crowd. I chatted with two French visitors,
including one -60 guy. I was also working out with an older guy. "So,
how long have you been doing judo?" "38 years." "Ah, I've been doing
judo for 40." He was 4th dan.

For breakfast I had a variety of foods, including from convenience stores,
bakeries, and McDonald's (somehow they don't have the ordering machines
but they do support the app).

I tried to get out for a walk for supper most days. There are a lot of
options nearby and I got through most of my checklist: sushi, udon,
curry, etc.  Did not manage to get ramen: I missed and got to the udon
place next door instead. Did get banh mi, which was a bit on the
expensive side for food in Tokyo and not outstanding.

Hieuy, from Texas, and I went to the Spa LaQua right next door to the Kodokan.
(Also next door: rollercoasters and ferris wheels). Cheaper and probably fancier
than the Polynesian Spa in Rotorua. Lots of hot and cold water. No clothes.
After-spa, in the Healing Baden part, there are clothes.

## Day 7: Koishikawa Korakuen Garden, Tsukiji Outer Market, bouldering

I had one more day in Tokyo after the course, before flying out on
Sunday evening.  There are a number of green spaces near the Kodokan,
including the Imperial Palace Gardens and Ueno Park, discussed
previously. Another space is the Koishikawa Korakuen Garden, with a
nominal entrance fee, some ponds, not that many birds, and lots of
photographers for some reason. I only had my super-compact
point-and-shoot (Sony HX95), but maybe I didn't miss that much anyway.

After the gardens, I went to the famous former fish market at
Tsukiji. The fish have moved elsewhere but there is still a
substantial collection of food outlets. I got an excellent sushi combo
for ¥2900. I noticed that the sushi chefs were all wearing ties under
their white coats.  The crowd kept them busy.

My last activity in Tokyo was the bouldering gym, B-Pump Tokyo
Akihabara.  It extends over 4 levels with an outside part (closed due
to the misty rain that day, with occasional downpours).  The top floor
also had some long traverses.  Some gyms have a discount for
first-time visits when accompanied by a member.  The B-Pump gyms
instead have an extra fee for first-time visits. This gym was also quite
crowded on a Sunday afternoon, with a fair number of gaijin, in
addition to locals. But the routesetting was good.

## Travel planning

I have a couple of trips coming up. There was some last-minute planning for the October trips:
* Arizona: annoyingly quick out-and-back to Flagstaff via LA for SCAM
* Toronto/Pasadena/Winnipeg: longer trip for two tournaments and a conference.

Basically I've been travelling with only brief respites from
September 21 and through to October 29, though with 5 days at home in Wellington
after Tokyo and 5 days in New Zealand between Arizona and Toronto (with 3 of them in Rotorua
for NZ judo nationals).

In December we also thought we'd check out French Polynesia. The Islands are pretty hard to get
to from other places and relatively closer to New Zealand. We'll have been to the Cook Islands,
New Caledonia, and French Polynesia. I was going back and forth about whether to go to the Marquesas
Islands (new UNESCO World Heritage site, less rainy) but finally couldn't justify the $2k in additional
airfare. We also have our third try at the Cascade Saddle planned for December. Hope that works.

# Movement statistics

Not much movement except for two plane trips. Mostly stayed put in Tokyo when I was there and in Wellington when I was there: I did try to walk to dinner when it wasn't raining, but that was only a few km each day.
* 🚶 Walking: 76km on 23 days (second-lowest of the year; only one walk and mostly stayed put in Tokyo)
* 🚲 Biking: 119km on 13 days, 31km ebike
* 🚗 Driving: 22km on 1 day (from Avondale to AKL)
* 🚗 Taxi: 19km (Skyline)
* 🚌 Bus: 32km on 3 days (in Auckland, and to and back from WLG)
* ✈ Plane: 19594km (WLG-AKL, AKL-WLG, WLG-AKL-NRT, NRT-AKL-WLG)

## Walks

Just one named walk this month, plus some walking around Tokyo.
* [Skyline Track](https://wellington.govt.nz/recreation/enjoy-the-outdoors/walks-and-walkways/beyond-the-city/skyline-walkway), Wellington (a repeat; they all are, these days, but this one is just nice.)

<figure>
{{< gallery-slider dir="/img/20241005-september/skyline" >}}
<figcaption style="text-align:center">Green hills; big and little sheep; mushroom; cow; Mount Kaukau viewing platform; Wellington CBD view.</figcaption>
</figure>


# Pictures

* [September photos report](/post/20241002-september-photos)

I always say that counting is hard. Anyway, by the way I count it, I processed about the same number of photos in September as in August, but not really, because I rejected some of the photos in previous months. Anyway, I got rid of a doozy of a set: the day on the boat with [Petrel Station](https://www.thepetrelstation.nz/) resulted in 982 photos, consuming 11GB. I kept 72 of those 982 photos. (Technically, I keep them all, but mark rejected photos).

I removed 8 sets from the queue and added 7 sets, so definitely ahead, especially since the added sets should be easy.

[Picture
logs](https://www.github.com/patricklam/picture-processing-logs) still
available. As always, pictures are clickable to go to the full gallery. 

* Sets of pictures posted: 8 (July: 12)
* Total pictures posted: 346 (523)
* Total pictures in selection pool: 2037 (2064)
* Accept rate: 17% (min 8%, max 52%) (July: 25%)
* Pictures posted on this page: 53

<figure>
{{< gallery-slider dir="/img/20241002-september-photos/highlights" >}}
<figcaption style="text-align:center">Gonzen in the actual Alps; saddleback with dappled sun at Zealandia; 2022 NZ nationals; surfer off the Taranaki coast; minature pony at Opunake; white-capped mollymawk head off Tutukaka; Māori carving (on Lake Taupō) detail; Rotorua mountain bike park.</figcaption>
</figure>

# September posts

I really need to post the remaining 2 days of the Overland Track. Three posts this month, one of which was a submission to a NZ Parliament committee, again about yet another misguided Government proposal.

* [Review: Sunshine Nails by Mai Nguyen](/post/20240919-review-sunshine-nails)
* [Comparison: Old Ghost Road vs Paparoa Tracks](/post/20240920-old-ghost-road-versus-paparoa-tracks)
* [Submission on oil and gas exploration in NZ](/post/20240926-oil-and-gas-exploration)

# Miscellaneous

Really stuck to routine until the travelling started (which will continue through the end of October).

## Courses

See above for discussion of IJF Academy course.

Still doing the te reo Māori course. I suspect it's less effective than Duolingo.

## Acquisitions

* Got fixed Sony A6600 back with non-broken viewfinder (a casualty of carrying around an ice axe and a camera at the same time, on the Snowcraft courses)
* Sony RX100M4 "beyond economical repair" due to water; to be replaced by an M7 for a modest fee (NZ$1000)
* Edelrid T-shirt (I put all climbing-suitable T-shirts in a locker; I worry about climbing trashing wool shirts).
* Mizuno judogi (my white gi is kind of ratty; the Mizuno store provides size checking with the soukuteki measuring device, as well as taxfree shopping, but still not cheap.)

## Sports

Only 7× of regular judo practice, one tournament, plus one practice at the Kodokan (Saturday night,
not the most hardcore bunch), and 6 days of judo (sometimes 6h per day) at the IJF Academy.
Climbing 8× as well, including once in Tokyo at B-Pump Akihabara.

## Food

Not so much, and then Tokyo, with infinite cheap food.

### Auckland

* Vietnamese Street Food: small restaurant in central Auckland
* Up Café: hotel cafe, nice spot for a tea
* Banh Mi Delight: food truck in Avondale
* Monster Kebab: open till real late
* Top Well: bakery in Avondale
* Yacht Chinese: almost all Asians eating there

Two banh mis and Chinese food as well as a kebab, fancy tea, and a pie.

<figure>
{{< gallery-slider dir="/img/20241005-september/food-akl" >}}
<figcaption style="text-align:center">Banh mi from Vietnamese Street Food and rom Banh Mi Delight; egg burger from Monster Kebab; pie from Top Well; greens and beef at Yacht Chinese.</figcaption>
</figure>

### Wellington

* Brewtown Market in Upper Hutt: really delicious banh mi from a food truck (better than Auckland).


### Tokyo

* Caffe Veloce (tuna sandwich): not as tasty as I'd hoped.
* RB's (indian, huge nan): great nan, plus a kofta-like thing along with my curry.
* Nikuman Horumon (grilled meats): delicious (U grill)
* Omi Sushi: also delicious
* Taurin: I was actually hoping for ramen but missed, but good udon
* Banh mi: not the best food to get in Japan
* Gusto-Korakuen Kasuga cho (creamy cod carbonara): robot servers (but not for me), nice
* My Curry Shokudo Kasuga: cheese! and curry!
* Fresh Fish Market at Tokyo Dome: cheap and tasty sushi (probably cheaper than Vancouver)
* Torikozu: I made it to the post-course celebration after randori; various grilled food (they grill)
* Sushizanmai at Tsujuki Outer Market: more cheap and tasty sushi

<figure>
{{< gallery-slider dir="/img/20241005-september/food-tokyo" >}}
<figcaption style="text-align:center">Tuna sandwich from Caffe Veloce; qofte from RB's; the grill; chirashi from Omi Sushi; breakfast from the convenience store; udon from Taurin; banh mi; McDonald's; creamy cod carbonara; curry with tonkatsu and cheese; sushi box from Fresh Fish Market; some grilled food; sushi set from Sushizanmai.</figcaption>
</figure>


## Volunteering

Contributed a "practices" document for the Wellington Judo Academy based on sources of friction within judo clubs that I've observed in the past. It's a guardrail, but it's impossible to prevent malicious people. Other than that, just routine.

# Conclusion

Things got a bit out of control at the end, but September was pretty chill until the travel started. Gotta keep up with stuff for another week and a half and then back to New Zealand for the rest of my sabbatical.