FROM python:3.9.0a3-alpine3.10

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
EXPOSE 5000:5000
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]