FROM python:3.7
COPY requirements.txt .
RUN pip install --default-timeout=100 -r requirements.txt
COPY . .
WORKDIR /dorandoran
EXPOSE 8000
EXPOSE 3306
ENV DJANGO_SETTINGS_MODULE config.settings.deploy
RUN python manage.py makemigrations
RUN python manage.py migrate
CMD ["gunicorn", "config.asgi:application", "--bind", "0.0.0.0:8000", "-k", "uvicorn.workers.UvicornWorker"]
