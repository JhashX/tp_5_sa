FROM python:3.8-slim-buster

WORKDIR /usr/src/app

COPY  requirements.txt requirements.txt

RUN ls -lh
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "./app.py", "run"]
