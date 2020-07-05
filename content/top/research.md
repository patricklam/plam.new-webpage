---
layout:     post

title:      "Research"
author:     "Patrick Lam"
published:  true
---

# Research

My <a href="/top/publications/">publications</a> contain
more technical descriptions of my research. 

<p> My research aims to develop tools and techniques to help
 developers produce more reliable software systems. In particular,
 I am developing (1) lightweight specification languages, which enable
 developers to state key properties of their software, and (2) static
 analysis techniques, which enable compilers to verify that these properties
 actually hold.</p>

<p> <strong>Technology.</strong> Static analysis determines properties
of a program without actually executing the program; contrast this to
dynamic analysis, which collects program properties by observing
program executions. Optimizing compilers have used static analysis to
eliminate unnecessary computations and thereby speed up program
executions. In the software engineering domain, static analysis has
been used, for instance, to find
<a href="http://findbugs.cs.umd.edu/papers/MoreNullPointerBugs07.pdf">potential
null pointer bugs</a> and to verify
that <a href="http://research.microsoft.com/SLAM/">device drivers
always respect API usage requirements</a>.</p>

<p>As a first step towards verifying useful properties on real
software, we <a href="/dsfinder/">surveyed</a> a corpus of
freely-available Java programs to determine what types of static
analysis would help most. Our results allow us to conclude that
understanding uses of Java Collections is key to understanding
programs; on the other hand, analyzing linked list implementations is
less likely to be useful in practice.</p>

<p> <strong>Applications.</strong> I am particularly interested in
using static analysis technology to verify domain-specific properties
of software. The key idea is to let the developer state particularly
important program properties and then to use static analysis techniques
to verify that these properties hold. I believe that the developer has a 
better chance of understanding the program than anyone else (for
example, a static analysis); but that, once the developer states
what is important, the computer can proceed to mechanically verify the stated
properties. Furthermore, static analysis still works much later in 
the development lifecycle, long after the original developer has moved
on to different projects.</p>

<p> Here are some of my ongoing and past projects: </p>

<ul>
<li> <a href="/dsfinder/">DSFinder</a>: applying straightforward static analysis techniques to see how many data structures Java programs implement in practice. (i.e. How much shape analysis do you need to do if you want to understand Java programs?)</li>
<li> Views: with <a href="http://demsky.eecs.uci.edu">Brian Demsky</a>, a novel language extension which enables developers to declaratively specify fine-grained (sub-object-level) locking policies.
<li> <a href="/research/tracematch/">Static analysis of tracematches</a>: verifying that specified sequences of program events never occur in any execution.
<li> <a href="/research/hob/">Hob</a>: verifying that all executions preserve certain set-based specifications.</li>
<li> <a href="/research/tokens/">Tokens</a>: embedding design information into Java source code.
</ul>
