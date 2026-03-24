FROM python:3.9-slim
WORKDIR /trap
COPY tarpit.py . 
EXPOSE 2222
CMD ["python", "tarpit.py"]