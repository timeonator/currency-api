# syntax=docker/dockerfile:1

FROM python:3.9.6-buster

WORKDIR /usr/src/app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

#

CMD [ "python", "-m", "flask", "run", "--host=0.0.0.0"]