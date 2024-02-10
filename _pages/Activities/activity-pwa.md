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
      embed: <iframe height="800px" width="100%" src="https://repl.it/@BillJr99/pwa-example-static?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>  
    - model: |
      title: A Dynamic PWA Using a Backend Web Service
      embed: <iframe height="400px" width="100%" src="https://repl.it/@BillJr99/pwa-example-dynamic?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe><br /><br /><iframe height="400px" width="100%" src="https://repl.it/@BillJr99/pwa-example-server?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>          
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

