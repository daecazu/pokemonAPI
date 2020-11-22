FROM nginxinc/nginx-unprivileged:1-alpine

COPY ./base/compose/production/nginx/default.conf /etc/nginx/conf.d/default.conf
COPY ./base/compose/production/nginx/uwsgi_params /etc/nginx/uwsgi_params

USER root

RUN mkdir -p /vol/static
RUN chmod 755 /vol/static

USER nginx

