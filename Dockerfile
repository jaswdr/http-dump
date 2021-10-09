FROM python:3

COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

COPY dump.py /tmp/dump.py

CMD ["python3", "/tmp/dump.py", "80"]
