FROM python:3.11-slim
WORKDIR /root
COPY ./requirements.txt /root
RUN pip install --no-cache-dir --upgrade -r requirements.txt
RUN mkdir crawler
COPY . /root/crawler

CMD ["celery", "-A", "crawler", "worker", "-B", "-l", "debug", "-c", "1"]
