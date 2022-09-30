#Python container version 3.10.7
FROM python:3.10.7

#using root user
USER root
#to install jupyter and wget
RUN pip3 install jupyter
RUN apt-get update && apt-get install wget

#declare a user
ENV JUPYTER_USER our_user


RUN useradd -ms /bin/bash ${JUPYTER_USER}

USER ${JUPYTER_USER}
WORKDIR /src/
RUN wget https://raw.githubusercontent.com/katrinathuthao/ACP-SCU-Fall22/main/miscellaneous/ThaoNguyen-pandas.ipynb -P /src
RUN wget https://raw.githubusercontent.com/katrinathuthao/ACP-SCU-Fall22/main/miscellaneous/train.csv -P /src

COPY requirements.txt /src/
RUN pip3 install --no-cache-dir -r requirements.txt

EXPOSE 8888

CMD jupyter notebook --ip=0.0.0.0 --port 8888