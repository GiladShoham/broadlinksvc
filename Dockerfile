FROM ubuntu:18.04

LABEL maintainer="tomer.klein@gmail.com"

#install pip3
RUN apt update

RUN apt install python3-pip --yes

RUN  pip3 install flask flask_restful cryptography==2.6.1 broadlink

#Create working directory
RUN mkdir /opt/broadlinksvc

EXPOSE 7020

COPY broadlinksvc /opt/

ENTRYPOINT ["/usr/bin/python3", "/opt/broadlinksvc/broadlinksvc.py"]
