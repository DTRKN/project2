FROM python:3.10
COPY requirements.txt /requirements.txt
RUN test -f /requirements.txt && pip install -r requirements.txt
COPY .. /Tasktwo_j
WORKDIR /Tasktwo_j
CMD python main.py