FROM python:3.12
# instalez dependinte
RUN apt-get update && apt-get install build-essential graphviz graphviz-dev -y
# Instalează clientul psql
RUN apt-get install -y postgresql-client
# Copiez tot conținutul directorului curent în container
COPY . /moonlight_relax
WORKDIR /moonlight_relax
RUN pip3 install -r requirements.txt
COPY wait-for-db.sh /usr/wait-for-db.sh
RUN chmod +x /usr/wait-for-db.sh
# Colectează fișierele statice
RUN python manage.py collectstatic --noinput
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

