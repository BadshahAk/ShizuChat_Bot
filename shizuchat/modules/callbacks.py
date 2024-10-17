from pyrogram import filters
from pyrogram.types import CallbackQuery

from shizuchat import shizuchat
from shizuchat.modules.helpers.button import gen_key
from shizuchat.modules.Gen import gen_session


@shizuchat.on_callback_query(
    filters.regex(pattern=r"^(gensession|pyrogram|pyrogram1|telethon)$")
)
async def cb_choose(_, cq: CallbackQuery):
    await cq.answer()
    query = cq.matches[0].group(1)
    if query == "gensession":
        return await cq.message.reply_text(
            text="<b>» ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴜᴛᴛᴏɴs ʙᴇʟᴏᴡ ғᴏʀ ɢᴇɴᴇʀᴀᴛɪɴɢ ʏᴏᴜʀ sᴇssɪᴏɴ :</b>",
            reply_markup=gen_key,
        )
    elif query.startswith("pyrogram") or query.startswith("telethon"):
        try:
            if query == "pyrogram":
                await gen_session(cq.message, cq.from_user.id)
            elif query == "pyrogram1":
                await gen_session(cq.message, cq.from_user.id, old_pyro=True)
            elif query == "telethon":
                await gen_session(cq.message, cq.from_user.id, telethon=True)
        except Exception as e:
            await cq.edit_message_text(e, disable_web_page_preview=True)