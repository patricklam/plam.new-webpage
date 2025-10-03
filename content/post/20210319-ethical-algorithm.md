---
layout:     post

title:      "Book review: The Ethical Algorithm by Kearns and Roth"
date:       2021-03-19
author:     "Patrick Lam"
tags:       []
categories: ["work"]
image:      "/img/20210115-overwork/20180409_094833_mtl_skyline.webp"
showtoc:    false

---

[Again](/post/20210115-overwork/) wandering through a [Wellington City Library](https://www.wcl.govt.nz) branch, this time I picked up *[The Ethical Algorithm](https://global.oup.com/academic/product/the-ethical-algorithm-9780190948207)*
by Michael Kearns and Aaron Roth, from January 2020. It was an easy read for someone with a PhD in Computer Science
and a BSc in Math/CS, and
I finished it in about two hours. I didn't pick up that much that was new to me, but
I follow developments in this domain as an interested but technically-educated reader.

I also think all Waterloo Bachelor of Software Engineering grads ought
to be conversant with the ideas in this book, which I'll summarize (extremely briefly)
below.  Our grads have a solid undergraduate algorithms education,
some statistics, and no mandatory machine learning/AI.  So they should
be able to read this book but they wouldn't have been exposed to the
ideas in our curriculum, which is problematic, given how much of our world
is being shaped by AI.

Some of the sources of the cover blurbs are questionable. (I'm not
going to elaborate on that point.)

# Technical complaint: induced demand

There is an extended discussion of game theory using road navigation
as an example. Yes, of course travel time depends on others'
navigational choices. But the authors explicitly state that they
consider the total amount of traffic to be constant. This is a
terrible assumption, because it ignores induced demand. That is, the more lanes
you build, the more low-value traffic you'll attract. There's nothing
wrong with the computer science here, but it's not properly modelling
the real world.

# Technical praise

On the other hand, the authors did a good job of giving analogies to
describe Generative Adversarial Networks (which intuitively make sense
to me now).  The concept is a simple extension of fairly standard
concepts; I just hadn't bothered learning what GANs actually are. And
of course I still haven't internalized the technical definition. But I
probably won't need it anytime soon. GANs are really popping up
everywhere.

I also appreciated the description (Chapter 4) of using differential
privacy to prevent p-hacking. The bit just before that, about short
descriptions and p-hacking, needed a couple of reads for me to make
sense of.

I've had a problem with the modern usage of "algorithm", and the
authors point out that in modern usage we're usually talking about AI
meta-algorithms where we learn parameters and then run the
models (which reduces to "algorithm" as we usually understand it).

# Summary

Again, if you read like I do, then you've likely encountered these
concepts. Here's a summary of what we have in this book.

* privacy and differential privacy: how we can publish summary statistics
without eroding individuals' privacy;
* fairness (quite relevant for undergrad admissions, which is an issue for SE!);
* game theory;
* perils of multiple comparisons; and
* open problems eg interpretability of models.

I hadn't seen the discussion of superintelligence vs diminishing returns previously,
but the argument against the Singularity is plausible.

They discuss the unintended problems with optimization (e.g. you
didn't specify what to optimize against properly), which is also
illustrated by [Universal
Paperclips](https://www.decisionproblem.com/paperclips/).

I've had a discussion this week with a colleague about fact-checking vs the modern Internet
and the various dysfunctions (e.g. QAnon). This book points out that human oversight doesn't
scale. (They also don't discuss how human moderation is problematic for those who are hired
to moderate, but that's mainly off topic here.)

# Conclusion

Really, this is a good defense of theoretical computer science, in particular of the value of
mathematical formalism and algorithms, and a call to apply these in ethical ways.