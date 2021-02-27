# Pull base image
FROM python:3.9

# Python install/upgrade pip
RUN pip install -U pip

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /home/drf/sb

# Install dependencies
COPY Pipfile Pipfile.lock /home/drf/sb/
RUN pip install pipenv && pipenv install --system

# Copy project
COPY . /home/drf/sb/