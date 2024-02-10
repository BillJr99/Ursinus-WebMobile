---
layout: assignment
permalink: /Assignments/Service
title: "CS471: Web and Mobile Development - RESTful Services"


info:
  coursenum: CS471
  githubclassroom:
    clonelink: https://classroom.github.com/a/8DnXHFfM
  points: 100
  goals:
    - To implement a web service in node.js using express and mongoose
  rubric:
    - weight: 40
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
    - weight: 20
      description: Service Endpoint Interface Design
      preemerging: Improper service endpoints are given, or use verbs instead of a CRUD model
      beginning: An arbitrary mapping of service endpoints is given to HTTP verbs (for example, only GET or POST verbs are used)
      progressing: Some service endpoints are ambiguous or improperly mapped
      proficient: Service endpoints are thoroughly defined for the application chosen, with CRUD endpoints that represent nouns that are appropriately mapped to HTTP verbs
    - weight: 10
      description: Writeup and Submission
      preemerging: An incomplete submission is provided
      beginning: The program is submitted, but not according to the directions in one or more ways (for example, because it is lacking a readme writeup)
      progressing: The program is submitted according to the directions with a minor omission or correction needed, and with at least superficial responses to the bolded questions throughout
      proficient: The program is submitted according to the directions, including a readme writeup describing the solution, and thoughtful answers to the bolded questions throughout
  
tags:
  - restservice
  
---

In this assignment, you will design a RESTful service interface and implement it using node.js.  You will test your service with a client that you will implement in node.js or in a web browser using JavaScript.

## Part 1: Stakeholder-Based Design

Choose a partner with whom you will discuss your model interface.  Your RESTful endpoints and data types should be well-established here.  Please document the results of this discussion and your overall design in your README.  I should be able to deploy and use your service by just reading your design document in the README.

Prior to proceeding, notify the instructor of the general service that you plan to implement, and the design and interface you plan to utilize.

## Part 2: Service Implementation
Craete your model, routes, and `express` service in node.js, according to the design you determined with your partner.

## Part 3: Service Client
Develop a service client in node.js or a browser webpage to invoke each operation of your service.

## Part 4: Presentation

Make a [Screencast](https://screencast-o-matic.com/) in which you demonstrate your program, and also review your codebase.  Imagine you are explaining how to use these API's to a new web service developer.  Give them a thorough tour!  I hope to solicit volunteers to demo their programs to the class!