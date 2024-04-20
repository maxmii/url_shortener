FROM python:3.11.9-slim

RUN mkdir /code
WORKDIR /code
RUN pip install --upgrade pip
COPY requirements.txt /code/

RUN pip install gunicorn

RUN pip install -r requirements.txt
COPY src/urlshortener /code/

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]