FROM python:3.10

# Create and Change Dir
WORKDIR /code

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
COPY serve /code/

ENV PATH=/code:$PATH

EXPOSE 8080

ENTRYPOINT ["serve"]

# ENTRYPOINT ["python", "app.py", "--host", "0.0.0.0", "--port", "8080"]
CMD ["serve"]