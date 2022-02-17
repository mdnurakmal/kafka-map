FROM python:3.8

COPY /stream2 /app/
WORKDIR /app

# Install packages
RUN pip3 install -r requirements.txt
# ENTRYPOINT ["python3", "app.py"]
CMD [ "python3", "-u", "./busdata1.py"]