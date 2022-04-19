FROM python

RUN mkdir /service
COPY ./ /service/gateway/

WORKDIR /service/gateway
RUN pip install -r requirements.txt

EXPOSE 50000
ENTRYPOINT [ "python", "api-gateway.py"]