from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

class Script(object):

    START_TEXT = """
<b>Hey</b><b> {} </b>

<b>I am Telegram Most Powerful Url Uploader Bot</b>

<b>I can Upload Any Link in File or Video</b>

<b>Use Help Command to Know How to Use me</b>

<b>Made With 💕 By</b><b> @Tellybots_4u</b>
"""
    HELP_TEXT = """
<b>Link to Media or File</b>
➠ <b>Send a link for upload to telegram file or media.</b>

<b>Set Thumbnail</b>
➠ <b>Send a photo to make it as permanent thumbnail.</b>

<b>Deleting Thumbnail</b>
➠ Send /delthumb to delete thumbnail.</b>

<b>Show Thumbnail</b>
➠ Send /showthumb to view custom thumbnail.</b>

<b>Made With 💕 By</b><b> @Tellybots_4u</b>
"""
    ABOUT_TEXT = """
 **🤖 <b>Bot :** URL Uploader</b>\n
 **👲 <b>Developer :** [Tellybots_4u](https://telegram.me/tellybots_4u)</b>\n
 **👥 <b>Channel :** [Tellybots_4u](https://telegram.me/tellybots_4u)</b>\n
 **❄️ <b>Credits :** Everyone in this journey</b>\n
 **🍴 <b>Source :** [Click here](https://t.me/tellybots_digital)</b>\n
 **📝 <b>Language :** [Python3](https://python.org)</b>\n
 **📚 <b>Library :** [Pyrogram v1.2.0](https://pyrogram.org)</b>\n
 **🌟 <b>Server :** [Heroku](https://heroku.com)</b>\n
"""
    START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🤖 Update Channel', url='https://telegram.me/tellybots_4u'),
        InlineKeyboardButton('💬 Support Group', url='https://telegram.me/tellybots_support')
        ],[
        InlineKeyboardButton('❔ Help', callback_data='help'),
        InlineKeyboardButton('⛔ Close', callback_data='close')
        ]]
    )
    HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🏡 Home', callback_data='home'),
        InlineKeyboardButton('👲 About', callback_data='about'),
        InlineKeyboardButton('⛔ Close', callback_data='close')
        ]]
    )
    ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🏡 Home', callback_data='home'),
        InlineKeyboardButton('❔ Help', callback_data='help'),
        InlineKeyboardButton('⛔ Close', callback_data='close')
        ]]
    )
    FORMAT_SELECTION = """<b>Select The Desired Format For Uploading In File or Video</b>"""
    CHECKING_LINK = "<code>Analysing Your Link</code>⏳"
    BANNED_USER_TEXT = "<code>You are Banned!</code>"
    SET_CUSTOM_USERNAME_PASSWORD = """"""
    DOWNLOAD_START = "<code>Downloading To My server Please Wait...</code>"    
    UPLOAD_START = "<code>Uploading into Telegram...</code>"
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = "Downloaded in {} seconds. \n\nUploaded in {} seconds."
    RCHD_TG_API_LIMIT = "Downloaded in {} seconds.\nDetected File Size: {}\nSorry. But, I cannot upload files greater than 1.95GB due to Telegram API limitations."
    CUSTOM_CAPTION_UL_FILE = "<b>Join :-</b> @Tellybots_4u"
    SLOW_URL_DECED = "Gosh that seems to be a very slow URL. Since you were screwing my home, I am in no mood to download this file. Meanwhile, why don't you try this:==> https://shrtz.me/PtsVnf6 and get me a fast URL so that I can upload to Telegram, without me slowing down for other users."
    NO_VOID_FORMAT_FOUND = "<code>{}</code>"
    REPORT_SITE_TEXT = "<code>Sorry not uploading in this site here because this site is reporting site.</code>"
    SOMETHING_WRONG = "<code>Something Wrong. Try again.</code>"
    FORCE_SUBSCRIBE_TEXT = "<code>Please Join My Updates Channel for using me 😌😉....</code>"
    FREE_USER_LIMIT_Q_SZE = "Sorry Friend, You Can Request only 1 Video Per {} minutes. Please try again after {} seconds later."
    REPLY_TO_DOC_FOR_SCSS = "Reply to a Telegram media to get screenshots"
