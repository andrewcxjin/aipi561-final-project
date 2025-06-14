FROM python:3.11
WORKDIR /app
COPY . .

# Download model inside container
RUN mkdir -p models && \
    curl -L -o models/mistral-7b.Q4_K_M.gguf https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.1-GGUF/resolve/main/mistral-7b.Q4_K_M.gguf

RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "app.py"]
