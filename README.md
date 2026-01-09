# Femme fatale gallery

## Table of contents
- **[General information](https://github.com/TikiTaki322/femme-fatale-gallery#general-information)**
- **[Technologies](https://github.com/TikiTaki322/femme-fatale-gallery#technologies)**
- **[Setup](https://github.com/TikiTaki322/femme-fatale-gallery#setup)**
- **[Overview](https://github.com/TikiTaki322/femme-fatale-gallery#overview)**

## General information
The project was created for exploring Django workflow and mastering the deployment process.
Femme Fatale Gallery is a CRUD web-app that demonstrates articles about famous women from various domains, however it can be used to host any type of content.


## Technologies
#### The technologies used in this project include:
- **Python 3**
- **Django 4.1**
- **SQLite**
- **CSS**
- **HTML**

#### The modules used in this project include:
- django environ
- django debug toolbar
- django simple captcha
- transliterate
- flake8


## Setup
To install this repository, follow these steps:

- Open the terminal to create a new directory:
  - mkdir name_of_project
- Navigate into the newly project directory: 
  - cd name_of_project
- Сreate an environment:
  - python -m venv venv
- Activate the virtual development environment:
  - for Windows: .\venv\Scripts\activate
  - for Unix: source venv/bin/activate 
- Clone the repository: 
  - git clone https://github.com/tikitaki322/femme-fatale-gallery.git
- Navigate into femme-fatale-gallery directory:
  - cd femme-fatale-gallery
- Create a .env file in the project directory with the following variables:
  - SECRET_KEY=<your_secret_key>
  - ALLOWED_HOSTS=127.0.0.1
  - DEBUG=<True_or_False>
  - REQUIRED_CAPTCHA=<True_or_False> (False to add entries/register without entering captcha)
- Install the necessary packages: 
  - pip install -r requirements.txt
- Create the data base:
  - python manage.py migrate
- Create admin profile:
  - python manage.py createsuperuser
- Run the Django development server: 
  - python manage.py runserver
- Access the admin panel in your browser by path:
  - http://127.0.0.1:8000/settings
- Create at least one category
- Go to main page by path:
  - http://127.0.0.1:8000
- Now you are able to add content, enjoy

If you have any difficulties with installation, feel free to contact me.

## Overview
To view the web application, please click on [this link](https://tikitaki322.github.io)
