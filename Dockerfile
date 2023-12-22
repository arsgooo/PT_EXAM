FROM python:3
WORKDIR /
COPY . .
RUN pip install unittest
EXPOSE 3000
CMD [ "python", "./days_in_month.py" ]