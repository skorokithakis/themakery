+++
title = "ESP32 voice recorder with automatic transfer and transcription"
date = "2026-02-15"
description = "A pocket voice recorder built around an ESP32 so I can take notes quickly. I press a button, it records audio, and when I'm near a PC it transfers the audio over Bluetooth and transcribes it automatically. Transcription happens on the computer rather than on the device, and startup is instant. The one part still fighting me is the power latching circuit: the MOSFET that is supposed to cut all the power doesn't."
path = "projects/64hweh/esp32-voice-recorder"
[taxonomies]
categories = ["Audio and music"]
[extra]
thread_id = "1472602730530078760"
channel = "ideas-and-feedback"
author_id = "213433184409485312"
author_name = "Stavros"
images = []
+++
I started out wanting a Pi Pico based voice recorder, but I ended up using an ESP32 instead. The goal was simple: be able to take notes quickly without pulling my phone out. You press the button, it records audio, and when you're near a PC it transfers the audio and transcribes it automatically. Transcription happens on the computer, not on the device. Startup is instant, and it works really well.

For storage I'm using FRAM, which is non volatile. I was soldering until 7am. For the Bluetooth transfer I had Claude work on it, and it made the transfer very reliable and really fast, while Codex spent 30 minutes progressively making it worse.

The remaining problem is power. The MOSFET that is supposed to turn all the power off doesn't, and I can't make a simple latching circuit work. Agisilaos suggested a physical switch as a stopgap, but that would mean flicking the switch on, pressing the button to record, then flicking it off again a few seconds later, at which point I might as well take my phone out. I've been simulating the circuit in CircuitJS, and I eventually worked out what I was doing wrong: the PMOS stops conducting when pulled low, and I was trying to pull it high. For now I think I'll just take the parasitic current.