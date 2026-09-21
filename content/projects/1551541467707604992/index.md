+++
title = "Room presence sensor"
date = "2026-09-21"
description = "I built a room presence sensor for the various rooms of my home using an ESP32 and an LD2410 mmWave sensor, running ESPHome firmware. After years of poor results with LD2410 sensors, I wrote a calibrator tool that finally got them working properly, and packaged the whole thing in a small printed box with very low detection latency."
path = "projects/0sewb3/esp32-ld2410-room-presence-sensor"
[taxonomies]
categories = ["Electronics"]
[extra]
thread_id = "1551541467707604992"
channel = "projects"
author_id = "213433184409485312"
author_name = "Stavros"
hero = "1551541582581207080.jpg"
thumb = "1551541582581207080.thumb.jpg"
images = ["1551541582581207080.jpg", "1551542148917370920.jpg", "1551542187622146128.jpg", "1551542202990071879.jpg"]
+++
I used an ESP32 and an LD2410 to make a presence sensor for the various rooms of my home. I flashed ESPHome firmware to the ESP32 and it worked out of the box.

Previous experiences with LD2410 sensors soured me a bit, since they never worked well for me. I initially thought it was a cool sensor so I bought ten off AliExpress, but then always had bad results with them and couldn't figure out the calibration. Claude explained to me how the sensor worked and helped me write a calibrator, which is up at [ld2410-calibrator](https://github.com/skorokithakis/ld2410-calibrator). Now it works amazingly well.

I also made a first iteration of the box for it. It's small and pretty nice looking. I really like it, it works perfectly, and the latency is super small.