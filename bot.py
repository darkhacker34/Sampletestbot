import subprocess
from pyrogram import Client, filters
from moviepy.editor import VideoFileClip

app = Client("my_bot")

@app.on_message(filters.video)
async def handle_video(client, message):
    video_path = "downloads/original_video.mp4"
    output_path = "downloads/sample_video.mp4"
    fixed_video_path = "downloads/fixed_video.mp4"

    # Download the video file
    await message.download(video_path)

    try:
        # Re-encode the video to ensure compatibility
        subprocess.run(
            ["ffmpeg", "-i", video_path, "-c:v", "libx264", "-c:a", "aac", fixed_video_path],
            check=True
        )

        # Create a sample video (e.g., first 10 seconds)
        with VideoFileClip(fixed_video_path) as video_clip:
            sample_clip = video_clip.subclip(0, 10)  # Get the first 10 seconds
            sample_clip.write_videofile(output_path)

        print("Sample video created successfully.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    app.run()
