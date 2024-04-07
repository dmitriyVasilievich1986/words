#### firstly creating frontend bundle ####
FROM node:18 AS node_18

WORKDIR /app
COPY ./backend /app/backend
COPY ./frontend /app/frontend

RUN npm install -g npm@10
RUN cd /app/frontend && \
    npm install && \
    npm run build


#### then main project ####
FROM python:3.9

WORKDIR /app
COPY --from=node_18 /app/backend /app/backend

ENV DJANGO_SETTINGS_MODULE=words.settings

RUN python -m pip install --upgrade pip
RUN python -m pip install -r /app/backend/requirements.txt

CMD python /app/backend/runserver.py