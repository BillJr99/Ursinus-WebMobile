---
layout: assignment
permalink: /Assignments/ServiceClient
title: "CS471: Web and Mobile Development - Service Clients"


info:
  coursenum: CS471
  githubclassroom:
    clonelink: https://classroom.github.com/a/Zg7pvINg
  points: 100
  goals:
    - To implement a web service client in node.js
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
  - restclient
  
---

In this assignment, you will choose two REST service endpoints and integrate them together.  You may select any two endpoints you want.  

## Part 1: Service Endpoint Integration

Here are some examples you can choose from (but you don't have to pick one of these!):

* [Google Calendar](https://developers.google.com/calendar/v3/reference)
* [Canvas](https://canvas.instructure.com/doc/api/)
* [Yahoo! Finance](https://rapidapi.com/apidojo/api/yahoo-finance1)
* [Pokemon](https://pokeapi.co/docs/v2)
* [Nexmo SMS Text Messaging](https://developer.nexmo.com/api/sms)
* [International Space Station Location](https://wheretheiss.at/w/developer)
* [Spoonacular Recipes](https://spoonacular.com/food-api/docs)
* [Open Movie Database](http://www.omdbapi.com/)
* [Text to Speech](http://www.voicerss.org/api/)
* [SEPTA](http://www3.septa.org/api/)

Please advise the instructor of your choices before you begin (this is not intended to restrict you, but just to determine if you need any additional resources to complete the assignment based on the choices you make).  

Regardless of the services you choose, you should:

1. Connect to one service, download and parse the result
2. Use that result to form the input of a request to a second service endpoint, and then process that result accordingly

In your README, please include a paragraph description of your intended audience: who can use your program, and how does it improve their workflow, their life, and/or their community?

## Part 2: Presentation

Make a [Screencast](https://screencast-o-matic.com/) in which you demonstrate your program, and also review your codebase.  Imagine you are explaining how to use these API's to a new web service developer.  Give them a thorough tour!  I hope to solicit volunteers to demo their programs to the class!