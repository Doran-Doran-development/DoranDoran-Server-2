FROM python:3.8
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
WORKDIR /code/dorandoran
EXPOSE 8000
ENV DJANGO_SETTINGS_MODULE config.settings.develop
CMD ["gunicorn", "config.asgi:application", "--bind", "0.0.0.0:8000", "-k", "uvicorn.workers.UvicornWorker"]