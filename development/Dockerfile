FROM python:3.7

WORKDIR /flask

ENV FLASK_APP=app.py
ENV FLASK_ENV=development
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5010

COPY . .

RUN pip install -r requirements.txt

CMD ["flask", "run"]
