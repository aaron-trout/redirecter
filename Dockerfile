FROM python:3.5.2-alpine
MAINTAINER Aaron Trout <aaron@trouter.co.uk>

ADD requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

ADD redirecter.py /app/redirecter.py
ENTRYPOINT ["python", "/app/redirecter.py"]
