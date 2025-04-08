FROM python:3.9-slim
WORKDIR /app
COPY . /app
EXPOSE 1234
RUN pip install Flask
CMD [ "python", "app.py" ]