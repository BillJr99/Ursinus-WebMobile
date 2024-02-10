---
layout: assignment
permalink: /Projects/Final
title: "Web and Mobile Development - Final Project"


info:
  coursenum: CS471
  githubclassroom:
    clonelink: https://classroom.github.com/g/mP1CDFqH
  points: 100
  goals:
    - To demonstrate the fundamental concepts of programming in a unified project
    - To work effectively as a member of a small group using collaborative tools for software development
  rubric:
    - weight: 40
      description: Algorithm Implementation
      preemerging: The algorithm fails on the test inputs due to major issues, or the program fails to compile and/or run
      beginning: The algorithm fails on the test inputs due to one or more minor issues
      progressing: The algorithm is implemented to solve the problem correctly according to given test inputs, but would fail if executed in a general case due to a minor issue or omission in the algorithm design or implementation
      proficient: A reasonable algorithm is implemented to solve the problem which correctly solves the problem according to the given test inputs, and would be reasonably expected to solve the problem in the general case
    - weight: 10
      description: Test Cases
      preemerging: Testing was performed outside of the unit test framework, or not performed at all
      beginning: Trivial test cases are provided in a unit test framework
      progressing: Test cases that cover some, but not all, boundary cases and branches of the program are provided
      proficient: Test cases that cover all boundary cases and branches of the program are provided
    - weight: 20
      description: Service Endpoint Interface Design
      preemerging: Improper service endpoints are given, or use verbs instead of a CRUD model
      beginning: An arbitrary mapping of service endpoints is given to HTTP verbs (for example, only GET or POST verbs are used)
      progressing: Some service endpoints are ambiguous or improperly mapped
      proficient: Service endpoints are thoroughly defined for the application chosen, with CRUD endpoints that represent nouns that are appropriately mapped to HTTP verbs      
    - weight: 10
      description: Code Quality and Documentation
      preemerging: Code commenting and structure are absent, or code structure departs significantly from best practice, and/or the code departs significantly from the style guide
      beginning: Code commenting and structure is limited in ways that reduce the readability of the program, and/or there are minor departures from the style guide
      progressing: Code documentation is present that re-states the explicit code definitions, and/or code is written that mostly adheres to the style guide
      proficient: Code is documented using Swagger at non-trivial points in a manner that enhances the readability of the program, and code is written according to the style guide
    - weight: 10
      description: Presentation
      preemerging: No presentation was provided, the presentation could not be viewed, or the presentation was not on the subject of the final project
      beginning: A presentation was provided that summarizes the project, but does not provide a demo or discuss broader impacts
      progressing: A presentation was provided that summarizes the project, provides a demo, and discusses broader impacts
      proficient: A presentation was provided that that summarizes the project, provides a demo, discusses broader impacts, and highlights challenges overcome and methodologies for developing the system as a group
    - weight: 10
      description: Writeup and Submission
      preemerging: An incomplete submission is provided
      beginning: The program is submitted, but not according to the directions in one or more ways (for example, because it is lacking a readme writeup)
      progressing: The program is submitted according to the directions with a minor omission or correction needed
      proficient: The program is submitted according to the directions, including a readme writeup describing the solution

tags:
  - project
  
---

In this project, you will propose a topic of your choosing and a group of at least 2 and up to 3 total members.  The project must be approved by the instructor before it may commence, but the topic is entirely up to you.  Multidisciplinary projects with a broader impact are encouraged, and you are welcome to collaborate with a stakeholder outside the department for inspiration on potential projects (this person is not to contribute code, only disciplinary context).  You are also encouraged to identify a stakeholder (please see me for assistance in this regard) who will advise you on the design of your project and test the final implementation.  

You will use git or another version control system to coordinate between your team.  

First, propse a project along with its RESTful interface definition.  Include your calls and data schemas (as if you were defining a Swagger document).  Your interface should include at least one authenticated user database or NoSQL lookup, authenticated with OAuth or a JWT token.  Then, implement your project server and client!  Finally, prepare as a team a project presentation using a screencast (such as [Screencast-O-Matic](https://screencast-o-matic.com/)) that you will share with the class for final presentations.  Alternatively, you may choose to present to a live class audience, as time permits.

Some possible projects include:

* Online debugging table for introductory students: a service-based mobile-friendly site that supports exception posting, commenting, resolution, and searching
* [Canvas](https://canvas.instructure.com/doc/api/) Course Manager: An organizational utility for students using Canvas with a personal [iCal](https://en.wikipedia.org/wiki/ICalendar) generator for your personal calendar

## Extra Credit (Up to 30%)
If you deploy your project publicly and make your repository/repositories publicly open source (please note this in your README), I will award 10% extra credit to your project.  Additionally, if you propose to deploy your project to a stakeholder group, and successfully do so, I will award 20% extra credit to your project!  Please note that you must propose the stakeholder group to the instructor when the interface and/or project proposal are due, and the instructor and stakeholder group must agree up front to participate!