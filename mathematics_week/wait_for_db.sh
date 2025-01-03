#!/bin/sh

echo "Waiting for the PostgreSQL database to be ready..."

while ! nc -z db 5432; do
  sleep 0.1
done

echo "PostgreSQL is up - executing command"
exec "$@"
