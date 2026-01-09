Perfect — that’s exactly what **ffmpeg is good at** 👍
For **NO audio**, **mid quality**, and **smooth / fast recording**, use these settings.

---

## ✅ Recommended command (balanced & fast)

```bash
ffmpeg \
-f v4l2 \
-input_format mjpeg \
-video_size 1280x720 \
-framerate 30 \
-i /dev/video0 \
-an \
-c:v libx264 \
-preset veryfast \
-crf 23 \
-pix_fmt yuv420p \
output.mp4
```

---

## 🎯 Why this works well

* **720p** → lighter on CPU, smooth
* **MJPEG input** → avoids USB bottleneck
* **CRF 23** → good quality, smaller file
* **preset veryfast** → no frame drops
* **-an** → no audio at all

This setup is **fast**, **stable**, and **won’t stutter** on most systems.

---

## 🔧 If you still see frame drops

Try one of these tweaks:

### Lower CPU load more

```bash
-preset ultrafast
```

### Lower FPS

```bash
-framerate 25
```

### Lower resolution

```bash
-video_size 640x480
```

---

## 📁 Output file size (approx)

* 720p / 30fps / CRF 23
  ➜ ~70–100 MB per 10 minutes

---

## ✅ TL;DR (best choice)

**Use 720p + CRF 23 + veryfast preset + no audio**

If you want, tell me:

* CPU (Intel / AMD / laptop?)
* Ubuntu version
* Webcam resolution

I can tune it **exactly** so it never cuts frames 🚀
