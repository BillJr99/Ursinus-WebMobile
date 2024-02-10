---
layout: assignment
permalink: /Assignments/NoSQL
title: "CS471: Web and Mobile Development - NoSQL"


info:
  coursenum: CS471
  githubclassroom:
    clonelink: https://classroom.github.com/a/I_WAcaGC
  points: 100
  goals:
    - To implement a NoSQL database in node.js using MongoDB
  rubric:
    - weight: 50
      description: Algorithm Implementation
      preemerging: The algorithm fails on the test inputs due to major issues, or the program fails to compile and/or run
      beginning: The algorithm fails on the test inputs due to one or more minor issues
      progressing: The algorithm is implemented to solve the problem correctly according to given test inputs, but would fail if executed in a general case due to a minor issue or omission in the algorithm design or implementation
      proficient: A reasonable algorithm is implemented to solve the problem which correctly solves the problem according to the given test inputs, and would be reasonably expected to solve the problem in the general case
    - weight: 40
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
  - database
  - nosql
  
---

In this assignment, you will create a collection data store using [MongoDB](http://mongodb.com), which you will manipulate from a RESTful web service.  Here is a [step-by-step guide](https://www.w3schools.com/nodejs/nodejs_mongodb.asp) to creating a database and to creating collections, followed by a [tutorial](https://www.guru99.com/node-js-mongodb.html) using MongoDB locally via a node.js library.

Note that you will need to point to a mongo installation with your url - you can [install MongoDB](https://docs.mongodb.com/manual/installation/) if you would like, or use an existing cloud service and port as your URL and port number variable parameter.

## Part 1: Web Service Backend
Using your data schema from the [Databases](./Databases) assignment, modify  your web service backend to use a MongoDB NoSQL collection instead of your relational database.  Use multiple queries with iteration, or a [lookup](https://docs.mongodb.com/manual/reference/operator/aggregation/lookup/) to implement your former relational JOIN.

### Aggregation with a Lookup
To do a lookup using the `MongoClient` library, you can do the following in node.js:

```javascript
  // https://www.w3schools.com/nodejs/nodejs_mongodb_join.asp
  var dbo = db.db('mycollection')
  dbo.collection('People').aggregate([
    { $lookup:
       {
         from: 'Enrollments',
         localField: 'PersonID',
         foreignField: 'EnrollmentID',
         as: 'PeopleEnrollments'
       }
     }
    ]).toArray(function(err, result) {
        if (err) throw err;
        db.close();
  });
```

This is equivalent to the following SQL JOIN statement:

```sql
SELECT * FROM People INNER JOIN Enrollments on Enrollments.EnrollmentID = People.PersonID
```

## Part 2: Testing with a Web Client
Hopefully, no changes are required to your web client to test your service!  Invoke your client to verify that everything continues to work normally.

## Part 3: Presentation

Make a [Screencast](https://screencast-o-matic.com/) in which you demonstrate your program, and also review your codebase.  Imagine you are explaining how to use these API's to a new web service developer.  Give them a thorough tour!  I hope to solicit volunteers to demo their programs to the class!