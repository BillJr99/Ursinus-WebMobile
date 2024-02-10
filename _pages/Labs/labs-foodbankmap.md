---
layout: assignment
permalink: /Labs/FoodBankMap
title: "CS471: Web and Mobile Development - Food Bank Map RESTful Service"


info:
  coursenum: CS471
  githubclassroom:
    clonelink: https://classroom.github.com/a/2v9HyXs8
  points: 100
  goals:
    - To implement a web service in node.js using express and mongoose
    - To develop a front-end page that accesses that web service through the Google Maps API interface
  rubric:
    - weight: 40
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
    - weight: 20
      description: Service Endpoint Interface Design
      preemerging: Improper service endpoints are given, or use verbs instead of a CRUD model
      beginning: An arbitrary mapping of service endpoints is given to HTTP verbs (for example, only GET or POST verbs are used)
      progressing: Some service endpoints are ambiguous or improperly mapped
      proficient: Service endpoints are thoroughly defined for the application chosen, with CRUD endpoints that represent nouns that are appropriately mapped to HTTP verbs
    - weight: 10
      description: Writeup and Submission
      preemerging: An incomplete submission is provided
      beginning: The program is submitted, but not according to the directions in one or more ways (for example, because it is lacking a readme writeup)
      progressing: The program is submitted according to the directions with a minor omission or correction needed, and with at least superficial responses to the bolded questions throughout
      proficient: The program is submitted according to the directions, including a readme writeup describing the solution, and thoughtful answers to the bolded questions throughout
  
tags:
  - restservice
  - googlemap
  - html
  
---

In this lab, you will design a RESTful service interface that represents food bank locations, and implement it using node.js and a browser frontend that uses the Google Maps API \[[^1]\].  Users should be able to POST food bank locations, and the browser script should place markers on the map along with the user's current location.

