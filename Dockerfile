FROM joshkaiju/gophernicus:v1
RUN apk add python3 py3-pip
RUN pip install requests
