FROM python:3.8
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
ENV DATABASE_URL=postgresql://postgres:password@db:5432/mydatabase
CMD ["python", "app.py"]
