FROM python:3.9
LABEL author='Label A'

WORKDIR /app

# Environment
RUN apt update
RUN apt install -y bash vim nano postgresql-client  python3-dev libpq-dev
RUN pip install --upgrade pip

# Major pinned python dependencies
RUN pip install --no-cache-dir flake8==3.8.4 uWSGI

# Regular Python dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy our codebase into the container
COPY . .

RUN ./manage.py collectstatic --noinput
RUN ./manage.py makemigrations
RUN ./manage.py migrate
# Ops Parameters
ENV WORKERS=2
ENV PORT=80
ENV PYTHONUNBUFFERED=1

EXPOSE ${PORT}

CMD uwsgi --http :${PORT} --processes ${WORKERS} --static-map /static=/static --module autocompany.wsgi:application
