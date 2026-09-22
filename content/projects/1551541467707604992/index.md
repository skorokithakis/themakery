+++
title = "Room presence sensor"
date = "2026-09-21"
description = "A small ESP32 and LD2410 presence sensor, boxed up for the rooms of a home, accurate enough to notice someone breathing two metres away."
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
captions = ["The presence sensor, built from an ESP32 and an LD2410.", "The first iteration of the box: small and pretty nice looking.", "", "", "The circuit.", "The final enclosure."]
+++
Stavros built a room presence sensor from an ESP32 and an LD2410 mmWave module, meant for the various rooms of their home. They flashed ESPHome firmware onto the ESP32, and it worked out of the box.

The sensor itself had a longer history. Earlier experiences with the LD2410 had soured them a little: it had never worked well, and after buying ten of them off AliExpress on the strength of how cool the sensor seemed, they kept getting bad results and could not work out the calibration. Claude explained how the sensor actually worked and helped them write a calibrator, published as [ld2410-calibrator](https://github.com/skorokithakis/ld2410-calibrator). After that, in their words, "it works amazingly well".

A first iteration of the box followed, small and pretty nice looking, and a final enclosure after it. Stavros reports very low latency and real accuracy from the sensors, which can easily detect breathing two metres away, and says they pretty much solve the presence problem, at least for smallish rooms of up to four metres.