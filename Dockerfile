FROM python:3.8-slim-buster

# Added by JJK
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Added by JJK - use Python3
RUN apt-get update && apt-get install -y python3 python3-pip
# RUN /usr/bin/pip3 install flask

# Install dependencies:
COPY requirements.txt .
RUN pip3 install -r requirements.txt

EXPOSE 3001

COPY master_assistant.py .

# Run the application:
CMD python3 master_assistant.py
