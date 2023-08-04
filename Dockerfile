FROM python:3.11.0
WORKDIR /app
COPY . .
RUN pip install flask
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
