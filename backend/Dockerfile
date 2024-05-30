FROM python:3.11-slim
WORKDIR /root
ENV PYTHONUNBUFFERED=1
COPY ./requirements.txt /root
RUN pip install --no-cache-dir --upgrade -r requirements.txt
RUN mkdir backend
COPY . /root/backend
EXPOSE 8000

CMD ["sh", "backend/run.sh"]