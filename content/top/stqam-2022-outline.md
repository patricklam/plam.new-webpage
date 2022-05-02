---
layout:     post

title:      "ECE 653 Software Testing, Quality Assurance, and Maintenance, Spring 2022"
author:     "Patrick Lam"
published:  true
url:        /stqam-2022-outline/
---

<style>
 .intro-header { display: none; }
 .sidebar-container { display: none; }
</style>

# ECE 653, Spring 2022: Syllabus
(based on a [previous version](https://ece.uwaterloo.ca/~agurfink/stqam/syllabus.html) by Prof. Arie Gurfinkel; thanks!)

## Course Description and Main Topics

This course will provide an introduction to software testing and quality assurance techniques. The students will learn a wide spectrum of techniques and tools that can be used to improve and evaluate software quality ranging from mature testing methodologies to cutting edge automated verification algorithms. Topics to be covered include: coverage criteria (graph, data-flow, and logic coverage), symbolic execution (static, dynamic, concolic), constraint solving (SMT), inductive invariants, automatic deductive verification, automatic invariant synthesis, and Software Model Checking.

### Recommended Background

The course will include programming assignments in Java/C/Python. Background in Compilers and Logic is useful, but is not required.

## Mechanics

### Course Website

[https://patricklam.ca/stqam-2022](https://patricklam.ca/stqam-2022)

We will also likely use [Piazza](https://piazza.com) for Q&A.

### Instructor

[Prof. Patrick Lam](https://patricklam.ca), patrick.lam@uwaterloo.ca

### Teaching Assistant

TBA

### Lectures

Tuesdays and Thursdays, 10:00-11:30, E7-4053

### Office Hours

By request

### Textbook

No required textbook. Lecture slides, lecture notes, and reading material will be provided.

### Grading

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

## Project

There are two choices of project. Projects can be done in groups of 2. You must declare your project by the end of Week 8. All projects must be approved by the instructor. Talk to me. Sooner the better. Deadline for project approval is Week 10. Projects are due by the last day of class.

The exact project deliverables depend on the project chosen. All projects must include approximately a 10 page report. The length of the report depends on the amount of code involved in the project (i.e., more code means shorter report).

## Project choice 1: applying a technique

Throughout the course, we will learn of several verification techniques including fuzzing, symbolic execution, and deductive verification. In this project, you have to propose a program or an algorithm to verify with one of the techniques that we have studied in the course. The complexity of the artifact being verified will depend on the verification technique involved. The more complex the verification technique, the simpler the artifact being verified can be.

### Deliverables

* **Code and any other artifacts you produce.** If the project is done in groups, request us to create a group repository for you. All code is to be submitted into the group repository (if the project is done in a group), or in your course repository (if the project is done independently)

* **Report**. An approximately 10 page report (can be 9, can be 15, cannot be 5) describing your experience, any theoretical foundations, any design decisions, and implementation that you had to do. Report is to be submitted in PDF. Suggested style is [LNCS](https://www.springer.com/gp/computer-science/lncs/conference-proceedings-guidelines). An [Overleaf](https://overleaf.com) template is [here](https://www.overleaf.com/latex/templates/springer-lecture-notes-in-computer-science/kzwwpvhwnvfj). If you insist on using MS Word, a template is available [here](https://resource-cms.springernature.com/springer-cms/rest/v1/content/7117506/data/v1).

## Project choice 2: independent study

Quality assurance and automated verification are active areas of research. In this project, you will conduct an independent study into a topic that is closely related to the material of the course but is not explicitly covered. The study must include reading at least two scientific papers. The outcome of the project can be an implementation of new technique or a report on the topic studied.

### Deliverable

* **Report**. An approximately 15 page report (can be 14, can be 20, cannot be 10) critically reviewing the paper that you have selected. Your review must be critical and in-depth. Simply repeating the papers verbatim is not sufficient. You must show that you have learned and understood something new. This can be done by contrasting different techniques, creating new examples, and, potentially, implementing the techniques. If your report involves implementation, the page limit of the report can be reduced.  Report is to be submitted in PDF. Suggested style is [LNCS](https://www.springer.com/gp/computer-science/lncs/conference-proceedings-guidelines). An [Overleaf](https://overleaf.com) template is [here](https://www.overleaf.com/latex/templates/springer-lecture-notes-in-computer-science/kzwwpvhwnvfj). If you insist on using MS Word, a template is available [here](https://resource-cms.springernature.com/springer-cms/rest/v1/content/7117506/data/v1).

## COVID-19 Contingency Policy

At this stage, we can hope that Spring 2022 will proceed in person without COVID-related disruptions. In the case of a disruption to in-person classes, I will record lectures and post them on YouTube. In the case of a disruption to in-person final exams, the final exam will be take-home as well.

All other course work is already being conducted in a way that is compatible with online interaction and no change will be necessary.

If you get COVID, you can submit a Verification of Illness and we'll 
shuffle things around to make things work.

If I get COVID, I will cancel lectures until I get better, and (after I get better), I will record lectures covering the relevant period. (I think we all hope I don't get COVID.)

As much as we'd like it to be, the pandemic is still not over, and I urge you to think about the risks that you choose to take. You are probably not going to die of COVID, but you are definitely better off not getting it (or getting it again); every time you get it you run the risk of getting possible long-term aftereffects. 

## Course Policies

By registering for this class, students agree to the following class policies:

**Independent work**. All work turned in will be that of the individual student unless stated otherwise. Violations would result in zero credit to all students concerned. [Policy 71](https://uwaterloo.ca/secretariat/policies-procedures-guidelines/policy-71) will be followed for any discovered cases of plagiarism.

**Lateness**. You have 2 days of lateness to use on assignment submissions throughout the term. Each day you hand in an assignment late consumes one of the days of lateness. If you consume all of your late days, assignments that are still late will get 0 marks. You can only hand in an assignment up to the time all assignments are returned. Missed assignments get 0 marks. For example, you may hand in A1 two days late and A2 on time, or you can hand in A1 one day late and A2 one day late.

**Missed Quizzes**. If you miss a quiz, you will receive 0 marks for the quiz. If you have a legitimate reason (at the discretion of the instructor) that you cannot take quiz, and obtain permission from the instructor **a week** in advance, the percentage for the quiz may be shifted to the final. No alternative quiz time will be provided.

## University Policies

**Academic Integrity**. In order to maintain a culture of academic integrity, members of the University of Waterloo community are expected to promote honesty, trust, fairness, respect and responsibility. [Check http://www.uwaterloo.ca/academicintegrity for more information.]

**Grievance**. A student who believes that a decision affecting some aspect of his/her university life has been unfair or unreasonable may have grounds for initiating a grievance. Read Policy 70, Student Petitions and Grievances, Section 4, http://www.adm.uwaterloo.ca/infosec/Policies/policy70.htm. When in doubt please be certain to contact the departments administrative assistant who will provide further assistance.

**Discipline**. A student is expected to know what constitutes academic integrity [check http://www.uwaterloo.ca/academicintegrity] to avoid committing an academic offense, and to take responsibility for his/her actions. A student who is unsure whether an action constitutes an offense, or who needs help in learning how to avoid offenses (e.g., plagiarism, cheating) or about rules for group work/collaboration should seek guidance from the course instructor, academic advisor, or the undergraduate Associate Dean. For information on categories of offenses and types of penalties, students should refer to Policy 71, Student Discipline, http:://www.adm.uwaterloo.ca/infosec/Policies/policy71.htm. For typical penalties check Guidelines for the Assessment of Penalties, http://www.adm.uwaterloo.ca/infosec/guidelines/penaltyguidelines.htm.

**Appeals**. A decision made or penalty imposed under Policy 70 (Student Petitions and Grievances) (other than a petition) or Policy 71 (Student Discipline) may be appealed if there is a ground. A student who believes he/she has a ground for an appeal should refer to Policy 72 (Student Appeals) http://www.adm.uwaterloo.ca/infosec/Policies/policy72.htm.

**Note for Students with Disabilities**. The AccessAbility Services, located in Needles Hall, Room 1132, collaborates with all academic departments to arrange appropriate accommodations for students with disabilities without compromising the academic integrity of the curriculum. If you require academic accommodations to lessen the impact of your disability, please register with the AccessAbility Services at the beginning of each academic term.

**Territorial Acknowledgement**. The University of Waterloo acknowledges that much of our work takes place on the traditional territory of the Neutral, Anishinaabeg and Haudenosaunee peoples. Our main campus is situated on the Haldimand Tract, the land promised to the Six Nations that includes six miles on each side of the Grand River.
