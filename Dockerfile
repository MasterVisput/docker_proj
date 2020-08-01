FROM python:3.6-slim
MAINTAINER master.visput@gmail.com
COPY . /python-test-api
WORKDIR /python-test-api
RUN pip install --no-cache-dir -r requirements.txt
RUN ["pytest", "-v", "--junitxml=reports/result.xml"]
CMD tail -f /dev/null