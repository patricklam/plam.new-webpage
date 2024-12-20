---
layout:     post

title:      "ECE 653 Software Testing, Quality Assurance, and Maintenance, Spring 2022"
author:     "Patrick Lam"
published:  true
url:        /stqam-2022-grading/
---

<style>
 .intro-header { display: none; }
 .sidebar-container { display: none; }
</style>

# ECE 653 S22: Grading

* Assignments: 35%
    * Assignment 1: 10%
    * Fuzz Battle: 5%
    * Assignment 2: 10%
    * Assignment 3: 10%
* Quizzes: 20%
    * Quiz 1: 10%
    * Quiz 2: 10%
* Final Exam: 25%
* Project: 20%

All assignments, quizzes, and tests that are submitted online will be returned online. Submissions will be by pushing to [gitlab](https://git.uwaterloo.ca).

Final exam will be in-person.

All quizzes are take home, open book, closed internet. Each online test will be time limited and must be completed within 3 days. That is, you can pick the best time to take the test, but once you start, you have to finish within the given time limit.

You must pass at least the two written tests and pass the assignments to pass the course. The final grade is computed using the following formula:

```
def grade(A, P, Q1, Q2, F):
    """Final grade calculation.

    A, P, Q1, Q2, F are grades for assignments, project, Quiz 1, Quiz 2,
    and the Final, respectively. Normalized to 100%.
    """
    tests_above_fifty = len(list(filter(lambda x: x >= 50, [Q1, Q2, F])))

    normal = 0.35*A + 0.1*Q1 + 0.1*Q2 + 0.25*F + 0.2*P
    if tests_above_fifty >= 2 and A > 50:
        return normal
    else:
        return 47
```

# COVID-19 Contingency Policy

At this stage, we can hope that Spring 2022 will proceed in person without COVID-related disruptions. In the case of a disruption to in-person classes, I will record lectures and post them on YouTube. In the case of a disruption to in-person final exams, the final exam will be take-home as well.

All other course work is already being conducted in a way that is compatible with online interaction and no change will be necessary.

If you get COVID, you can submit a Verification of Illness and we'll 
shuffle things around to make things work.

If I get COVID, I will cancel lectures until I get better, and (after I get better), I will record lectures covering the relevant period. (I think we all hope I don't get COVID.)

As much as we'd like it to be, the pandemic is still not over, and I urge you to think about the risks that you choose to take. You are probably not going to die of COVID, but you are definitely better off not getting it (or getting it again); every time you get it you run the risk of getting possible long-term aftereffects. 

# Course Policies

By registering for this class, students agree to the following class policies:

**Independent work**. All work turned in will be that of the individual student unless stated otherwise. Violations would result in zero credit to all students concerned. [Policy 71](https://uwaterloo.ca/secretariat/policies-procedures-guidelines/policy-71) will be followed for any discovered cases of plagiarism.

**Lateness**. You have 2 days of lateness to use on assignment submissions throughout the term. Each day you hand in an assignment late consumes one of the days of lateness. If you consume all of your late days, assignments that are still late will get 0 marks. You can only hand in an assignment up to the time all assignments are returned. Missed assignments get 0 marks. For example, you may hand in A1 two days late and A2 on time, or you can hand in A1 one day late and A2 one day late.

**Missed Quizzes**. If you miss a quiz, you will receive 0 marks for the quiz. If you have a legitimate reason (at the discretion of the instructor) that you cannot take quiz, and obtain permission from the instructor **a week** in advance, the percentage for the quiz may be shifted to the final. No alternative quiz time will be provided.
