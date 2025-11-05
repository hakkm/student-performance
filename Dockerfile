# dockerfile
FROM python:3.9-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    git \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# clone repo into /app so `requirements.txt` is present
#RUN git clone --depth 1 https://github.com/hakkm/student-performance .
COPY . /app

# install requirements if present, then make sure streamlit is installed
RUN if [ -f requirements.txt ]; then pip3 install --no-cache-dir -r requirements.txt; fi
RUN pip3 install --no-cache-dir streamlit

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health || exit 1

CMD ["streamlit", "run", "app.py", "--server.port", "8501", "--server.address", "0.0.0.0"]
