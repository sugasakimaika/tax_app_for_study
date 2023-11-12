FROM python:3.7.5-slim

WORKDIR /work

ADD Womanmoneycareer Womanmoneycareer
ADD tests tests
ADD setup.py setup.py
ADD MANIFEST.in MANIFEST.in

RUN pip install --upgrade pip \
  && pip install -r requirements.txt \
  && pip install pytest

CMD bash