import logging
from telegram import Update, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import (Application,
                          CommandHandler,
                          ContextTypes,
                          MessageHandler,
                          filters,
                          CallbackQueryHandler)
from config import dandy_cat_bot
from collections_for_import import the_Zen_of_Python, best_thoughts_west
import random

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)

keyboard = [
        [
            "the best thoughts of humanity"
        ],
        [
            'the zen of python'
        ],
        [
            'help'
        ],
        ]

reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    await update.message.reply_html(f"Hi {user.mention_html()}!\n"
                                    f"This bot was made by Yudin Vladyslav for family use",
                                    reply_markup=reply_markup)


async def reply_text(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """the message is displayed after duplicating the
                button name from ReplyKeyboardMarkup in the chat"""
    if update.message.text == 'help':
        await help_command(update, context)
    elif update.message.text == 'the best thoughts of humanity':
        await best_thoughts(update, context)
    elif update.message.text == 'the zen of python':
        await zen_command(update, context)
    else:
        await update.message.reply_text(f'>>>{update.message.text}')


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    text = (f'/start - to start or reboot the bot\n'
            f'/zen - for remember design principles and programming philosophy in Python.\n'
            f'\nmy useful links 🔭')
    keyboard_inline = [
        [
            InlineKeyboardButton('my github', url='https://github.com/Yulauk'),
            InlineKeyboardButton('PEP 8', url='https://peps.python.org/pep-0008/')
        ],
        [InlineKeyboardButton("python-telegram-bot", url='https://docs.python-telegram-bot.org/en/v20.6/index.html')]
    ]

    reply_markup_inline = InlineKeyboardMarkup(keyboard_inline)
    await update.message.reply_text(text, reply_markup=reply_markup_inline)
    # await update.message.reply_html("Help!"+'<b>bold</b>')
    # await update.message.reply_text('*Help2*', parse_mode='MarkdownV2')


async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Parses the CallbackQuery and updates the message text."""
    query = update.callback_query

    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    await query.answer()
    await query.edit_message_text(text=query.data)


async def best_thoughts(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """The best human thoughts"""
    thought = random.choice(list(best_thoughts_west.keys()))
    output = (f'{thought}\n\_\n_автор: {best_thoughts_west[thought]["автор"]}\nкомментарий: '
              f'{best_thoughts_west[thought]["комментарий"]}_')
    await update.message.reply_text(output, parse_mode='Markdown')


async def zen_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """import this"""
    random_string = the_Zen_of_Python[random.randint(0, len(the_Zen_of_Python)-1)]
    await update.message.reply_text(random_string)


def main() -> None:
    """Start the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(dandy_cat_bot).build()
    print('server is running...')
    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler('zen', zen_command))
    application.add_handler(CallbackQueryHandler(button))
    application.add_handler(MessageHandler(filters.Regex("^(help|the best thoughts"
                                                         " of humanity|the zen of python)$"), reply_text))
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    try:
        main()
    except Exception as ex:
        print('Exception:', ex)
    finally:
        print('telegram server is stopped...')
