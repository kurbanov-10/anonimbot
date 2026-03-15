import telebot

token = '8335459586:'
bot=telebot.TeleBot(token)

user_targets={}

@bot.message_handler(commands=['start'])
def send_welcome(message):
    chat_id=message.chat.id
    text_parts=message.text.split()
    
    if len(text_parts)==2:
        target_id=text_parts[1]
        
        if str(chat_id)==target_id:
            bot.send_message(chat_id,"O'zingizga o'zingiz anonim xabar yoza olmaysiz! 😊")
        else:
            user_targets[chat_id]=target_id
            bot.send_message(chat_id,"✅ Ulandingiz! Endi xabarlaringizni yuborishingiz mumkin.")
            
    else:
        bot_info=bot.get_me()
        link=f"https://t.me/{bot_info.username}?start={chat_id}"
        javob=(
            f"👋 Salom, {message.from_user.first_name}!\n\n"
            f"Sizning shaxsiy anonim havolangiz:\n{link}\n\n"
            f"Buni tarqating va anonim xabarlarni qabul qiling!"
        )
        bot.send_message(chat_id, javob)
        
if __name__ == '__main__':
    print("Bot ishga tushdi...")
    bot.polling(none_stop=True)