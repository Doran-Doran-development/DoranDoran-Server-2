FROM python:3.8
WORKDIR .
COPY . .
RUN pip install -r requirements.txt
EXPOSE 8000
ENV DJANGO_SETTINGS_MODULE config.settings.deploy
CMD ["gunicorn", "config.asgi:application", "--bind", "127.0.0.1:8000", "-k", "uvicorn.workers.UvicornWorker"]