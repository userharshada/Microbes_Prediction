FROM continuumio/anaconda3:latest

WORKDIR /app
COPY . /app
RUN apt-get update && apt-get install -y python3 python3-pip
RUN pip install -r requirements.txt
RUN pip install joblib
EXPOSE 8080  
CMD gunicorn --workers=4 --bind 0.0.0.0:8080 app:app 
