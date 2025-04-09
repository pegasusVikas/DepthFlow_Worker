FROM ghcr.io/brokensource/broken-base:0.9.0.dev0-cpu
LABEL org.opencontainers.image.title="DepthFlow"
WORKDIR /App
RUN uv pip install python-dotenv google-cloud-storage google-cloud-run
COPY assets.py depthflow.py invoke_job.py .env ./
COPY /access_keys ./access_keys
CMD ["python", "depthflow.py"]