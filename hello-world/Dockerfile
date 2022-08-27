from debian:latest

RUN apt -y update 
RUN apt -y install python3-dev python3-pip python3-venv libgl1 ffmpeg libsm6 libxext6

RUN pip install tensorflow keras-ocr

RUN mkdir tests

ADD /scripts/hello-world.py /tests
