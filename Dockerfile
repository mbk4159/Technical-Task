
FROM python:3.9-slim
RUN pip install boto3
WORKDIR /app
COPY main.py /app/main.py
CMD ["python", "main.py"]

