+++
title = "ESP32 voice recorder for quick notes"
date = "2026-02-15"
description = "I built a small ESP32 based voice recorder so I can take notes quickly: I press a button, it records audio, and when I am near a PC it transfers the audio over Bluetooth and transcribes it automatically. Startup is instant, and the Bluetooth transfer ended up very reliable and fast. The one thing still fighting me is the power side, where the MOSFET that is meant to cut all the power off does not do its job."
slug = "esp32-voice-recorder"
[taxonomies]
categories = ["Electronics"]
[extra]
thread_id = "1472602730530078760"
channel = "ideas-and-feedback"
author_id = "213433184409485312"
author_name = "Stavros"
images = []
+++
I started out wanting to make a Pi Pico based voice recorder, and asked around for anyone with experience on that, but I ended up using an ESP32 instead. I wanted it so I could quickly take notes.

The way it works is simple: you press the button, it records audio, and when you're near a PC it transfers the audio and transcribes it automatically. Transcription happens on the computer, not on the device. For storage there's the FRAM, which is non volatile. Startup speed went back and forth while I was testing, but now it's instant, and it works really well.

I was soldering until 7am, and the MOSFET that is supposed to turn all the power off doesn't. Claude did some amazing feats of engineering and made the Bluetooth transfer very reliable and really fast, where Codex spent 30 minutes progressively making it worse, but on the power side Claude was useless and I wasted hours following its advice. I can't make a simple latching circuit. I've been using [CircuitJS](https://www.falstad.com/circuit/circuitjs.html) to simulate it and I didn't understand what was going on, until I worked out that the PMOS stops conducting when pulled low and I was trying to pull it high. If I manage to fix the power issue, I'm done, but for now I think I'll just take the parasitic current.