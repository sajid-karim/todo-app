FROM python:3.11.5

WORKDIR /app
COPY . /app

# We need libpq-dev & gcc for building psycopg (for Postgresql).
RUN apt-get update && apt-get install libpq-dev gcc -y \
  && pip install -r requirements.txt

#Name of the service that the logger.py uses to display the service name from os package.
ENV SERVICE_NAME="todo-app"

COPY scripts/entrypoint.sh /app
RUN chmod +x /app/entrypoint.sh

EXPOSE 8000

ENTRYPOINT ["/app/entrypoint.sh"]
