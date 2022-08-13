from bot import bot
from pyromod import listen
from pyrogram import Client, filters

@bot.on_message(filters.private & filters.command("start"))
async def genStr(bt, message):
  
  api = await bot.ask(message.chat.id, "How are you bruh?")
  print(api)
  print(' ')
  print(api.text)
  print(' ')
  print(api.document)
  await message.reply_document(api.document)
  
if __name__ == "__main__":
    bot.run()
