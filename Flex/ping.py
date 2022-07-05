# -*- coding: utf-8 -*-
from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message

TOKEN = 'Token_Here'

client = Bot(TOKEN,parse_mode="HTML")
dp = Dispatcher(client)
@dp.message_handler()
async def nain(message: Message):
	ct = message.text.lower()
	content = ct.split(" ")
	user_id = str(message.from_user.id)
	user_name = message.from_user['username']
	chat_id = message.chat.id
	if content[0][0] == '/':
		if content[0][1:] == 'ping':
			await client.send_message(chat_id=chat_id, text='PONG!!\nLatency ￫ 259ms\nServer Location ￫ North Virginia\nServer IP ￫ 21.186.142.83')
		elif content[0][1:] == 'pong':
			await client.send_message(chat_id=chat_id, text='PING!!\nLatency ￫ 259ms\nServer Location ￫ North Virginia\nServer IP ￫ 21.186.142.83')


if __name__ == '__main__':
	executor.start_polling(dp, skip_updates=True)
