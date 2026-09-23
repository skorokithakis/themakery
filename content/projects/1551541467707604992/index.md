+++
title = "Room presence sensor"
date = "2026-09-21"
description = "A small presence sensor built from an ESP32 and an LD2410 radar module, made to tell when someone is in the various rooms of a home, with a photodiode added to sense light."
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
captions = ["The ESP32 and LD2410 presence sensor Stavros built for the rooms of his home.", "The first iteration of the sensor's box.", "The first box, small and, in Stavros's words, \"pretty nice looking\".", "", "The circuit for the presence sensor.", "The final enclosure for the presence sensor."]
+++
Stavros built a presence sensor for the various rooms of his home using an ESP32 and an LD2410 sensor. He flashed ESPHome firmware to the ESP32, and it worked out of the box.

The LD2410 had a history with him. He once thought it was a cool sensor and bought ten off AliExpress, but always had bad results with them and couldn't figure out the calibration. This time Claude explained to him how the sensor worked and helped him write a calibrator, which he published as [ld2410-calibrator](https://github.com/skorokithakis/ld2410-calibrator). With that in hand, the sensor "works amazingly well."

The first iteration of the box turned out small and pretty nice looking, and it worked perfectly with very small latency. He found the sensors remarkably accurate, able to detect breathing 2m away, and in his view they pretty much solve the presence problem for smallish rooms of up to about 4m. A final enclosure followed.

Along the way he also added a photodiode to sense light. ESPHome handles it well, sending updates only when the light level changes significantly. The photodiode is soldered directly to a GPIO and 3.3V, using the GPIO's internal pulldown to form the voltage divider. The readings are a bit compressed towards the bright end, but it works very well in general.