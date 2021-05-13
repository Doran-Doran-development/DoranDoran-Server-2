FROM python:3.7
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
WORKDIR /dorandoran
EXPOSE 8000
ENV DJANGO_SETTINGS_MODULE config.settings.develop
CMD ["gunicorn", "config.asgi:application", "--bind", "0.0.0.0:8000", "-k", "uvicorn.workers.UvicornWorker"]