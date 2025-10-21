# Python version
FROM python:3.12

# Set working directory
WORKDIR /app

# Copy requirements first (cache layer)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --upgrade pip \
 && pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Start the bot
CMD ["python", "-m", "Moco"]
