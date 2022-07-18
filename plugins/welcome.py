import os
from pyrogram import Client, filters
from pyrogram.types import Message, User



@Client.on_message(filters.new_chat_members)
async def welcome(bot,message):
	chatid= message.chat.id
	await bot.send_message(text=f"Hyy {message.from_user.mention} Welcome to {message.chat.username} \n 📍 No Promo, No Porn, No Other Abuses \n 📍 Ask Your Movies With Correct Spelling \n 📍 Spammers Stay Away \n 📍 Feel Free To Report Any Errors To Admins using @admin \n\n 🔰 Share & Support Us 🔰",chat_id=chatid)
	
@Client.on_message(filters.left_chat_member)
async def goodbye(bot,message):
	chatid= message.chat.id
	await bot.send_message(text=f"Bye ,  {message.from_user.mention} , Have a Nice Day",chat_id=chatid)
	

