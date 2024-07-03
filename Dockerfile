FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN pip install gunicorn 

COPY . .

ENV FLASK_APP=app.py
ENV FLASK_ENV=Division

EXPOSE 5500

CMD [ "sh", "-c", "flask db upgrade head && gunicorn --bind 0.0.0.0:5500 app:app"]