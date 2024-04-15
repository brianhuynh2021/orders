#!/bin/bash -x

# Apply database migrations
python manage.py migrate --noinput || exit 1
# install node_modules for tailwind app
python manage.py tailwind install
python manage.py tailwind build
python manage.py collectstatic --noinput

daphne -b 0.0.0.0 -p 8000 order.asgi:application

exec "$@"