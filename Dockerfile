FROM python3.6-alpine3.7
WORKDIR /project
ADD . /project
RUN pip install flask
CMD ["python3","/project/rhassignment/webserver.py"]
