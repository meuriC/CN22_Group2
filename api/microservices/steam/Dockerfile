FROM python

RUN mkdir /service
COPY protobufs/ /service/protobufs/
COPY steam/ /service/steam/

WORKDIR /service/steam
RUN pip install -r requirements.txt
RUN python -m grpc_tools.protoc -I ../protobufs --python_out=. --grpc_python_out=. ../protobufs/steam.proto

EXPOSE 50050
ENV FLASK_APP=steam.py
ENTRYPOINT [ "flask", "run", "--host=0.0.0.0"]