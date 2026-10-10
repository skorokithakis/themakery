+++
title = "Vetinari clock driven by an ESP32"
date = "2026-10-10"
description = "A Vetinari clock built from an inexpensive store-bought wall clock, whose second hand ticks irregularly yet still keeps perfect time, minute by minute."
path = "projects/2wfnb9/vetinari-clock-driven-by-an-esp32"
[taxonomies]
categories = ["Electronics"]
[extra]
thread_id = "1558352476414017536"
channel = "projects"
author_id = "213433184409485312"
author_name = "Stavros"
hero = "1558352561348542545.jpg"
thumb = "1558352561348542545.thumb.jpg"
images = ["1558352561348542545.jpg", "1558355409293541406.jpg"]
captions = ["The finished Vetinari clock, built from an inexpensive store-bought clock.", "Inside the clock movement. Stavros removed its simple PCB, which pulses a voltage onto the coil to turn the gear that moves the hands."]
+++
Stavros built a Vetinari clock: a clock whose ticking wanders and stutters, yet always adds up to exactly one minute every minute. It began with a $6 clock from a store, followed by a second $6 clock and two movements from AliExpress.

The first attempt was a complete failure. For days he tried to make it tick, but the second hand would only "just barely barely move" no matter what current settings or timings he tried. Ready to give up, he ordered three more movements from AliExpress to experiment on, and bought yet another clock while he waited. When he put a battery in that one, the problem finally revealed itself: it didn't tick at all. It was a continuous sweep clock, which was never going to work for irregular ticking.

When the new movements arrived, two turned out to be continuous sweep as well, but one ticked. He took out its PCB, which is basically just a crystal that pulses a voltage onto the coil to rotate the gear that moves the hands. Not wanting to repeat the mistakes of the past, he put an oscilloscope on it, noted the voltages and timings, and reproduced them with an ESP32, which he admits is overkill. This time it worked perfectly, and he then wrote the code to make it tick irregularly.

The clock has a few modes, all synced with NTP so that each minute comes out exact:

- one that ticks randomly each second
- one that ticks normally but then stops for a second
- one that behaves a bit like a pendulum, swinging fast at the bottom and slow at the top
- one that rushes to :59 and stays there for 30 seconds, then rushes again to :59 and waits

The trick behind the irregular ticking is a list of 59 integers, each one dictating how long a given second's tick lasts. In the mode that skips a second, for example, 58 of the integers are 980 and one is 2000, the skipped second. Some modes shuffle the list so those odd seconds land in a random position, while others, such as the pendulum mode, keep it in order. The 60th second is never dictated at all: the clock simply waits for NTP to tick over the minute, then moves to the 00 position. That way it is always synced with NTP, to the minute.

Setting the time is a small delight of its own. When the clock boots, it is stopped. Since it has no way of knowing where its hands are, it is told what time it is showing, and it then rushes forward (or stays stopped) until it catches up with the real time, at which point it carries on as normal.