FROM alpine
RUN apk add --update python3 py-pip
RUN pip install xmlrunner
WORKDIR /
COPY . .
EXPOSE 3000
ENTRYPOINT [ "python" ]
CMD ["pawnshop_tests.py"]