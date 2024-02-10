---
layout: activity
permalink: /Activities/Cache
title: "Web and Mobile Development - Cache"


info:
  goals: 
    - To explain the benefit and risk of using a cache
    - To use the HEAD verb to check the modified date on an item for refreshing
  models:
    - model: |
        <img src="../images/activity-cache/httphead.png" alt="HTTP HEAD Example">
      title: Checking Modification Date Using the HEAD verb
      questions:
        - How is this less expensive than making a full GET request, when we still need to do that anyway if the modification date from the HEAD response is newer than the version we have?
        - In addition to the response data (such as the web page), what other information would you need to store for the cache to be effective?
        - What kind of data structure would you use to save values into the cache?        
        - How often should you refresh the cache?
    - model: |
        <div align="left">
        Review <a href="https://medium.com/@danielsternlicht/caching-like-a-boss-in-nodejs-9bccbbc71b9b">this tutorial</a> that uses <code>node-cache</code> to return data from a cache lookup, calling a function to insert into the cache only if the data is out of date or nonexistent.
        </div>
      title: "Internal Caches with node-cache"
      questions:
        - "What data structure do you think underlies <code>node-cache</code>?"
        
tags:
  - cache
  
---

