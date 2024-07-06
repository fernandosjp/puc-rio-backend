FROM python:3.8

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

# Install SQLite
RUN apt-get update
RUN apt-get install -y sqlite3
RUN mkdir database
RUN sqlite3 database/db.sqlite3 < populate_test_db.sql

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0"]