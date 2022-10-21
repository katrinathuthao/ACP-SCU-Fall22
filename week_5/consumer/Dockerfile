FROM python:3.8.2

RUN pip3 install flask
RUN pip3 install requests
WORKDIR /app

EXPOSE ${CONSUMER_PORT}

CMD python consumer.py

# ENTRYPOINT start login2.html