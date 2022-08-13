from bot import bot
from pyromod import listen
from pyrogram import Client, filters

@bot.on_message(filters.private & filters.command("start"))
async def genStr(bt, message):
  
  one = await bot.ask(message.chat.id, "How are you bruh?")
  await message.reply_cached_media(one.document.file_id)
  
  two = await bot.ask(message.chat.id, "How are you bruh?")
  await message.reply_cached_media(two.document.file_id)
  
if __name__ == "__main__":
    bot.run()
