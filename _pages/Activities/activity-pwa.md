---
layout: activity
permalink: /Activities/PWA
title: "Web and Mobile Development - Progressive Web Apps"


info:
  goals: 
    - To implement a Progressive Web App (PWA) in JavaScript, HTML5, and CSS
  models:
    - model: |
        Review the example below as a class.
      title: A Static Progressive Web App for Mobile Clients
      questions:
        - How do we name elements in HTML5 for dynamic updating?  What is the name of the main body element that we're updating?
        - What JavaScript command is used to set the content of a web page element?
        - How do we define each list item to be a box?
        - How do we ensure that each box appears in a dynamically-sized grid?
        - How do we intercept a fetch and serve the content locally, serving as a cache?
        - Load the web page in a Chrome browser on your mobile device, if you have one.  From the Chrome menu, you can add the app to your home screen.  Try changing the navigation color and the home screen icon.
      embed: <iframe
  src="https://www.billmongan.com/Ursinus-WebMobile/assets/code-viewer.html?zip=https%3A%2F%2Fraw.githubusercontent.com%2FBillJr99%2FUrsinus-WebMobile%2Fgh-pages%2Ffiles%2Freplit%2Fpwa-example-static.zip&title=pwa+example+static"
  scrolling="yes"
  frameborder="no"
  allowfullscreen="true"
  sandbox="allow-scripts allow-same-origin">
</iframe>  
    - model: |
      title: A Dynamic PWA Using a Backend Web Service
      embed: <iframe
  src="https://www.billmongan.com/Ursinus-WebMobile/assets/code-viewer.html?zip=https%3A%2F%2Fraw.githubusercontent.com%2FBillJr99%2FUrsinus-WebMobile%2Fgh-pages%2Ffiles%2Freplit%2Fpwa-example-dynamic.zip&title=pwa+example+dynamic"
  scrolling="yes"
  frameborder="no"
  allowfullscreen="true"
  sandbox="allow-scripts allow-same-origin">
</iframe><br /><br /><iframe
  src="https://www.billmongan.com/Ursinus-WebMobile/assets/code-viewer.html?zip=https%3A%2F%2Fraw.githubusercontent.com%2FBillJr99%2FUrsinus-WebMobile%2Fgh-pages%2Ffiles%2Freplit%2Fpwa-example-server.zip&title=pwa+example+server"
  scrolling="yes"
  frameborder="no"
  allowfullscreen="true"
  sandbox="allow-scripts allow-same-origin">
</iframe>          
      questions:
        - "In <code>script.js</code>, where has the <code>courses</code> array gone?"
        - How has the service worker changed to intercept fetches and forward them to the web server if they are remote data calls?
        - What would happen if the server side data changed?  What could we do about this?
        
tags:
  - pwa
  - html5
  - javascript
  - css
  
---

