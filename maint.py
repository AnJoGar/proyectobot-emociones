import telebot
import subprocess

from test import main


bot = telebot.TeleBot(' 1840113599:AAEhV28T3my6erhtUo0kxC3F9h7PQNREnGI')


@bot.message_handler(content_types=['voice'])
def handel(message):
    fileID = message.voice.file_id
    file = bot.get_file(fileID)
    down_file = bot.download_file(file.file_path)
    with open('test.ogg', 'wb') as f:
        f.write(down_file)

    src_filename = 'test.ogg'
    dest_filename = 'test.wav'

    process = subprocess.run(
        ['C:\\webem\\bin\\ffmpeg.exe', '-i', src_filename, dest_filename, '-y'])
    if process.returncode != 0:
        raise Exception("Error")

    result= main()
    bot.send_message(message.chat.id, result)


bot.polling(none_stop=True)
