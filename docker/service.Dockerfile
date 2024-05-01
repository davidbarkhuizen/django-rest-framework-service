FROM alpine:3.14 as os

ARG OS_PACKAGES="python3 py3-pip sqlite"

RUN apk update && apk upgrade
RUN apk add ${OS_PACKAGES}

FROM os as intermediate

WORKDIR /server

COPY *.* /server

RUN echo "CAT"
RUN echo "DOG"
RUN echo "$(ls -al)"
RUN echo "$(ls -al /server)"
RUN . docker/build_intermediate.sh
