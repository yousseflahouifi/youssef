## Intro
This is just a django application to execute nmap using celery asynchronously 

## requirements 
you need a redis instance up and running so : 

```
docker run -d --name some-redis -p 6379:6379 redis
```
<br>
navigate to the root of the project and do :

```
celery -A youssef worker -l info <br>
```
<br>
spin up python server :

```
python manage.py runserver 0:8000
```

*note:you can use docker compose*
