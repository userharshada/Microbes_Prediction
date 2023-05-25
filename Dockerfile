FROM continuumio/anaconda3:latest
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
RUN pip install joblib
EXPOSE $PORT
CMD gunicorn --workers=4 --bind 0.0.0.0:$PORT app:app