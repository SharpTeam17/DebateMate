# DebateMate

## About this project
This project was developed as part of the class project for the Software Engineering class at the University of Memphis (COMP 4081) in the Fall 2017 semester.

## Problem Statement
Debate is a pastime enjoyed by many people across the world. The formality of these debates can range from a simple conversation on the internet to a formal, moderated debate 
competition. On the internet, debates are prevalent. The comment sections of news articles, Facebook posts, and even Tweets are commonly transformed into impromptu debates. These media are not designed with debates in mind, so numerous problems can occur when they are used to host debates. The user interface for comment-style sites makes it difficult to trace arguments and rebuttals—the flow of information is not clear. These sites also lack any implicit or explicit agreement that good debate etiquette and structure will be followed.  

Because these media are inappropriate for debate, they are prone to abuse, breaking down into echo chambers, and nonproductive squabbles. This is plainly evident when sites such as news outlets close their comment sections due to issues. When this happens, there is almost always backlash. This shows that there is a strong desire among people to debate, but no good site to provide structure and moderation.  

In order to solve this problem, our team will create a web application, DebateMate, that provides a structured, moderated, and focused venue for online debate. Through the use of clear rules, moderation, and peer feedback systems, users will be able to engage in constructive debates.

## Team Members
The project was organized using SCRUM.
### Product Owner and Team Lead
* Matthew Weihl ([mattweihl](https://github.com/mattweihl/))

### Developers
* Benjamin Brown ([bbrown683](https://github.com/bbrown683))
* Brianna Frye ([bfrye1](https://github.com/bfrye1))
* Austin Nabors ([Triads](https://github.com/Triads))

### Scrum Master
The professor (Dr. James Yu) and TA (Katie Bridson) served as the group's scrum master.


## Setup
This project was originally designed to use a Postgres database hosted on Heroku.

Install all of the python dependencies via pip for Windows:
```
pip install -r requirements.txt
```

For Unix-based operating systems you will need to use the python3-pip package and run it with elevated permissions:
```
sudo pip3 install -r requirements.txt
```

Install the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli). To run a local instance of Heroku on Unix-based operating systems:
```
heroku local web
```

For Windows you must use the following command:
```
heroku local web -f Procfile.windows
```

You must also provide a .env file that resembles the following:

```
DATABASE_NAME='your database name goes here'
DATABASE_USER='your database user goes here'
DATABASE_PASSWORD='your database password goes here'
DATABASE_HOST='your database host goes here'
DATABASE_PORT='your database port goes here'
SECRET_KEY='your secret key goes here'
```
## Project Report
The document "DebateMate-FinalReport.pdf" contains the final report for the project. 
