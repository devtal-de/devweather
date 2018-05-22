#!/bin/bash
set -e


if [ -z "$@" ]; then

    if [ ! -f /app/config/config.py ]; then
        cp /app/config.py.example /app/config/config.py
    fi

    # if /app/migrations is empty init database
    if [ ! -f /app/migrations/README ]; then
        python3 manage.py db init -d /tmp/migrations 2> /dev/null
        mv /tmp/migrations/* /app/migrations
    fi


    python3 manage.py db migrate
    python3 manage.py db upgrade


    #if app is mounted, Dockerfile is available
    if [ -f Dockerfile ]; then
        echo "Running app in debug mode!"
        python3 app.py
    else
        echo "Running app in production mode!"
        nginx && uwsgi --ini /app/app.ini
    fi
fi

exec "$@"
