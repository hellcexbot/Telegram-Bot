from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("🖥 Developer ", url="https://t.me/intiqam")],
        [InlineKeyboardButton(
            "Kanalımız 📣", url="https://t.me/AzeBots")]
    ])
    welcomed = f"Salam🤚🏻<b>{message.from_user.first_name}</b>\n/🤖 Bu Bot ilə siz YouTube videolarını səs faylı kimi yükləyə və getdiyiniz hər yerə apara bilərsiniz."
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
