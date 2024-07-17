from pyrogram import Client, filters
from moviepy.video.io.VideoFileClip import VideoFileClip
import os
import random

app = Client("sample_video_bot", api_id=Config.API_ID, api_hash=Config.API_HASH, bot_token=Config.BOT_TOKEN)

@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text("Send me a video to generate a random sample from it.")

@app.on_message(filters.video)
async def handle_video(client, message):
    video = message.video
    video_path = await message.download()

    # Process video to generate a random sample
    with VideoFileClip(video_path) as video_clip:
        sample_duration = 10  # Duration of the sample in seconds
        video_duration = video_clip.duration
        start_time = random.uniform(0, video_duration - sample_duration)
        sample_clip = video_clip.subclip(start_time, start_time + sample_duration)
        sample_path = f"sample_{os.path.basename(video_path)}"
        sample_clip.write_videofile(sample_path, codec="libx264")

    # Send the sample video back to the user
    await message.reply_video(sample_path)

    # Clean up
    os.remove(video_path)
    os.remove(sample_path)

app.run()
