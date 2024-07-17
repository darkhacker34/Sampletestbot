import subprocess
from pyrogram import Client, filters
from moviepy.editor import VideoFileClip
import random
import os

app = Client(
    "my_bot",
    api_id=29843602,
    api_hash="fc6589fe625b0d1e0ba1ee7d876e8541",
    bot_token="7213907869:AAEWyjLs492_EiUzbS3vIYkTfpxcbF5bYIU"
)

@app.on_message(filters.video)
async def handle_video(client, message):
    video_url = message.video.file_id
    fixed_video_path = "downloads/fixed_video.mp4"
    output_path = "downloads/sample_video.mp4"

    # Ensure downloads directory exists
    os.makedirs("downloads", exist_ok=True)

    try:
        # Re-encode the video to ensure compatibility
        subprocess.run(
            ["ffmpeg", "-i", f"https://api.telegram.org/file/bot{client.token}/{video_url}", "-c:v", "libx264", "-c:a", "aac", fixed_video_path],
            check=True
        )

        # Get the duration of the video
        with VideoFileClip(fixed_video_path) as video_clip:
            duration = video_clip.duration
            start_time = random.uniform(0, max(0, duration - 20 * 60))  # Random start time for a 20-minute clip
            sample_clip = video_clip.subclip(start_time, start_time + 20 * 60)  # Get a 20-minute clip
            sample_clip.write_videofile(output_path)

        await message.reply_video(output_path)

        print("Sample video created and sent successfully.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    app.run()
