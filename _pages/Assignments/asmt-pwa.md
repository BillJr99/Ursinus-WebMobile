---
layout: assignment
permalink: /Assignments/PWA
title: "CS471: Web and Mobile Development - PWA"


info:
  coursenum: CS471
  githubclassroom:
    clonelink: https://classroom.github.com/a/P7BL-rBc
  points: 100
  goals:
    - To implement a Progressive Web App (PWA)
  rubric:
    - weight: 60
      description: Algorithm Implementation
      preemerging: The algorithm fails on the test inputs due to major issues, or the program fails to compile and/or run
      beginning: The algorithm fails on the test inputs due to one or more minor issues
      progressing: The algorithm is implemented to solve the problem correctly according to given test inputs, but would fail if executed in a general case due to a minor issue or omission in the algorithm design or implementation
      proficient: A reasonable algorithm is implemented to solve the problem which correctly solves the problem according to the given test inputs, and would be reasonably expected to solve the problem in the general case
    - weight: 30
      description: Code Quality and Documentation
      preemerging: Code commenting and structure are absent, or code structure departs significantly from best practice, and/or the code departs significantly from the style guide
      beginning: Code commenting and structure is limited in ways that reduce the readability of the program, and/or there are minor departures from the style guide
      progressing: Code documentation is present that re-states the explicit code definitions, and/or code is written that mostly adheres to the style guide
      proficient: Code is documented at non-trivial points in a manner that enhances the readability of the program, and code is written according to the style guide
    - weight: 10
      description: Writeup and Submission
      preemerging: An incomplete submission is provided
      beginning: The program is submitted, but not according to the directions in one or more ways (for example, because it is lacking a readme writeup)
      progressing: The program is submitted according to the directions with a minor omission or correction needed, and with at least superficial responses to the bolded questions throughout
      proficient: The program is submitted according to the directions, including a readme writeup describing the solution, and thoughtful answers to the bolded questions throughout
  
tags:
  - pwa
  
---

In this assignment, you will create a Progressive Web App (PWA) using the model discussed in class.

## Part 1: PWA
You may choose the topic of your PWA listing, but I suggest developing a client that utilizes a backend service that you've already created.  The requirements are that the PWA must:

* Intercept its fetch calls with a `serviceWorker` and provide a cache
* Call a web service to dynamically obtain data
* Present that data using a card-style PWA
* Link to something or provide a functional front-end to facilitate interaction with each card

## Part 2: Presentation

Make a [Screencast](https://screencast-o-matic.com/) in which you demonstrate your program, and also review your codebase.  Imagine you are explaining how to use these API's to a new web service developer.  Give them a thorough tour!  I hope to solicit volunteers to demo their programs to the class!