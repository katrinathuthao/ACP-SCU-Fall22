FROM python

#/tmp/ folder = temp folder
COPY requirements.txt /tmp/ 

RUN pip3 install -r /tmp/requirements.txt

VOLUME /vol_app
WORKDIR /app

EXPOSE 8000
#@ this pt, must run in interactive mode
#-it = i want the docker run in interactive mode and also give a terminal
#docker run -it -p 8000:8000-v "$(pwd)/vol_app:/app" my_django /bin/bash

#python /app/app/manage.py runserver 0.0.0.0:8000
#python /app/app/manage.py createsuperuser

#go to app/settings.py > DATABASES
#NAME: web
#USER: root
#PSSWORD: pass
#HOST: mydb
#PORT: 5432

#docker run -it -p 8000:8000 --network mynetwork -v "$(pwd)/app:/app" my_django /bin/bash


