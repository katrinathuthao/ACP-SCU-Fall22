FROM python:3.8.2

RUN pip3 install flask

WORKDIR /app
# COPY . /app
# RUN python api.py
# ENV FLASK_APP=api.py
EXPOSE ${API_PORT}
# EXPOSE 80
# CMD ["flask", "run", "--host", "0.0.0.0"]
# CMD ["flask", "run","-host", "${API_HOST}", "-p", ${API_PORT}]
CMD python api.py
#docker run -it -p 5000:5000 -v "$(pwd)/vol_app:/app" api