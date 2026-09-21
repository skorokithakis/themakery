+++
title = "WiFi-driven analog clock with a sweep movement"
date = "2026-02-10"
description = "I wanted to convert a cheap analog clock so its hands are driven over WiFi, inspired by an ESP8266 analog clock project and the ventinari-clock project. My first attempt seemed to fail: the second hand crawled round in tiny steps instead of ticking, and after many long hours I gave up and assumed I had ruined the movement. Buying a second clock and putting a battery in it first showed me the real problem, because the thing sweeps rather than ticks. I pulled the old clock's circuit back out of the bin, measured it with an oscilloscope, and replicated the pulse pattern in firmware."
path = "projects/1szqgh/wifi-analog-clock-conversion"
[taxonomies]
categories = ["Electronics"]
[extra]
thread_id = "1470595311008354396"
channel = "links"
author_id = "213433184409485312"
author_name = "Stavros"
images = []
+++
I came across a project where someone converted a cheap analog clock to be driven by WiFi and immediately wanted one: [ESP8266_WiFi_Analog_Clock](https://github.com/jim11662418/ESP8266_WiFi_Analog_Clock). I also found more information in another project, [ventinari-clock](https://github.com/iracigt/ventinari-clock).

When I started building mine, I screwed something up: the second hand moved very, very slightly, each tick about 1 degree instead of 6. After many, many long hours working on this clock, I gave up on it and figured I had ruined the motion, because it kept moving extremely slowly no matter what parameters I used.

So I went out and got another one. This time I figured I'd put a battery in first, just to see what happens, and when I plugged the battery in, THE FUCKING THING SWEEPS! That's why the first clock was going so slowly: it wasn't built to tick at all.

Then I dug the old clock's circuit out of the trash, measured it with an oscilloscope, replicated the pulse pattern in firmware, and it works perfectly. I left it running overnight, but now it doesn't work, and I think something broke.