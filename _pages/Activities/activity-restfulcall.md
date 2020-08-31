---
layout: activity
permalink: /Activities/RESTfulCalls
title: "Web and Mobile Development - RESTful Calls"
excerpt: "Web and Mobile Development - RESTful Calls"

info:
  goals: 
    - To explore Representational State Transfer (REST) as applied to HTTP web calls
    - To articulate the basic RESTful operations and map those to HTTP standard verbs
    - To identify arrays of objects, and elements within objects, of JSON structures
  models:
    - model: |
        <a href="https://twitter.com/NSF/status/1299367852374450185">https://twitter.com/NSF/status/1299367852374450185</a>
      title: RESTful Resources
      questions:
        - What part of the URL represents the tweet ID?
        - How do we know which user made that tweet?
        - What CRUD verb do you think is executed on this URL (Create, Read, Update, Delete)?
        - What HTTP verb do you think is executed (POST, PUT, DELETE)?
        - What is the noun in this transaction?
        - What changes in the URL if we want to get a different tweet from the same user?
    - model: | 
        <img src="../images/restfulexchange.png" alt="A RESTful Exchange Diagram">
      title: RESTful Exchanges
      questions:
        - Modify the program to print out the length of daylight (between sunrise and sunset) in hours, minutes, and seconds.  Note that the sunrise and sunset times are given in Unix epoch time, which is the number of seconds that have elapsed since January 1, 1970.
      embed: |
        <iframe height="400px" width="100%" src="https://repl.it/@BillJr99/WeatherClientExample?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>  
    - model: |
        <iframe src="https://api.weatherusa.net/v1/forecast?q=40.1915,-75.4559&daily=0&units=e&maxtime=7d" width="100%"</iframe>
      title: JSON Objects
      questions:
        - "This JSON result was returned from a web request to <a href=\"https://api.weatherusa.net/v1/forecast?q=40.1915,-75.4559&daily=0&units=e&maxtime=7d\">https://api.weatherusa.net/v1/forecast?q=40.1915,-75.4559&daily=0&units=e&maxtime=7d</a>, which obtains the 7-day forecast at Ursinus College given the College's latitude and longitude GPS coordinates.  Use a <a href=\"https://jsonformatter.org/json-pretty-print\">JSON Pretty Printer</a> to better format the JSON for reading."
        - What do the curly braces represent?
        - What does the square bracket represent?
        - Modify the program above to access this RESTful endpoint and, in a loop, print out each day's date (using <code>validt</code>) and temperature (use a <code>for</code> loop in <a href=\"https://www.w3schools.com/js/js_json_arrays.asp\">JavaScript</a>).
tags:
  - rest
  
---

