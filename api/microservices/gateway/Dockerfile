FROM python

RUN mkdir /service
COPY protobufs/ /service/protobufs/
COPY gateway/ /service/gateway/

WORKDIR /service/gateway

RUN pip install -r requirements.txt




EXPOSE 5000
ENTRYPOINT [ "python", "api-gateway.py" ]