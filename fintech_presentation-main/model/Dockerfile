FROM python:3.7-slim
COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt
ENV APP_HOME /app
WORKDIR $APP_HOME
EXPOSE 1111
COPY . ./
CMD python app/main.py