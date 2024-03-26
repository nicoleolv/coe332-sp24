FROM python:3.10.12

RUN mkdir /gene_api
WORKDIR /gene_api
COPY requirements.txt /gene_api/requirements.txt
RUN pip install -r /gene_api/requirements.txt
COPY gene_api.py /gene_api/gene_api.py

CMD ["python3", "/gene_api/gene_api.py"]