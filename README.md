# ReviewMe

An open source platform that helps students take advantage of the existing content on the web and provides reviews for their projects. 

<img src="https://i.imgur.com/gqLcZQc.png" width="400" height="300"> <img src="https://i.imgur.com/wNM64yQ.png" width="400" height="300" height="300"> <img src="https://i.imgur.com/38u3Lk6.png" width="400"> <img src="https://i.imgur.com/gPLFOVD.png" width="400" height="300">

#### Various Components : 
- Landing Page
- Projects
- User Registeration System

#### Languages Used : 
- Python
- HTML
- CSS
- Javascript

#### Framkeworks Used : 
- Django
- Django-Storages
- Raven
- PostgresSQL

#### Services Used :
- Mailgun : Mail (Order Confirmation, User Validation, Etc)
- Sentry : Error handnling and managment
- HeapAnalytics : Anaytics

#### Hosted on : 
- Website : Heroku (Hobby dyno at the moment)
- Static Media : AWS-S3

#### Projects available so far :
- Computer Science and Programming
  - [A Wikipedia inspired about you](https://fathomless-mesa-90743.herokuapp.com/content/categories/projects/2/) : HTML
  - [My Faviourite Quote](https://fathomless-mesa-90743.herokuapp.com/content/categories/projects/3/) : HTML, CSS
  - [My Responsive Portfolio](https://fathomless-mesa-90743.herokuapp.com/content/categories/projects/5/) : HTML, CSS, Responsive Design
  - [My Idea Journal](https://fathomless-mesa-90743.herokuapp.com/content/categories/projects/6/) : HTML, CSS, JS
  
## How to Install 

1. Grab a copy of the project : 

```
git clone https://github.com/manibatra/reviewme.git
```
2. Create a virtual environment and install dependencies
```
mkvirtualenv reviewme_env
pip install -r requirements.txt
```
3. Update the database settings in `settings.py`.
4. Update the envrioment variables requiired in `settings.py`.
5. Initialize your database : 
```
python ./manage.py makemigrations
python ./manage.py migrate
```
6. Run the developement server to verify everything is working
```
python ./manage.py runserver
```

