FROM python:3.12-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    git \
    && apt-get clean

# Install Python packages
RUN pip install --upgrade pip && pip install \
    jupyterlab \
    pandas \
    numpy \
    matplotlib \
    seaborn \
    plotly