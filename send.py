import os
import telebot
import schedule
import time
from openai import OpenAI

AI_TEXT_MODEL = 'chatgpt-4o-latest'
BOT_TOKEN_NAME = "ATHE_BOT_TOKEN"
BOT_TOKEN = os.environ.get(BOT_TOKEN_NAME)
# CHAT_ID = -1002374309134
CHAT_ID = '@conscious_mother_the'

def job(CHAT_ID=CHAT_ID):
    client = OpenAI()
    text = client.chat.completions.create(
        model=AI_TEXT_MODEL,
        messages=[
            { "role": "developer", "content": f"Ты - осознанная мать, ты много раз ошибалась в воспитании детей, но теперь хочешь восстановить хорошие отношения" },
            { "role": "user", "content": f"Пожелай хорошего дня дочери, используй смайлики" },
        ]
    ).choices[0].message.content
    bot = telebot.TeleBot(BOT_TOKEN)
    bot.send_message(chat_id=CHAT_ID, text=text, parse_mode="Markdown")

if __name__ == '__main__':
    schedule.every().day.at("07:00",'Europe/Moscow').do(job)

    fifteen_minutes = 15 * 60

    for i in range(fifteen_minutes):
        schedule.run_pending()
        time.sleep(1)
