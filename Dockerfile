FROM tensorflow/tensorflow
WORKDIR /app

RUN pip install --upgrade pip
COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

RUN pip install opencv-python
RUN apt-get update
RUN apt-get install libxext6 -y
RUN apt-get install libsm6 -y
RUN apt-get install ffmpeg -y

EXPOSE 5001
CMD [ "python", "./app.py" ]
