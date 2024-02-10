---
layout: assignment
permalink: /Labs/WeatherUSA
title: "Web and Mobile Development: WeatherUSA Client"


info:
  coursenum: CS471
  githubclassroom:
    clonelink: https://classroom.github.com/a/En0_7Wun
  points: 100
  goals:
    - To invoke a RESTful web service using node.js
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
  - restclient
  
---

In this lab, you will use the [WeatherUSA API](https://www.weatherusa.net/services/weather-api/docs) to access a weather report from a nearby weather station.

## Step 1: Obtaining your FIPS Code
First, we must obtain the latitude and longitude coordinates that correspond to your location.  The `place` Feed Type will allow you to do this.  The query string is a place of your choosing: you can use a town, a zip code, or an airport code.  You can use `19426`, which is the zip code for Collegeville, or any valid query you'd like.  Obtain the `lat` and `long` values from this result.  If you obtain an array as the result, you may choose the coordinates from the first element of the array (or any that you please).

## Step 2: Finding Weather Stations Near You
Use the latitude and longitude to query the `stationlist` Feed Type.  Choose the station from the array with the minimum `distance` field value, and obtain its `station_id` field.

## Step 3: Getting the Current Weather Conditions
Now, use the `obs` Feed Type to obtain the current weather conditions.  You can use the `station_id` that you just obtained as the query parameter here.  Print out at least 4 fields to the console, with appropriate labels so that you can read it.