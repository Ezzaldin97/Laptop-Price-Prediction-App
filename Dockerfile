FROM python:3.10.11-slim-buster

WORKDIR /ml_app

COPY . /ml_app

RUN pip install --trusted-host pypi.python.org -r requirements.txt

# to make port 5200 available to users..
EXPOSE 5200

CMD ["python", "run.py"]