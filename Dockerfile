FROM python:3.12-slim

WORKDIR /lms

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV SECRET_KEY='django-insecure-2_c8_%4#o&5z0xlg3-=*en#!h)s0h9w-@&@)z-#wcf^21ii5%s'
ENV CELERY_BROKER_URL="redis://127.0.0.1:6379/0"
ENV CELERY_BACKEND="redis://127.0.0.1:6379/0"

RUN mkdir -p /lms/media

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "127.0.0.1:8000"]