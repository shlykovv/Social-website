FROM python:3.10.15-slim

WORKDIR /bookmarks

RUN pip install  gunicorn==20.1.0

COPY requirements.txt .

RUN pip install -r requirements.txt --no-cache-dir


COPY . .

CMD ["python", "manage.py", "runserver", "0:8000"]