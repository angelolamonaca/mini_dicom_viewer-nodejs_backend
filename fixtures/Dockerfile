FROM python:3

COPY wait-for-it.sh /wait-for-it.sh
RUN chmod +x wait-for-it.sh

ADD main.py /

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir graphqlclient && \
    pip install --no-cache-dir pymysql