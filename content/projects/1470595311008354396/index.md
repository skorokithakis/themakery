+++
title = "WiFi-driven analog clock from a cheap movement"
date = "2026-02-10"
description = "I set out to convert a cheap analog clock so it could be driven over WiFi, inspired by a couple of existing projects. My first attempt seemed broken because the second hand crawled around a degree at a time, so I eventually gave up on it and bought a second clock. Putting a battery in that one first revealed the real problem: the movement sweeps rather than ticks. I pulled the old clock's circuit back out of the trash, measured it on an oscilloscope, replicated the pulse pattern in firmware, and got it working."
slug = "wifi-analog-clock-conversion"
[taxonomies]
categories = ["Electronics"]
[extra]
thread_id = "1470595311008354396"
channel = "links"
author_id = "213433184409485312"
author_name = "Stavros"
images = []
+++
I saw that someone had converted a cheap analog clock to be driven by WiFi and immediately wanted one, based on [ESP8266_WiFi_Analog_Clock](https://github.com/jim11662418/ESP8266_WiFi_Analog_Clock), with some more info on another project at [ventinari-clock](https://github.com/iracigt/ventinari-clock).

When I tried to make it, I screwed something up: the second hand moved very, very slightly, with each tick covering about 1 degree instead of 6. After many, many long hours on the clock I gave up on it and figured I had ruined the motion, since it kept moving extremely slowly no matter what parameters I used.

So I went out and got another one. This time I figured I would put a battery in first, just to see what happened, and the thing swept. That was why the first clock was going so slowly: it was not built to tick at all.

I then dug the old clock's circuit out of the trash, measured it with an oscilloscope, replicated the pulse pattern in firmware, and it worked perfectly. I left it running overnight, but now it does not work, and I think something broke.