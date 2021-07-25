FROM python:alpine3.7
WORKDIR /app

RUN pip install -r requirements

EXPOSE 5001
CMD [ "python", "./app.py" ]
