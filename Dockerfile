FROM node:14 AS node_14

WORKDIR /app
COPY ./backend /app/backend
COPY ./frontend /app/frontend

RUN npm install -g npm
RUN bash /app/frontend/run_build.sh

FROM python:3.9

WORKDIR /app
COPY --from=node_14 /app/backend /app/backend

RUN ls -la /app
RUN python -m pip install --upgrade pip
RUN python -m pip install -r /app/backend/requirements.txt

CMD python /app/backend/runserver.py