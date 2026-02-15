# AI Video Generation Pipeline

An end-to-end automated AI-powered pipeline that transforms a simple **topic input** into a YouTube-ready MP4 video.

---

## Project Overview

This project demonstrates workflow automation and AI integration using **n8n** and **Python (Flask)**.

Pipeline Flow:

**Topic → AI Script → Text-to-Speech → Visual Fetching → Video Composition → MP4 Output**

The entire process runs automatically from a **single trigger**, fulfilling the assignment requirement.

---

## Workflow Architecture

### 1. Topic Input
A topic is provided via an n8n trigger node.

### 2. AI Script Generation
An AI model generates a video script based on the topic.

### 3. Voice Generation (Edge TTS)
The script is converted into natural-sounding speech using **Edge TTS**, exposed via a custom Flask API.

### 4. Visual Fetching (Pexels API)
Relevant visuals are dynamically retrieved from the **Pexels API**.

### 5. Video Composition (MoviePy)
The selected image and generated audio are merged into an **MP4 video** using **MoviePy** and **FFmpeg**.

---

## 🛠️ Tools & Technologies

- **n8n** → Workflow orchestration  
- **Python (Flask)** → API endpoints  
- **Edge TTS** → AI voice synthesis  
- **MoviePy** → Video creation  
- **FFmpeg** → Media encoding  
- **Pexels API** → Visual assets  

---

## How to Run

### 1️. Install Dependencies

```bash
pip install -r requirements.txt
````

---

### 2. Start Flask Server

```bash
python tts_server.py
```

Runs on:

```
http://localhost:5000
```

---

### 3️. Expose API (for n8n Cloud)

```bash
ngrok http 5000
```

Update n8n HTTP Request nodes with the generated ngrok URL.

---

### 4️. Execute Workflow

Trigger the n8n workflow → pipeline generates video automatically.

---

## Output

✔ AI-generated script
✔ AI-generated voiceover
✔ Dynamically fetched visuals
✔ Final MP4 video

Generated from a **single trigger**.

---

## Challenges Faced

* Handling binary data between n8n and Flask
* Synchronizing image/audio duration
* MoviePy version compatibility
* Codec playback issues

---

## Future Improvements

* Subtitles / captions
* Multi-image slideshow videos
* Thumbnail automation
* SEO metadata generation
* Direct YouTube upload

---

## Security Note

API keys have been removed from this repository for security purposes.

Use environment variables or n8n credentials when running the workflow.

---

## Author

Built by **Eepsita Modi**
