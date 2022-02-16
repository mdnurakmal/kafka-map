FROM python:3.8

COPY /frontend /app/
WORKDIR /app

# Install packages
RUN pip3 install -r requirements.txt

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]