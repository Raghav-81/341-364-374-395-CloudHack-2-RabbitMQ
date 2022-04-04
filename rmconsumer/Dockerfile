# Dockerfile for rmconsumer
FROM ubuntu:18.04

RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev

COPY ./dependencies.txt /rmconsumer/dependencies.txt

WORKDIR /rmconsumer

RUN pip3 install pika && \
    pip3 install -r dependencies.txt

COPY . /rmconsumer

ENTRYPOINT [ "python3" ]

CMD [ "ride_matching_consumer.py" ]