FROM python
WORKDIR /project
ADD . /project
RUN pip install flask
CMD ["python3","/project/rhassignment/webserver.py"]
