FROM python:3.10.11-slim-buster

WORKDIR flask_app
COPY . /flask_app

RUN pip install --trusted-host pypi.python.org -r requirements.txt

# to make port 5200 available to users..
EXPOSE 5200
# run WSGI server on port 5200..
CMD ["gunicorn", "-w", "2", "-b", "0.0.0.0:5200" , "app:app"]