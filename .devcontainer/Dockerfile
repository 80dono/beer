FROM python:3.12-bookworm

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    git \
    # tini \
    && apt-get clean

# Copy requirements.txt into the image
COPY ../requirements.txt /tmp/requirements.txt

# Install Python packages
RUN pip install --upgrade pip && pip install --no-cache-dir -r /tmp/requirements.txt
