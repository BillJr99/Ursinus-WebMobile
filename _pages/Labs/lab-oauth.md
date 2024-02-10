---
layout: assignment
permalink: /Labs/OAuth
title: "Web and Mobile Development: OAuth Receiver"


info:
  coursenum: CS471
  githubclassroom:
    clonelink: https://classroom.github.com/a/epgvwhOa
  points: 100
  goals:
    - To implement the OAuth protocol with a node.js receiver
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
      progressing: The program is submitted according to the directions with a minor omission or correction needed
      proficient: The program is submitted according to the directions, including a readme writeup describing the solution

tags:
  - oauth
  
---

In this lab, you will connect to a service using OAuth and obtain a key \[[^1]\].  We will implement a proper online OAuth protocol, such that a node.js web service will receive the callback from the service provider to parse the token for the user.  We will use [Github](https://docs.github.com/en/rest) in this example, but you may substitute any service provider you choose (as long as it offers a 3-Legged OAuth option with a callback).

## Part 1: Allowing the User to Log In

Direct the user to the github page at `https://github.com/login/oauth/authorize?client_id=<CLIENT ID>&redirect_uri=http://<YOUR REPL.IT PROJECT URL>/oauth/redirect&state=<RANDOM STRING>`

You can generate a Client ID and Client Secret for your application at the [Github Developer page](https://docs.github.com/en/developers/apps/creating-an-oauth-app).

## Part 2: Intercepting the OAuth Callback Redirection

Deploy a repl.it project in node.js that uses `express` to capture a call to `/oauth/redirect` (which will be invoked automatically by OAuth redirection step above).

The HTTP request will contain a query parameter called `code` that you can extract.  You will also receive the `state` string that you originally passed - this should equal your original string.  In the handler for this endpoint, use the code to make a POST request to:

`https://github.com/login/oauth/access_token?client_id=<CLIENT ID>&client_secret=<CLIENT SECRET>&code=<CODE>`

with a header: `accept: application/json`.

The response to this request will contain a body parameter called `access_token`.  This is the user's access token to utilize the Github API on their behalf.

You can pass a user ID back to the user, to which you associate the corresponding `access_token` in a secure data store.  Ideally, this would be encrypted.  If the token should fail at some point due to expiration (or if a token doesn't exist for this user), you could automatically trigger the OAuth process again.

## Part 3: Accessing the Github User's Information

Perform a GET request to `https://api.github.com/user` with header: `Authorization: token <ACCESS TOKEN>` to test that the OAuth protocol you implemented successfully authenticated the user.  You could use this account information as the basis of your own app authentication, avoiding the need to store a password for the user.

[^1]: [https://www.sohamkamani.com/blog/javascript/2018-06-24-oauth-with-node-js/](https://www.sohamkamani.com/blog/javascript/2018-06-24-oauth-with-node-js/)