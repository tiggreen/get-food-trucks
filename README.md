get-food-trucks
===============

A web app that shows what types of food trucks might be found near a specific location on a map.

Link to the webpage is http://get-food-trucks.herokuapp.com/
Try this address as an input: 1219 7th Ave San Francisco, CA

Some observations:

I know you guys mentioned that the good engineering is to use the right tool for the right job.I think I pretty much followed that concept in this project which made it super simple in terms of the # of code lines I wrote but not the hours I spent on this because a lot of cool stuff was new to me.

How was it so simple?

Mapbox (https://www.mapbox.com/) is my hero here and I have to admit it. It basically did most of the job for me. I exported the trucks dataset from DataSF as a .cvs and imported into my Mapbox project. It used tracks' lat/lngs-s to find the exact location of trucks and mapped them on the map. This basically gave me a map whith bunch of trucks on it. It was awesome! 

Next, what I needed to do is to connect this map with my web app. So I did. I created a small Python web app which takes the location string from the user, forward geocodes it using Mapbox's API and shows the location bound on the map. This allows user to see all the found trucks nearby and click on small truck icons to learn more about their types.  

Next, I hosted on Heroku. Didn't know how awesome and easy could Heroku be.
Super excited that I learned about them. Going to use Heroku for my next projects for sure. 


Code is hosted on Github here - 
https://github.com/tiggreen/get-food-trucks


Being said, 

1. The project I chose.
I chose food trucks project.

2.The technical track you chose (full stack, back-end or front-end)
The technical track I guess is more back-end. 

3.Reasoning behind your technical choices (and level of experience with those)
I used Python. Python is currently my primary language (do homework and interviews) but I never done any web stuff with it. I chose Flask web framework (turned out to be awesome for small projects like this). I was completely novice in Flask.

Mapbox API (never used Mapbox before) created the map with trucks data and geocoded the user input location. Was novice in their API too.

Hosted on Heroku. Never used it before but after first try I just loved it.

Do you ask why Python? Because it's sexy! 

4.Trade-offs you might have made, anything you left out, or what you might do differently if you were to spend additional time on the project?

Well my map is static in the first place. You don't want to import a new data every single time once a new truck is added. Do you? So instead of importing the map I could use the DataSF API.

Flask is not a MVC framework it's a microframework. So this makes this project not really scalable right? MVC is pretty awesome keeping things separate and simple even when your project is growing fast. I was more focused on getting this project done.

Not sure how accurate Mapbox's forward geocoder is. We could possible use third party geocoder to have better results. E.g. Foursquare's twofishes is pretty good. I worked on it. 


5. Link to other code you're particularly proud of.
Check out my startup at https://Wheelie.me. It's php that's why I didn't send you the source code guys. 
Take a look some python code I have on my github profile as well. 

6.Link to your resume or public profile.
Here I am - http://www.tiggreen.me/ (scroll down when you open the website).
If you have time you could read what I write about :)

Thank you!!
Tigran


[![Bitdeli Badge](https://d2weczhvl823v0.cloudfront.net/tiggreen/get-food-trucks/trend.png)](https://bitdeli.com/free "Bitdeli Badge")

