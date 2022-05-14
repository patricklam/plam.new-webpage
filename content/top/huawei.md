---
layout:     post

title:      "Research Collaborations (Huawei)"
author:     "Patrick Lam"
published:  false
---

# Areas I’d be keen to work on again

Historically I’ve done work on various verification-related topics, and would be happy to revisit these areas. My current students aren’t working in these areas but I’d be willing to take on new ones who would work on them.

## Verification-adjacent
* I participated in a project where we generated test cases that would exhaustively test the behaviour of an RMA implementation according to the specification [[OOPSLA 2016](/papers/16.oopsla.rma-alloy.pdf)]; although I haven’t thought about it in too much detail, I do know that GPUs have to worry about some sort of memory consistency/manual cache management. I think there is interesting work to be done here, with proper language extensions plus static analyses.
* I also participated in a project where we model checked C concurrent code, using SAT solver technology to observe executions and generate new behaviours, until exploring all reachable behaviours. [[OOPSLA 2015](/papers/15.oopsla.satcheck.pdf)]

## Static analysis
* With my now-graduated PhD student Jon Eyolfson, we developed a static analysis to verify that C++ class implementations respected “const” annotations, even in the presence of internal changes like caches (not publicly visible). We didn’t yet manage to publish this work but we have published empirical studies on the use of const in C++ codebases.

In general I’d really like the idea of getting developer-provided information through to the compiler and applying it for either performance (in your case) or correctness (leveraging powerful static analyses.)

# Projects I am currently working on
One way that developers indirectly express information about their code is through test cases. I’m interested in finding ways to leverage that for static analyses. They are going to be difficult to use in optimizations (because they are extremely incomplete), but I think they do point at important program executions and can point at where analyses should spend more resources to get precision.

* I am collaborating with Gregor Richards and we share a student who is working on virtual machine research. He’s still early in program and hasn’t picked a specific project.
* I have some research studying semantic versioning and breaking changes; the goal is to better support developers working in modern ecosystems, where dependencies change all the time. For instance, it would be great to tell the developer that this dependency upgrade is safe and urgent, whereas that upgrade is going to require mitigation in the developer’s codebase, because the API changed.
* I’m also working on automatic refactoring and augmentation of existing test suites.

The last two projects are pretty software-engineering-ish and I think Huawei people are looking more at the other points.

Thanks! I’m always happy to chat about potential collaborations.

