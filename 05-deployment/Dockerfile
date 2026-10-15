FROM python:3.12-slim
RUN pip install pipenv
WORKDIR /app
COPY ["Pipfile", "Pipfile.lock", "./"]

RUN pipenv install --deploy 

COPY ["predict.py", "model_C=1.0.bin", "./"]
EXPOSE 9696

ENTRYPOINT ["pipenv", "run", "gunicorn", "--bind=0.0.0.0:9696", "predict:app"]
