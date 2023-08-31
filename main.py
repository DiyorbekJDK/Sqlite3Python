import telebot
import sqlite3

bot = telebot.TeleBot('5926541709:AAGnE0YLen0josWnwtBQB_nhJMVMMJvjsIM')
print("Bot has started")


@bot.message_handler(commands=['start'])
def start(message):
    # connection = sqlite3.connect('db/BotDatabase.sql')
    # cursor = connection.cursor()

    # cursor.execute('CREATE TABLE IF NOT EXISTS users (id int primary key, language varchar(50), bot_post varchar(50))')
    # connection.commit()
    # cursor.close()
    # connection.close()

    mess = "Дарова!"
    if checkLanguage(1342503849) == "English":
        print("English")
    elif checkLanguage(1342503849) == "Russian":
        print("Russian")
    bot.send_message(message.chat.id, mess)


def saveUser(id, language, post):
    connection = sqlite3.connect('db/BotDatabase.sql')
    cursor = connection.cursor()
    cursor.execute("INSERT INTO users (id,language,bot_post) VALUES ('%s','%s','%s')" % (id, language, post))
    connection.commit()
    cursor.close()
    connection.close()
    print("Saved")


def getAllUsers():
    connection = sqlite3.connect('db/BotDatabase.sql')
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM users')
    user_list = cursor.fetchall()
    cursor.close()
    connection.close()

    info = ''
    for element in user_list:
        info += f'{element}'

    print("User:")
    print(user_list)
    file = open("D:/CanDeleteAnyTime/PycharmProjects/Sqlite3Python/data/user_in_text.txt", 'w')
    file.write(f'{user_list}')
    file.close()


def checkUser(id, language, post):
    connection = sqlite3.connect('db/BotDatabase.sql')
    cursor = connection.cursor()
    cursor.execute("SELECT id FROM users WHERE id='%s'" % id)

    res = cursor.fetchone()
    connection.commit()
    cursor.close()
    connection.close()
    if res:
        print("User already exist")
    else:
        saveUser(id, language, post)


def checkLanguage(id):
    connection = sqlite3.connect('db/BotDatabase.sql')
    cursor = connection.cursor()

    cursor.execute("SELECT language FROM users WHERE id = '%s'" % id)
    user = cursor.fetchone()
    cursor.close()
    connection.close()

    info = ''
    for element in user:
        info += f'{element}'
    return info


bot.polling(none_stop=True)
