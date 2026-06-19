FROM python:3.11-slim

WORKDIR /app

# O Debian Slim baixa diretamente os binários pré-compilados (.whl) sem estressar a CPU
RUN pip install --no-cache-dir requests duckdb

COPY main.py .

CMD ["python", "main.py"]
