+++
title = "Sky Team board game PCB"
date = "2026-08-22"
description = "A PCB project built around the cooperative board game Sky Team, with switches and LEDs standing in for the cockpit controls. The first job is working out how everything connects: some of the LEDs come on with the switch next to them, so those might be wired with the switch in series, while other LEDs act as counters. The software comes much later, once the game has been played enough to know what is actually needed."
slug = "sky-team-board-game-pcb"
[taxonomies]
categories = ["Electronics"]
[extra]
thread_id = "1540811780790558912"
channel = "makes"
author_id = "213433184409485312"
author_name = "Stavros"
images = []
+++
I want to build a PCB for the board game Sky Team, and Nicolas Mattia is in on it and doing the PCBs. It is a very fun game: you cannot talk to your teammate at all, so you have to reason about why they are doing what they are doing. If you want to look it up, it is [on BoardGameGeek](https://boardgamegeek.com/boardgame/373106/sky-team).

First we need a copy of the game. Amazon.de does not stock it, and Nicolas pointed out that Amazon is not really a thing in Switzerland, where you would use galaxus.ch instead, though you can order from neighbouring countries and Amazon covers the fees. Nicolas offered to get it himself since that is much simpler, and wanted a non German edition out of principle even though the board barely has any text on it. He found it in a store in Zurich, and then found the original French edition, which is in the mail.

The next step is figuring out how to connect everything; the actual software can come much later. Some of the switches turn on their corresponding LEDs, and some other LEDs are counters. For the first group I wondered whether we could just put an actual switch in series, and whether an INPUT can drive an LED, hopefully better than an OUTPUT can. Neither of us could test it straight away since we were both away from our hardware. Nicolas also wants to play the game before we go further, because it is still very abstract without that, and then we brainstorm.