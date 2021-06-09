FROM ubuntu:18.04
RUN apt-get update -y
RUN apt-get install -y apt-utils
RUN apt-get upgrade -y
RUN apt-get install -y python3 python3-pip python3.6-dev build-essential net-tools
RUN pip3 install --upgrade pip
RUN mkdir /app\
    && mkdir -p /app/abstract_client\
    && mkdir -p /app/endpoint_client\
    && mkdir -p /app/tests

COPY abstract_client /app/abstract_client
COPY endpoint_client /app/endpoint_client
COPY tests /app/tests
COPY settings.py /app
COPY requirements.txt /app
WORKDIR /app
ENV PYTHONPATH=/app
RUN pip3 install -r requirements.txt
ENTRYPOINT ["/usr/bin/python3", "-m" ,"pytest" ,"/app/tests"]
