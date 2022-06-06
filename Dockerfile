FROM alpine:latest
ENV DESTDIR /usr/local/bin/

RUN apk add --no-cache python3 py3-requests
COPY cibot.py ${DESTDIR}
WORKDIR ${DESTDIR}

CMD ["/usr/bin/python3", "-u", "cibot.py"]
