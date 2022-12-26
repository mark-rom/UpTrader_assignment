FROM python:3.10-slim

WORKDIR /app
COPY ../requirements.txt /app


RUN pip3 install -r requirements.txt --no-cache-dir
RUN pip3 install gunicorn

COPY ./src/ /app/

RUN python3 manage.py collectstatic


CMD ["gunicorn", "menu_template.wsgi:application", "--bind", "0:8000" ]