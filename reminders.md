To run server: 
```cmd
python manage.py runserver
```

When changing anything in models.py or upon inital deployment:
```cmd
python manage.py makemigrations 
python manage.py migrate
```

To push to Heroku
```cmd
heroku login
heroku git:remote -a joy-studio
git push heroku master
```