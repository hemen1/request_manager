# Use the official Python image as the base image
FROM python:3.11

# Set environment variables for Python
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Create and set the working directory
RUN mkdir /code
WORKDIR /code

# Copy the requirements file into the container and install dependencies
COPY requirements.txt /code/
RUN pip install -r requirements.txt

# Copy the Django project files into the container
COPY . /code/

# Run database migrations and collect static files
#RUN python manage.py makemigrations
#RUN python manage.py migrate

#RUN echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin','','admin')" | python manage.py shell