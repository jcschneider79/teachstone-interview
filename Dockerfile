FROM ubuntu:22.04

RUN apt update && apt upgrade -y
RUN apt install python3 -y
RUN apt install ca-certificates -y
RUN useradd mytest

WORKDIR /usr/local/bin/

COPY report-generator.py ./report-generator
RUN chown mytest report-generator
RUN chmod 755 report-generator

# make it look exactly like the example provided:
RUN mkdir /app
WORKDIR /app
CMD sleep inf
