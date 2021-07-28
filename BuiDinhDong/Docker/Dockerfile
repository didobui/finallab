FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y python3-pip
RUN mkdir -p /usr/src/app/ && cd /usr/src/app
EXPOSE 5000
COPY . /usr/src/app/
RUN pip install --no-cache-dir install -r /usr/src/app/requirements.txt
CMD ["python3","/usr/src/app/app.py"]