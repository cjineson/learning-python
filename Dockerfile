FROM alpine:3.7
RUN apk add --update python3
COPY 5_passwordgen.py /main.py
CMD ["python3", "main.py","10"]
