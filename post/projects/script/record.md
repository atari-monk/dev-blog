# Screen Capture with ffmpeg

**Option 1: Faster preset for real-time capture**
```powershell
# Faster real-time capture
ffmpeg -f gdigrab -framerate 30 -thread_queue_size 1024 -i desktop -f dshow -thread_queue_size 1024 -i audio="Miks stereo (Realtek(R) Audio)" -c:v libx264 -preset ultrafast -crf 23 -pix_fmt yuv420p -c:a aac output.mkv
```

**Option 2: Balanced quality and speed**
```powershell
# Balanced settings
ffmpeg -f gdigrab -framerate 30 -thread_queue_size 1024 -i desktop -f dshow -thread_queue_size 1024 -i audio="Miks stereo (Realtek(R) Audio)" -c:v libx264 -preset veryfast -crf 21 -pix_fmt yuv420p -c:a aac output.mkv
```

**Option 3: Lower resolution for better performance**
```powershell
# Lower resolution for smooth capture
ffmpeg -f gdigrab -framerate 30 -thread_queue_size 1024 -i desktop -f dshow -thread_queue_size 1024 -i audio="Miks stereo (Realtek(R) Audio)" -vf "scale=1280:720" -c:v libx264 -preset veryfast -crf 22 -pix_fmt yuv420p -c:a aac output.mkv
```

**Option 4: Hardware acceleration (if available)**
```powershell
# Hardware accelerated (much faster if supported)
ffmpeg -f gdigrab -framerate 30 -thread_queue_size 1024 -i desktop -f dshow -thread_queue_size 1024 -i audio="Miks stereo (Realtek(R) Audio)" -c:v h264_nvenc -preset fast -pix_fmt yuv420p -c:a aac output.mkv
```

**Option 2.1: Higher bitrate profile (more consistent quality)**
```powershell
# Maximum quality for screen recording
ffmpeg -f gdigrab -framerate 30 -thread_queue_size 1024 -i desktop -f dshow -thread_queue_size 1024 -i audio="Miks stereo (Realtek(R) Audio)" -c:v libx264 -preset faster -crf 12 -pix_fmt yuv420p -profile:v high -level 4.1 -c:a aac -b:a 192k output.mkv
```

**Option 2.2: Even lower CRF (near lossless)**
```powershell
# Near-lossless quality
ffmpeg -f gdigrab -framerate 30 -thread_queue_size 1024 -i desktop -f dshow -thread_queue_size 1024 -i audio="Miks stereo (Realtek(R) Audio)" -c:v libx264 -preset fast -crf 10 -pix_fmt yuv420p -c:a aac output.mkv
```

**Option 2.3: Professional screen recording settings**
```powershell
# Professional screen capture quality
ffmpeg -f gdigrab -framerate 30 -thread_queue_size 1024 -i desktop -f dshow -thread_queue_size 1024 -i audio="Miks stereo (Realtek(R) Audio)" -c:v libx264 -preset medium -crf 8 -pix_fmt yuv420p -x264-params keyint=60:min-keyint=30 -c:a aac -b:a 256k output.mkv
```

**Option 4.1: NVIDIA NVENC with high quality**
```powershell
# NVIDIA GPU accelerated - Best performance/quality
ffmpeg -f gdigrab -framerate 60 -thread_queue_size 1024 -i desktop -f dshow -thread_queue_size 1024 -i audio="Miks stereo (Realtek(R) Audio)" -c:v h264_nvenc -preset p6 -tune hq -rc vbr -cq 18 -b:v 0 -pix_fmt yuv420p -c:a aac -b:a 192k output.mkv
```

**Option 4.2: NVIDIA with lossless quality**
```powershell
# NVIDIA near-lossless quality
ffmpeg -f gdigrab -framerate 60 -thread_queue_size 1024 -i desktop -f dshow -thread_queue_size 1024 -i audio="Miks stereo (Realtek(R) Audio)" -c:v h264_nvenc -preset p4 -tune lossless -rc constqp -cq 0 -pix_fmt yuv420p -c:a aac -b:a 192k output.mkv
```

**Option 4.3: Balanced NVIDIA settings**
```powershell
# NVIDIA balanced high quality
ffmpeg -f gdigrab -framerate 60 -thread_queue_size 1024 -i desktop -f dshow -thread_queue_size 1024 -i audio="Miks stereo (Realtek(R) Audio)" -c:v h264_nvenc -preset p5 -tune hq -rc vbr -cq 14 -b:v 10M -pix_fmt yuv420p -c:a aac -b:a 192k output.mkv
```
