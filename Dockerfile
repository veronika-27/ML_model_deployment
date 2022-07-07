FROM python:3.9

COPY requirements.txt requirements.txt
COPY main.py main.py
COPY fruit_rec.pt fruit_rec.pt

RUN mkdir -p /input_folder/uploads
RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
