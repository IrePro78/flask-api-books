FROM python:3.9
WORKDIR /app
COPY requinments.txt requinments.txt
RUN pip install -r requinments.txt
COPY . .
CMD ["python", "-m", "flask", "run", "--host", "0.0.0.0"]
