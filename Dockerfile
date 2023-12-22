FROM alpine
RUN apk add --update python3 py-pip
RUN pip install xmlrunner
WORKDIR /
COPY . .
ENTRYPOINT [ "python" ]
CMD ["pawnshop_tests.py"]