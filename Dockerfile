FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app/backend
RUN apt-get update \
    && apt-get -y install curl \
    && apt-get install libgdal-dev -y \
    && apt-get install libjpeg-dev
COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8000
#
# RUN chmod +x entrypoint.sh
# ENTRYPOINT ["sh", "entrypoint.sh"]