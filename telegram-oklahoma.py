from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import random
import schedule
import time

# Adicione esta linha no início do seu script para obter o Chat ID
# Substitua '6481332485:AAFIWoG5u99v2Lyo-SEqtZKtneu9-9_P9L0' pelo token real do seu bot
from telegram import Bot
bot = Bot(token='6481332485exemple-9_P9L0')
chat_id = bot.get_updates()[-1].message.chat_id

# Função para o comando /start
def start(update, context):
    update.message.reply_text('Olá! Eu sou um bot simples. Como posso ajudar?')

# Função para o comando /carinho
def send_love(context):
    messages = [
        '💖 Você é a razão do meu sorriso todos os dias, ioio! 😊',
        'Com você, ioio cada dia é uma nova aventura cheia de amor! ❤️',
        'Seu amor, oioié a música que faz meu coração dançar! 🎶💕',
        'Você é o sol que ilumina até os dias mais nublados da minha vida! ☀️💛',
        'Nosso amor é como uma história mágica que nunca acaba! 📖✨',
        'Você é a peça que faltava no quebra-cabeça do meu coração! 🧩💓',
        'Cada momento ao seu lado é como um sonho realizado! 💭💘',
        'Com você, cada obstáculo se transforma em uma oportunidade de fortalecer nosso amor! 🌈💑',
        'Seu abraço é meu lugar favorito na Terra! 🌍🤗',
        'Meu amor por você é tão grande que até as estrelas ficam com inveja! ✨💖',
        'Você é a inspiração por trás de todas as minhas melhores ideias! 💡💏',
        'Se eu fosse uma abelha, você seria minha flor favorita! 🐝🌸💕',
        'Com você, a vida é um poema romântico que nunca acaba! 📜❤️',
        'Você é a obra-prima que eu admiraria todos os dias da minha vida! 🎨🌹',
        'Meu amor por você é como o Wi-Fi - forte e incondicional! 📶💞'
    ]
    random_message = random.choice(messages)
    context.bot.send_message(chat_id=chat_id, text=random_message)

# Função para lidar com mensagens de texto
def echo(update, context):
    update.message.reply_text('Você disse: ' + update.message.text)

# Configuração e inicialização do bot
def main():
    # Substitua 'SEU_TOKEN' pelo token do seu bot no Telegram
    updater = Updater('6481332485:AAFIWoG5u99v2Lyo-SEqtZKtneu9-9_P9L0', use_context=True)

    dp = updater.dispatcher

    # Adiciona handlers para diferentes comandos
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("carinho", send_love))
    
    # Adiciona handler para lidar com mensagens de texto
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Configuração do agendamento para enviar mensagem de carinho todos os dias às 10h
    job_context = {'4137926408': chat_id}  # Substitua 'SEU_CHAT_ID' pelo ID do chat com sua namorada
    updater.job_queue.run_daily(send_love, time(hour=10, minute=0, second=0), context=job_context)

    # Inicia o bot
    updater.start_polling()

    # Mantém o bot em execução até que você o interrompa manualmente
    updater.idle()

if __name__ == '__main__':
    main()
