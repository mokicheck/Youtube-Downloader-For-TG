from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup
import config

@Client.on_message(Filters.command(["help"]))
async def start(client, message):
	alpha2 = InlineKeyboardMarkup([
		[InlineKeyboardButton("ʀᴇᴘᴏʀᴛ ʙᴜɢs 👾", url="https://t.me/AlphaX_SUPPORT")]
                ])

	help_image = config.HPIC
	await message.reply_photo(help_image,  caption="**💡 English HELP 📃...**\n \n__• Just Send your Youtube video url 🌟__ \n__• And i will give Method list to select your choice 😋__\n \n======================\n \n**💡 Инструкция на RU 📃...**\n \n__• Просто отправьте свой URL-адрес видео c Youtube.__\n__• И я дам список методов, чтобы выбрать нужную вам функцию.__\n\n•••••••••••••••••••••••\n__• 😊 This bot is fully free.__\n`•⚙ Don't pay anyone for Bots like this.`\n\n",reply_markup=alpha2)
