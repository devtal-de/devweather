FROM alpine

# expose web server port
# only http, for ssl use reverse proxy
EXPOSE 80
VOLUME [ "/app/migrations", "/app/config" ]

RUN apk add --no-cache bash git nginx uwsgi uwsgi-python3 python3-dev alpine-sdk postgresql-dev\
	&& pip3 install --upgrade pip


# application folder
ENV APP_DIR /app

# app dir
COPY webapp ${APP_DIR}/webapp
COPY app.ini app.py config.py.example entrypoint.sh manage.py requirements.txt ${APP_DIR}/
COPY nginx.conf /etc/nginx/nginx.conf
RUN chmod 777 -R /run/
WORKDIR ${APP_DIR}

RUN pip3 install -r requirements.txt

# exectute start up script
ENTRYPOINT [ "/bin/bash", "/app/entrypoint.sh"]
