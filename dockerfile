# syntax=docker/dockerfile:1

FROM python:3.10.6-buster

WORKDIR /app

COPY src/contact_sam contact_sam

CMD [ "python3", "contact_sam"]