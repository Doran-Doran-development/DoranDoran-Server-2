FROM python:3.8
WORKDIR .
COPY . .
RUN pip install -r requirements.txt
EXPOSE 8000
ENV DJANGO_SETTINGS_MODULE config.settings.deploy
CMD ["gunicorn", "--bind","0.0.0.0:8000", "dorandoran.config.asgi:application", "-k", "uvicorn.workers.UvicornWorker"]