# Dockerfile for Producer 

FROM ubuntu:18.04

RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev

COPY ./dependencies.txt /producer/dependencies.txt

WORKDIR /producer

RUN pip3 install pika && \
    pip3 install -r dependencies.txt

COPY . /producer

ENTRYPOINT [ "python3" ]

CMD [ "producer.py" ]