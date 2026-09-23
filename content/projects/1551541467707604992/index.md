+++
title = "Room presence sensor"
date = "2026-09-21"
description = "A small room presence sensor built from an ESP32 and an LD2410 radar module, made to tell when someone is in the various rooms of a home."
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
captions = ["The presence sensor Stavros built from an ESP32 and an LD2410.", "The first iteration of the sensor's box.", "The first box, small and, in Stavros's words, \"pretty nice looking\".", "", "The circuit for the presence sensor.", "The final enclosure for the presence sensor."]
+++
Stavros set out to make a presence sensor for the various rooms of his home, pairing an ESP32 with an LD2410 sensor. He flashed ESPHome firmware to the ESP32, and it worked out of the box.

The LD2410 had a history with him. He had once thought it a cool sensor and bought ten off AliExpress, but always had bad results with them and couldn't figure out the calibration. This time, with Claude explaining how the sensor worked, he wrote a calibrator, [ld2410-calibrator](https://github.com/skorokithakis/ld2410-calibrator), and after that the sensor "works amazingly well".

The first iteration of the box came out small and pretty nice looking, and he was pleased with how it performed: it works perfectly, with super small latency. The sensors proved remarkably accurate, easily detecting breathing 2m away, and by his account they pretty much solve the presence problem, at least for smallish rooms of up to 4m. He finished by sharing the circuit and the final enclosure.