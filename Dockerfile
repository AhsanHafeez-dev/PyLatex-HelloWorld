FROM blang/latex

RUN apt-get update   && \
    apt-get install python3-pip
    WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

# Install necessary tools*

CMD ["python", "app.py"]
