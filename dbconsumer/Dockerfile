# Dockerfile for database consumer
FROM ubuntu:18.04

RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev

COPY ./dependencies.txt /dbconsumer/dependencies.txt

WORKDIR /dbconsumer

RUN pip3 install pika && \
    pip3 install -r dependencies.txt

COPY . /dbconsumer

ENTRYPOINT [ "python3" ]

CMD [ "database_consumer.py" ]