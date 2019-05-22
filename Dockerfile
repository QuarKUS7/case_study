FROM python:alpine

EXPOSE 80

# Install gunicorn
RUN pip install gunicorn

# Install falcon
RUN pip install falcon

# Add demo app
WORKDIR /app

COPY . /app

CMD ["gunicorn", "-b", "0.0.0.0:8000", "app:app"]