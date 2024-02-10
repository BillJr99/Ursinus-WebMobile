---
layout: assignment
permalink: /Assignments/Databases
title: "CS471: Web and Mobile Development - Databases"


info:
  coursenum: CS471
  githubclassroom:
    clonelink: https://classroom.github.com/a/aGs6TRqf
  points: 100
  goals:
    - To implement a relational database in node.js
  rubric:
    - weight: 50
      description: Algorithm Implementation
      preemerging: The algorithm fails on the test inputs due to major issues, or the program fails to compile and/or run
      beginning: The algorithm fails on the test inputs due to one or more minor issues
      progressing: The algorithm is implemented to solve the problem correctly according to given test inputs, but would fail if executed in a general case due to a minor issue or omission in the algorithm design or implementation
      proficient: A reasonable algorithm is implemented to solve the problem which correctly solves the problem according to the given test inputs, and would be reasonably expected to solve the problem in the general case
    - weight: 20
      description: Code Quality and Documentation
      preemerging: Code commenting and structure are absent, or code structure departs significantly from best practice, and/or the code departs significantly from the style guide
      beginning: Code commenting and structure is limited in ways that reduce the readability of the program, and/or there are minor departures from the style guide
      progressing: Code documentation is present that re-states the explicit code definitions, and/or code is written that mostly adheres to the style guide
      proficient: Code is documented at non-trivial points in a manner that enhances the readability of the program, and code is written according to the style guide
    - weight: 20
      description: Database Schema Design
      preemerging: No schema is provided
      beginning: A database schema is provided that is flat and/or de-normalized, and would benefit from normalized structure into modular tables
      progressing: A database schema is provided that is normalized and relates tables with foreign keys
      proficient: A database schema is provided that is normalized and relates tables with foreign keys, and is documented to describe the structure and function of each table and key
    - weight: 10
      description: Writeup and Submission
      preemerging: An incomplete submission is provided
      beginning: The program is submitted, but not according to the directions in one or more ways (for example, because it is lacking a readme writeup)
      progressing: The program is submitted according to the directions with a minor omission or correction needed, and with at least superficial responses to the bolded questions throughout
      proficient: The program is submitted according to the directions, including a readme writeup describing the solution, and thoughtful answers to the bolded questions throughout
  
tags:
  - database
  
---

In this assignment, you will create a relational database using MySQL at [db4free](http://db4free.net), and connect to it from your web service.

## Part 1: Database Schema Design
First, decide what kind of data you'd like to represent.  Your database should have at least two tables that must be related through primary and foreign keys.  This can be anything you'd like, so feel free to be creative!  Whatever you decide, document your schema: list out or draw a diagram indicating the structure of your tables, and which columns are the keys.  Draw arrows (or write down a list) of which keys from which tables relate to which keys in the other table(s).

## Part 2: Web Service Backend
Next, develop a RESTful web service backend that accepts objects for storage in the relational database, and store / query those items accordingly.  At least one of your RESTful endpoints must execute a SQL JOIN statement that returns an aggregation of your tables as appropriate.

## Part 3: Testing with a Web Client
Finally, develop a client in node.js or in the web browser that inserts, queries, and lists the data from your database.

## Part 4: Presentation

Make a [Screencast](https://screencast-o-matic.com/) in which you demonstrate your program, and also review your codebase.  Imagine you are explaining how to use these API's to a new web service developer.  Give them a thorough tour!  I hope to solicit volunteers to demo their programs to the class!