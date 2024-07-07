FROM python:3.8

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

# Install postgresql-client and populate test database
RUN apt-get update
RUN apt-get install -y postgresql-client
RUN psql -h database -U postgres -d splitfy -a -f populate_test_db.sql

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0"]