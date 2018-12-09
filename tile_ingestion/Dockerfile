FROM python:3.7
RUN mkdir -p /app
WORKDIR /app
COPY . /app
RUN pip install --trusted-host pypi.python.org -r requirements.txt
ENTRYPOINT python unzip.py