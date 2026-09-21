+++
title = "Room presence sensor"
date = "2026-09-21"
description = "I built a room presence sensor from an ESP32 and an LD2410 mmWave sensor, so I can tell when the various rooms of my home are occupied. I flashed ESPHome to the ESP32 and it worked out of the box, but the LD2410 had always given me bad results before, so I wrote a calibrator for it. With calibration it works amazingly well, with very low latency, and it sits in a small enclosure I like the look of."
path = "projects/0sewb3/room-presence-sensor"
[taxonomies]
categories = ["Electronics"]
[extra]
thread_id = "1551541467707604992"
channel = "projects"
author_id = "213433184409485312"
author_name = "Stavros"
hero = "1551541582581207080.jpg"
thumb = "1551541582581207080.thumb.jpg"
images = ["1551541582581207080.jpg", "1551542148917370920.jpg", "1551542187622146128.jpg", "1551542202990071879.jpg", "1551644379805122591.jpg", "1551644475036672121.jpg"]
captions = ["The presence sensor I made from an ESP32 and an LD2410.", "The first iteration of the box.", "The first iteration of the box, which is small and pretty nice looking.", "", "The circuit.", "The final enclosure."]
+++
I used an ESP32 and an LD2410 to make a presence sensor for the various rooms of my home. I flashed ESPHome firmware to the ESP32 and it worked out of the box.

Previous experiences with LD2410 sensors had soured me a bit, since they never worked well for me. I initially thought it was a cool sensor so I bought ten off AliExpress, but then always had bad results with them and couldn't figure out the calibration. Claude explained to me how the sensor worked and helped me write a calibrator, which is at [ld2410-calibrator](https://github.com/skorokithakis/ld2410-calibrator). Now it works amazingly well.

The first iteration of the box is small and pretty nice looking. I really like it, and it works perfectly too, with super small latency. I'm really liking how accurate these sensors are, they can easily detect breathing 2m away. They pretty much solve the presence problem, at least for smallish rooms of up to 4m.