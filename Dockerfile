FROM docker.artifactory.openwaygroup.com/python:3.8-slim

WORKDIR /app
ADD srvtest /app/srvtest
ADD requirements.txt /app
RUN pip3 install -r requirements.txt

EXPOSE 4444

CMD ["python3","-u","/app/srvtest/srvtest.py"]
