FROM ubuntu:20.04

RUN apt-get -y update
RUN DEBIAN_FRONTEND="noninteractive" TZ="Europe/London" apt-get -y install software-properties-common poppler-utils tesseract-ocr wget
RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt-get -y install python3.10 python3-opencv python3-pip python3.10-distutils
RUN wget https://bootstrap.pypa.io/get-pip.py
RUN python3.10 get-pip.py

COPY requirements.txt /app/requirements.txt
RUN python3.10 -m pip install -r /app/requirements.txt

ADD . /app
WORKDIR /app

ENTRYPOINT ["python3.10", "main.py"]