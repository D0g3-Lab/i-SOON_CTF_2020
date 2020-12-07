FROM python:3

WORKDIR /usr/src/app

COPY app.py ./
COPY requirements.txt ./
COPY source ./
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8822
COPY flag /
CMD su root -c "python3 app.py"