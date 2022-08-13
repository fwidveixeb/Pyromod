from bot import bot
from pyromod import listen
from pyrogram import Client, filters

@bot.on_message(filters.private & filters.command("start"))
async def genStr(bt, msg):
  
  api = await bot.ask(msg.chat.id, "How are you bruh?")
  await message.reply_document(api.document)
  
if __name__ == "__main__":
    bot.run()
