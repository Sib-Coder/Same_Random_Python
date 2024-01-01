FROM python:3.9-alpine

RUN pip install requests && pip install pyTelegramBotAPI && pip install beautifulsoup4

WORKDIR /opt/telebot
ENV BOT_TOKEN=""
COPY kateeee_bot.py /opt/telebot

CMD ["python", "kateeee_bot.py"]
