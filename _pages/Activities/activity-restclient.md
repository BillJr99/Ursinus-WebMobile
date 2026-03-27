---
layout: activity
permalink: /Activities/ServiceClient
title: "Web and Mobile Development - RESTful Service Client"


info:
  additional_reading:
    - title: "GitHub OAuth Login with Node.js"
      link: "http://thecodebarbarian.com/github-oauth-login-with-node-js.html"
  goals: 
    - To explore Representational State Transfer (REST) as applied to HTTP web calls
    - To use OAuth to enable user authentication when interacting with a RESTful web service
  models:
    - model: |
        <iframe src="http://thecodebarbarian.com/github-oauth-login-with-node-js.html" width="100%" height="1068" scrolling="yes"></iframe>
      title: RESTful Service Clients
      questions:
        - "Using the <a href=\"http://thecodebarbarian.com/github-oauth-login-with-node-js.html\">tutorial above</a>, write a program to support OAuth login to GitHub, writing a web service using express to capture the callback with the user's token.  You can enter the repl.it URL into a new tab in your browser to load the page, and set that same URL as the callback URL (add <code>/oauth-callback</code> to the callback URL field on the GitHub application page)."
        - How could we use this token in place of a user account when developing our own web services?  How could we associate a user with a token, while ensuring that subsequent tokens for the same user are also associated with that same user?  In other words, how can we ensure that not just any valid GitHub user can masquerade as a user on our eventual service?
      embed: |
        <iframe src="https://www.billmongan.com/Ursinus-WebMobile/assets/code-viewer.html?zip=https%3A%2F%2Fraw.githubusercontent.com%2FBillJr99%2FUrsinus-WebMobile%2Fgh-pages%2Ffiles%2Freplit%2FWeatherClientExample.zip&title=WeatherClientExample"
          height="600px"
          width="100%"        
          scrolling="yes"
          frameborder="no"
          allowfullscreen="true"
          sandbox="allow-scripts allow-same-origin">
        </iframe>         
        
tags:
  - rest
  
---

