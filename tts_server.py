from flask import Flask, request, send_file, jsonify
import edge_tts
import asyncio
import json
import uuid
from moviepy import ImageClip, AudioFileClip

app = Flask(__name__)

@app.route("/tts", methods=["POST"])
def tts():
    try:
        data = request.get_json(force=True)

        if isinstance(data, str):
            data = json.loads(data)

        text = data.get("text", "")

        if not text:
            return jsonify({"error": "No text provided"}), 400

        output_file = "voice.mp3"

        async def generate():
            communicate = edge_tts.Communicate(text, "en-US-AriaNeural")
            await communicate.save(output_file)

        asyncio.run(generate())

        return send_file(output_file, mimetype="audio/mpeg")

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/video", methods=["POST"])
def create_video():
    try:
        if "image" not in request.files or "audio" not in request.files:
            return jsonify({"error": "Image or audio missing"}), 400

        image = request.files["image"]
        audio = request.files["audio"]

        image_filename = f"image_{uuid.uuid4()}.jpg"
        audio_filename = f"audio_{uuid.uuid4()}.mp3"
        video_filename = f"video_{uuid.uuid4()}.mp4"

        image.save(image_filename)
        audio.save(audio_filename)

        audio_clip = AudioFileClip(audio_filename)

        image_clip = (
            ImageClip(image_filename)
            .with_duration(audio_clip.duration)
            .with_audio(audio_clip)
        )

        image_clip.write_videofile(
            video_filename,
            fps=24,
            codec="libx264",
            audio_codec="aac"
        )

        return send_file(video_filename, mimetype="video/mp4")

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(port=5000)
