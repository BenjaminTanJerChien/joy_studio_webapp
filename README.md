# Developmental Django server for Joy Studio 

To run server: 
```cmd
python manage.py runserver
```

When changing anything in models.py or upon inital deployment:
```cmd
python manage.py makemigrations 
python manage.py migrate
```

To push to git:
```
git add .
git commit -m "my changes" 
git remote add origin https://github.com/BenjaminTanJerChien/joy_studio_webapp
git push -u origin master
```
To push to Heroku
```
git clone <YOUR HTTPS URL FROM GITHUB>
git add .
git commit -m "<YOUR COMMIT MESSAGE>"
git push origin master
heroku login
heroku git:remote -a joy-studio
git push heroku master
```

Currently deployed to heroku -> [https://joy-studio.herokuapp.com/](https://joy-studio.herokuapp.com/ "herokuapp.com")