import os
import telebot
import schedule
import time
from openai import OpenAI

#AI_TEXT_MODEL = 'chatgpt-4o-latest'
AI_TEXT_MODEL = 'gpt-4o-mini'
BOT_TOKEN_NAME = "ATHE_BOT_TOKEN"
BOT_TOKEN = os.environ.get(BOT_TOKEN_NAME)
# CHAT_ID = -1002374309134
CHAT_ID = '@conscious_parent_the'

def job(parent, child):
    client = OpenAI()
    text = client.chat.completions.create(
        model=AI_TEXT_MODEL,
        messages=[
            { "role": "developer", "content": parent },
            { "role": "user", "content": child },
        ]
    ).choices[0].message.content
    bot = telebot.TeleBot(BOT_TOKEN)
    bot.send_message(chat_id=CHAT_ID, text=text, parse_mode="Markdown")

mother = f"Ты - осознанная мать, ты много раз ошибалась в воспитании детей, но теперь хочешь восстановить хорошие отношения"
#father = f"Ты - осознанный отец, ты много раз ошибался в воспитании детей, но теперь хочешь восстановить хорошие отношения"
daughter = f"Пожелай хорошего дня дочери, используй смайлики"
#son = f"Пожелай хорошего дня сыну, используй смайлики"

#job(mother, daughter)
#job(father, daughter)
#job(mother, son)
#job(father, son)

schedule.every().day.at("07:00",'Europe/Moscow').do(job, parent=mother, child=daughter)

fifteen_minutes = 15 * 60

for i in range(fifteen_minutes):
    schedule.run_pending()
    time.sleep(1)
