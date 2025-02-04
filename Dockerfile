FROM python:3.10
RUN mkdir sentiment
WORKDIR sentiment
COPY . .
RUN pip install -r requirements.txt
ENTRYPOINT ["python","-m","pytest","."]
