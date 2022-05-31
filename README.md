# QuizApp Development using Django Framework

A web application is a computer program that allows you to complete tasks using the internet. It is a software application that uses web technologies and
web browsers to carry out requests and activities. The project quiz app is one of the web applications that users can use to demonstrate their expertise on a
specific topic.\
The goal of this Quiz Application is to give all types of IT users a platform to develop their profile by taking various skill tests. A range of general,
programming-specific, and company-specific competence tests will be available through the web app. A quiz is a set of questions you give visitors to your
website to test their knowledge on a specific topic.\
\
Benefits from taking a Quiz from this project website are as follows:\
1 Rising to a challenge and coming out victorious. And being associated with a renowned personality.\
2 Can share the quiz results on social media platforms for future opportunities.\
3 Taking a quiz and display their result and show the current statistics of your own performance as compared to your colleagues and friends.\
4 Quiz App is the best way to curate the visitors and imbibe a sense of competitiveness in them.

![image](https://user-images.githubusercontent.com/96367746/171114949-03018e34-ce3a-4150-9ed8-370b6cd1bfcd.png)

The web application has home page where user need to login first to take the test. The navigation bar has sign in and signup facilities. After successful login, only authenticate users can attend the test. There is a list of tests on different skills tests, the user can select any of them. A pop-up window will show up with the description of respective skill test with topic, duration of the test, its difficulty level and score to pass the test. After taking the test user can see the results.
Admin login throws you to the Django administration page where admin have three applications named as account, questions and results. Account app contains quizzes, admin can add quiz, its topic, time difficulty level and passing score. Questions app have list of questions and their answer of choices. Results app can show the results of all the user login to the web app and gave the tests.


## Description of tool and technologies used in the project
### _FRONTEND PART_
HTML, CSS, Bootstrap and JavaScript are measure utilized in frontend of the project. They are an important web designer skill and a prerequisite to learn web designing. While HTML is purposely used to feature online web documentation and content, whereas CSS is
favourable to customize this documentation design/style the website content. JavaScript is an associate object-oriented scripting language used to add behaviour using HTML.
### _BACKEND PART_
For the backend part, Django framework written in python programming is employed. Django is a no-cost and open supply frame software. It is a high-level Python net framework that encourages rapid clen, pragmatic style and development. It is created by
experienced developers, and takes care of lot of efforts for web development, thus you will be able to target on writing your app withno need of reinvent the wheel.
### _MIDDLEWARE_
For the Middleware or database, Django uses its in-build SQLite to perform CRUD operations, that is creation of database, Read, Update/modify and delete the data or database.
### _PLATFORM_
Visual Code Studio is the platform where the project is built, deploy, manage and debug. It’s an efficient code editor that provide development operations like debugging, task running, and version control management. It aims to supply simply the tools a developer desire for a fast code-build-debug cycle and leaves additional complicated workflows. It is a free, powerful and lightweight code editor for various operating system
### _HOSTING BROWSER_
The project uses Chrome browser localhost:8000 (127:0.0.1:8000) to test and validate projects working state. With GitHub and Heroku logins, it can deploy to all the user having internet access.

## Features of the project
The following are the QuizApp features:
### 1 Access features of website:
-> User should be logged in to access the List of Quiz or to take test.\
-> For user registration on signup page, user is required to provide their username, first-name, last-name, e-mail address. Also, have to create strong password.\
-> For login page, the authenticated user is going to be needed to enter their username and password only.
### 2 Features of the Quiz web app:
-> All questions are of multiple-choice question.\
-> Each question is displayed just once per user.\
-> Questions are displayed on website randomly for every user.\
-> If the user by-mistake presses refresh or go back to the previous page, the quiz will start again with totally different questions and time.
### 3 Administrative (admin) features:
-> Only admin have access to add quizzes, questions and show results.\
-> Admin has access to modify quiz, questions and answers.
