FROM python:3.13

WORKDIR /app
COPY . /app

RUN pip install -U pip
RUN pip install -r requirements.txt
RUN pip install gunicorn


ENTRYPOINT [ "gunicorn", "-b", "0.0.0.0:10000", "config.wsgi:application" ]