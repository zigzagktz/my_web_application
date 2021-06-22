FROM python:3.8.6

WORKDIR /app

COPY . .

RUN apt-get -y update
RUN pip3 install -r requirements.txt

#CMD ["python","run.py"]
CMD ["gunicorn","--bind","0.0.0.0:5000","run:app"]