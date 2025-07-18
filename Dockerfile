FROM python:3.11-slim-bookworm
WORKDIR /loan_app_flask

RUN python3 -m pip install --upgrade pip
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt


COPY . .


CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]