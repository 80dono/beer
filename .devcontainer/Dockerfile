FROM python:3.12-bookworm

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    git \
    && apt-get clean

# Install Python packages
RUN pip install --upgrade pip && pip install \
    jupyterlab \
    # jupyter \
    pandas \
    numpy \
    matplotlib \
    seaborn \
    plotly