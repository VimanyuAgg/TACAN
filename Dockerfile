FROM python:2.7
MAINTAINER Vimanyu Aggarwal <vimanyu1022007@gmail.com>

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 50051
ADD . /usr/src/app
CMD  python greeter_server.py