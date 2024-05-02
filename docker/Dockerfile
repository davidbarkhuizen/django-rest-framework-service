FROM alpine:3.14 as os

ARG OS_PACKAGES="bash curl python3 py3-pip sqlite"

RUN apk update && apk upgrade
RUN apk add ${OS_PACKAGES}

FROM os as intermediate

WORKDIR /server

COPY . /server

RUN . docker/configure_python_venv.sh

FROM intermediate as final

EXPOSE 8000

ENTRYPOINT [ "/server/entrypoint" ]