## Part 1: Service Backend and Testing
Design a RESTful web service in node.js that stores the name and address of food banks.  In addition to storing the name and address, you should store the latitude and longitude of the location when you create or update a resource.  You can lookup the latitude and longitude for the address by calling [this API from ArcGIS](https://developers.arcgis.com/labs/rest/search-for-an-address/).

You should support:

* GET: Retrieve a list of all food banks
* POST: Create a food bank given its name and address
* PUT: Update a food bank given its ID, its new name and/or new address
* DELETE: Delete a food bank given its ID

Test each of these using a client program, a web browser, or a cURL command, and show the results of your testing.

To support a web-based frontend, we will need to enable [CORS](../Activities/CORS) on this server.

## Part 2: Google Map Frontend Configuration and Tutorial
The example below shows a minimal working example of a Google Map that plots the location of Ursinus College, and plots a custom marker with a location given by the current location as obtained through the browser client.  You can change this marker icon later by calling the `Marker.setIcon(image);` function.

<iframe height="400px" width="100%" src="https://repl.it/@BillJr99/GoogleMapExample?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>

### Elements of the Working Example

#### Adding an Element to Hold the Map
First, set up a web page with a `div` element to hold the map.  We'll call it `map`.

```javascript
<!DOCTYPE html>
<html>
<body>
<div id="map"></div>
</body>
</html>
```

Between the `html` and `body` opening tags, we can add CSS styling inline to set the size of the map:

```javascript
  <html>
  <head>
    <style>
       /* Set the size of the div element that contains the map */
      #map {
        height: 400px;  /* The height is 400 pixels */
        width: 100%;  /* The width is the width of the web page */
       }
    </style>
  </head>
  <body>
  ...
  </body>
```

Inside the `<body>`, let's call the Google Maps API script to render the map.  We'll provide a `callback` parameter which will invoke a script that we'll write in our page.  We'll call this function `initMap`.  You'll also need an API Key, which we'll discuss shortly.

```javascript
    <body>
    ...
    <script defer
    src="https://maps.googleapis.com/maps/api/js?key=YOUR_API_KEY_HERE&callback=initMap">
    </script>
    ...
    </body>
```

To implement the `initMap` function, add a `<script>` tag inside your `<body>` tag.  Our function creates a marker at a given latitude and longitude, and plots it on the map.

Note that the `map` variable is declared without a `var` tag.  This places the variable into the global scope, so that we can access it from other script functions later.

```javascript
    <body>
    <script>
    function initMap() {
      // The location of Ursinus College
      var ursinus = {lat: 40.1915, lng: -75.4559};
      // The map, centered at Ursinus
      map = new google.maps.Map(
          document.getElementById('map'), {zoom: 4, center: ursinus}); // no var == global scope
      // The marker, positioned at Ursinus College
      var marker = new google.maps.Marker({position: ursinus, map: map});
    }    
    </script>
    ...
    </body>
```

At the end of the `initMap()` function, you can call `navigator.geolocation.getCurrentPosition(showPosition)`, which will callback another function that you'll write shortly, and that we'll call `showPosition`.  This gets the current latitude and longitude of the user, if they grant that permission to the browser.  For clarity, we'll place this geolocation call in another function called `getLocation` and call it from `initMap`.  One note: repl.it doesn't grant location permissions, so this won't work there.  You can take the URL from repl.it's mini browser and open a new browser tab with that URL instead, and grant location permissions there.

```javascript
    function getLocation() {
      // https://www.w3schools.com/html/html5_geolocation.asp 
      if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosition); // callback
      } else {
        //Geolocation is not supported by this browser
      }
    }
    
    function initMap() {
        ...
        getLocation();
    }
```

Finally, let's implement the `showPosition` function, which takes a single parameter representing the user's location.  We'll create a second marker and place it on the map representing the user's current location.  This function goes with the other scripts on the page.  

```javascript
    function showPosition(position) {
      // display your position using a beach flag icon
      // https://developers.google.com/maps/documentation/javascript/markers
      var image = {
        url: 'https://developers.google.com/maps/documentation/javascript/examples/full/images/beachflag.png',
        // This marker is 20 pixels wide by 32 pixels high.
        size: new google.maps.Size(20, 32),
        // The origin for this image is (0, 0).
        origin: new google.maps.Point(0, 0),
        // The anchor for this image is the base of the flagpole at (0, 32).
        anchor: new google.maps.Point(0, 32)
      };

      var currentPosition = {lat: position.coords.latitude, lng: position.coords.longitude};
      var currentLocationMarker = new google.maps.Marker({position: currentPosition, icon: image, map: map});
    }
```

### Setting up a Google Maps API Key

To obtain a Google API key on your account, first go to [https://console.cloud.google.com](https://console.cloud.google.com), and log into your Google account.  Select "Credentials" under the "APIs and Services" menu on the left.

![Google API Key](../images/lab-foodbankmap/googleapiappkey.png)

Select your project from the top (or create a new one if prompted), and click the "Create Credentials" button near the top middle of the page.  Select "API key" to create a new key.

![Google API Credentials](../images/lab-foodbankmap/googlemapcreatecredentials.png)

Fill out the form that appears and you will be given an API key.  Copy this down: it will go into your webpage above at the placeholder `YOUR_API_KEY_HERE`.

Next, click the "Library" menu on the left, and search for the "Maps JavaScript API" service.  Click on it.

![Google API Library of Services](../images/lab-foodbankmap/googleapilibrary.png)

Click "Enable" to add it to your project and key.

![Enabling Maps Service](../images/lab-foodbankmap/googleapienablemaps.png)

Under the Credentials menu on the left, click the "Edit" icon on your key to manage it.  We're going to add "restrictions" to your key so that others cannot use it.  This is especially important if you have enabled billing on your key (which we will not!).

![Managing the Key](../images/lab-foodbankmap/googleapimanagekey.png)

I added an HTTP referrer restriction as shown below.  Specifically, I added my repl.it URL (seen on the repl.it browser page on the right side of your repl.it project), with a `/*` at the end, to show that all URL's under this domain are acceptable.  I added a second variant of the URL for external browser access, which you can see and replicate below.  Now, I can only use this key from my repl.it project web page.

Additionally, I added an API restriction and selected "Google Maps API" so that the key can only be used for calls to the Google Maps API, and not to other Google services.

![Adding Key Restrictions](../images/lab-foodbankmap/googleapirestrictkey.png)

Try it out by copying the repl.it URL into a web browser and allowing location access.  You will get an error that says the map failed to load, and it will display "For development purposes only" as an overlay on the map, if you do not have billing set up for the Google API service.  This is perfectly acceptable, and there is no need to set up any billing accounts!

## Part 3: Plotting Locations
Iterate over the food bank latitude and longitude values obtained by issuing a GET request on your web service, and plot them on the map, using the example provided.

## Part 4: Identifying the Closest Food Bank
Using the [Haversine formula](https://en.wikipedia.org/wiki/Haversine_formula) to compute the distance between two points on a sphere, approximate the distance between your current location and each food bank.  You may use [this example](https://www.movable-type.co.uk/scripts/latlong.html) to compute the distance.  Choose a custom marker image for the nearest one and add it to the map.

You will want to make your json object that you get from your food bank call a global variable, and then call `getPosition()` to get your current location.  The callback from `getPosition` (which is `showPosition`) is where you get the `position` variable that is your current location.  In that function, search your global json array for the closest food bank by computing the distance between each food bank's latitude and longitude, and your current position's latitude and longitude.  Set a custom marker for this position!  For finding the closest location, you can compare each food bank's location to your current position (this was `position.coords.latitude` and `position.coords.longitude` in the `showPosition` function), keeping track of the closest one (with the minimum distance) to drop a custom marker as you go.  You should call `getPosition` during the callback of your food bank web request, so that you have your json with the food bank locations prior to getting your current position.  Put this minimum distance computation loop inside `showPosition`, where you'll learn your current latitutde and longitude for comparison.  You can make variables from your primary function global by removing the `var` tag from them.  For example `map = ...` is global, but `var map = ...` is not.
 
 Finally, add a `div` tag to the webpage, and set its `innerHTML` value to the name, address, and computed distance of that food bank, so that they appear on the browser page.

[^1]: The Google Map code example is adapted from [Google Maps Platform Documentation](https://developers.google.com/maps/documentation/javascript/adding-a-google-map), which is licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0).  Under the terms of this license, the code example here is also licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0), with attribution to the Google Maps Platform and Google.