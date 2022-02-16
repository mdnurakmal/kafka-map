FROM python:3.8

COPY /frontend /app/
WORKDIR /app

# Install packages
RUN pip3 install -r requirements.txt


CMD ["sleep", "10", "&&", "python","app.py"]