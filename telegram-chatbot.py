import telegram
import telegram.ext
import re
from random import randint
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# api key for bot
API_KEY = "<insert-api-key-here>"
# create an updater object with api key
updater = telegram.ext.Updater(API_KEY)
# retrieve the dispatcher
dispatcher = updater.dispatcher

# our states, as integers
WELCOME = 0
QUESTION = 1
CANCEL = 2
CORRECT = 3


# the entry function
def start(update_obj, context):
    # send the question, and show the keyboard markup
    update_obj.message.reply_text("hello there, do you want to answer a question? (Yes/No)",
                                  reply_markup=telegram.ReplyKeyboardMarkup([['Yes', 'No']], one_time_keyboard=True)
                                  )
    # go to the welcome state
    return WELCOME


# helper function generates new numbers and sends the question
def randomize_numbers(update_obj, context):
    # store the numbers in the context
    context.user_data['rand_x'], context.user_data['rand_y'] = randint(0, 1000), randint(0, 1000)
    # send the question
    update_obj.message.reply_text(f"Calculate {context.user_data['rand_x']}+{context.user_data['rand_y']}")


# check if user wants to answer a question
def welcome(update_obj, context):
    if update_obj.message.text.lower() in ['yes', 'y']:
        # send question and go to the question state
        randomize_numbers(update_obj, context)
        return QUESTION
    else:
        # go to the cancel state
        return CANCEL


# in question state
def question(update_obj, context):
    # expected solution
    solution = int(context.user_data['rand_x']) + int(context.user_data['rand_y'])

    # check if solution is correct
    if solution == int(update_obj.message.text):

        # correct answer, ask if it was dificult
        update_obj.message.reply_text("Correct answer!")
        update_obj.message.reply_text("Was the question dificult to solve?")
        return CORRECT
    else:
        # wrong answer, reply, send new question and loop
        update_obj.message.reply_text("Wrong answer (t.t) ")

        # send another random numbers calculation
        randomize_numbers(update_obj, context)
        return QUESTION


# in the correct state
def correct(update_obj, context):
    if update_obj.message.text.lower() in ['yes', 'y']:
        update_obj.message.reply_text("Uh-oh, Someone has to study math more")
    else:
        update_obj.message.reply_text("You must be a math wizard!")

    # get user's first name
    first_name = update_obj.message.from_user['first_name']
    update_obj.message.reply_text(f"see you {first_name}!, bye for now")
    return telegram.ext.CommandHandler.END


def cancel(update_obj, context):
    # get user's first name
    first_name = update_obj.from_user['first_name']
    update_obj.message.reply_text(f"OKay, no question for you then, take care, {first_name}.",
                                  reply_markup=telegram.ReplyKeyboardRemove()
                                  )
    return telegram.ext.ConversationHandler.END


# regular expression that matches yes or no
yes_no_regex = re.compile(r'^(yes|no|y|n)$', re.IGNORECASE)

# create our conversationHandler, with one state
handler = telegram.ext.ConversationHandler(entry_points=[telegram.ext.CommandHandler('start', start)],
                                           states={
                                               WELCOME: [
                                                   telegram.ext.MessageHandler(telegram.ext.Filters.regex(yes_no_regex),
                                                                               welcome)],
                                               QUESTION: [
                                                   telegram.ext.MessageHandler(telegram.ext.Filters.regex(r'^\d+$'),
                                                                               question)],
                                               CANCEL: [
                                                   telegram.ext.MessageHandler(telegram.ext.Filters.regex(yes_no_regex),
                                                                               cancel)],
                                               CORRECT: [
                                                   telegram.ext.MessageHandler(telegram.ext.Filters.regex(yes_no_regex),
                                                                               correct)]
                                           },
                                           fallbacks=[telegram.ext.CommandHandler('cancel', cancel)],
                                           )
# add the handler to the dispatcher
dispatcher.add_handler(handler)

# start polling for updates from telegram
updater.start_polling()
# block until a signal is sent
updater.idle()
