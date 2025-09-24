FROM python:3.10-slim

RUN pip install --no-cache-dir scikit-learn numpy

WORKDIR /app

COPY linear_regression.py .

CMD ["python", "linear_regression.py"]