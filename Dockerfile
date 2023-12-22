FROM python:3
RUN pip install flask
RUN pip install flask_restful
WORKDIR /
COPY . .
EXPOSE 3000
CMD [ "python", "./days_in_month.py" ]