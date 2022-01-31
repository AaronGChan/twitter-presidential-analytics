# Grab the Python slim image
FROM python:3.8-slim

# Install python and pip
COPY requirements.txt ./requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Add our code
COPY . /app
WORKDIR /app
EXPOSE 8501
# Run the image
CMD streamlit run app.py --server.port $PORT