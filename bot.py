from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

def start(update: Update, context: CallbackContext):
    update.message.reply_text('Send me a video to generate a 10-second sample.')

def handle_video(update: Update, context: CallbackContext):
    video_file = update.message.video.get_file()
    video_file.download('input_video.mp4')

    # Process video
    clip = VideoFileClip('input_video.mp4')
    sample_clip = clip.subclip(0, 10)
    sample_clip.write_videofile('sample_video.mp4', codec='libx264', audio_codec='aac')

    # Send back the sample video
    context.bot.send_video(chat_id=update.effective_chat.id, video=open('sample_video.mp4', 'rb'))

    # Clean up files
    os.remove('input_video.mp4')
    os.remove('sample_video.mp4')

def main():
    updater = Updater(os.getenv("7213907869:AAFByjyPdeXjsqT-dPdzVvDyV_0q5qWAKrY"))  # Use environment variable
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.video, handle_video))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
