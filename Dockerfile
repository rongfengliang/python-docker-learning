FROM python:slim-stretch
LABEL AUTHOR="dalongrong"
LABEL EMAIL="1141591465@qq.com"
WORKDIR /app
COPY . /app/
RUN chmod +x /app/main.py
CMD ["/app/main.py" ]