FROM python:3.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt

COPY . /code/

CMD ["python", "manage.py makemigrations --noinput"]
CMD ["python", "manage.py migrate --run-syncdb"]

CMD ["python", "populate_moviegeek.py"]
CMD ["python", "populate_ratings.py"]
