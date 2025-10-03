---
layout:     post

title:      "Throwback: Aspect-Oriented Programming"
date:       2022-12-02
author:     "Patrick Lam"
tags:       ["programming"]
categories: ["work"]
image:      "/img/20220917-nz-interregional-rail/PXL_20210530_002805808.webp"
showtoc:    false
summary:    "Aspect-Oriented Programming used to be trendy but never really got traction. Occasionally people talk about things where AOP would have helped."

---

<style>
.post-heading h1  { color: yellow; text-shadow: 2px 2px 2px grey; }
.meta { color: #fff; text-shadow: 1px 1px 1px grey; }
</style>

[Hillel Wayne](https://hillelwayne.com/) wrote about something that he calls [hyperprogramming](https://buttondown.email/hillelwayne/archive/i-am-disappointed-by-dynamic-typing/) or higher-order programming on his newsletter (worth subscribing to).

> But there’s another way of thinking about dynamic types: a dynamically typed language is one where types are runtime values and manipulable like all other values. It’s a short hop from there to thinking of the whole runtime environment in the same way, where everything is a runtime construct.

He then gives a number of applications. I would summarize these applications as being things developers might want to know about their program as it runs, enabling future changes to the code or validating past changes. For instance, checking that an optimized function produces the same result as an unoptimized function. Or providing better information about failed test executions.

To me, this feels very much like aspect-oriented programming, where one could provide advice modifying the execution of Java programs. One would typically state some program points where the advice would apply ("method foo()") and perhaps a predicate. If true, then the program would execute some provided code.

No one really talks about AOP these days. The aspectj compiler produced some quite slow code, and there were efforts like the [abc AspectBench compiler](https://dl.acm.org/doi/10.1145/1094855.1094877) to make it produce faster code. But I think the real problem was that, at the time, no one could really come up with applications besides debugging and tracing. I don't think you'd want to deploy aspect-oriented code which had functional effects into production! It's too hard to reason about!

Maybe the right thing would have been as a tool for program introspection and augmenting the usefulness of test suites. It's quite hard to evaluate such a tool, but that doesn't stop us usually. Certainly there was no killer app for AOP; and test suites, which come up in Hillel Wayne's examples, weren't thought about as much.

(I was recently on [Blad Glasbergen](https://scholar.google.ca/citations?user=pI5jLCEAAAAJ&hl=en)'s PhD committee; he invented a system for tuning database engines at runtime. That could also have benefited from aspect-oriented programming, I think, though really to change nonfunctional properties of the database engine.)
