FROM python:3.7

WORKDIR /flask

COPY . .

RUN pip install -r requirements.txt

CMD ["uwsgi", "--ini", "uwsgi.ini"]
