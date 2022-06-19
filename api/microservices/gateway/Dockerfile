FROM python

RUN mkdir /service
COPY api/microservices/protobufs/ /service/protobufs/
COPY api/microservices/gateway/ /service/gateway/

WORKDIR /service/gateway

RUN pip install -r requirements.txt

EXPOSE 5000
ENTRYPOINT [ "python", "api-gateway.py" ]
