# Python бейнесі негізінде
FROM python:3.12-slim

# Жұмыс каталогын жасау
WORKDIR /app

# Netcat (netcat-openbsd) орнату (wait_for_db.sh үшін қажет)
RUN apt-get update && apt-get install -y netcat-openbsd && rm -rf /var/lib/apt/lists/*

# Тәуелділіктерді орнату
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Жобаның барлық файлдарын көшіру
COPY . /app/

# wait_for_db.sh скриптын көшіріп, атқару құқығын беру
RUN chmod +x /app/wait_for_db.sh

# Статикалық файлдарды жинақтау
RUN python manage.py collectstatic --noinput

# Серверді іске қосу
CMD ["sh", "-c", "./wait_for_db.sh python manage.py runserver 0.0.0.0:8000"]
