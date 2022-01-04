# Book-scraper

[![Build Status](https://app.travis-ci.com/skochansky/book-scraper.svg?branch=main)](https://app.travis-ci.com/skochansky/book-scraper)
# Table of contents
* [General info](#general-info)
* [Setup](#setup)
* [Technologies](#technologies)
* [Application view](#application-view)


## General info
A simple scrapping app for books on the ebookpoint biblio platform.  <br/>
The application takes the pages of the book then combine them together into a PDF and makes it available for download. <br/>
This makes it extremely easy to read books on different hardware, instead of downloading several app you can use single pdf file.



## Setup
To run this project use the following command:
```
$ docker-compose up
```
<b>The application is available at 127.0.0.1:5000</b> <br/><br/>
You can find the data you need to scrape the images that will be linked in the PDF on the ebook point page.<br/> Here is a short instruction. 
<br/> 
1. Log in to your account on the platform.
2. Borrow the book you want in PDF version and then open it. 
3. Go to network, then click on the book URL. 
4. Copy the URL into the Book URL field in the application. 
5. Then copy our Cookie and Referer from the same place to those fields in the app. 
6. Enter the number of pages of the book you want to download in Number of Pages field.

## Technologies
<details>
    <summary>Click here to see the technologies used!</summary>
        <ul>
	    <li>Python 3.8</li>
        <li>Pytest</li>
		<li>Flask</li>
		<li>WTForms</li>
		<li>HTML</li>
		<li>CSS</li>
		<li>Bootstrap 4 </li>
		<li>Jinja</li>
		<li>Docker</li>
		<li>docker-compose</li>
		<li>Travis CI</li>
		<li>PyTest </li>
        </ul>
</details>

## Application view
![flask_app_view](https://user-images.githubusercontent.com/48139558/148096905-9d5bb8e3-5e33-4364-957d-d534724f9078.png)

