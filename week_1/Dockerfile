
#FROM python:latest to get the latest version of Python

#to get specific version of Python
FROM python:latest

RUN apt-get update

#installing wget Linux command
RUN apt-get install wget 

RUN wget https://raw.githubusercontent.com/mschermann/forensic_accounting/master/fb_sub.csv
# RUN awk -F ',' '$3 ~ /\w+(?=\s+INC)/ {print $3}'  fb_sub.csv > company.txt
RUN awk -F ',' '$3 ~ /[\s\S]*INC$/ {print $3; exit}'  fb_sub.csv > company.txt

