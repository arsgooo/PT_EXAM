FROM python:3
WORKDIR /
COPY . .
EXPOSE 3000
CMD [ "python", "./days_in_month.py" ]