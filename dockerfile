FROM python:3.11-slim
WORKDIR /app
COPY main.py .
ENTRYPOINT [ "python", "main.py" ]
# build: docker build -t sandbox .
# docker run -it --rm sandbox