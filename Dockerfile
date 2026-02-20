# Python tasvirini tanlash
FROM python:3.8-slim

# Virtual muhit yaratish
RUN python -m venv /env

# Virtual muhitni faollashtirish
ENV PATH="/env/bin:$PATH"

# PIP-ni yangilash
RUN pip install --upgrade pip

# Kutubxonalarni o'rnatish
COPY requirements.txt .
RUN pip install -r requirements.txt

# Kodni nusxalash
COPY . /app
WORKDIR /app

# Botni ishga tushurish
CMD ["python", "bot.py"]
