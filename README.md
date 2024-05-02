# readme

## to build and test on the host machine

    $ . docker/configure_python_venv.sh
    $ ./test

## to build and run on the host machine

    $ . docker/configure_python_venv.sh
    $ ./runserver

## to build and run docker image on the host

!! assumes that port 8000 is available on the host machine for docker to bind to

    $ ./docker_build
    $ ./docker_run