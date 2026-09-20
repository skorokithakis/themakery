+++
title = "Sky Team PCB: An Electronic Cockpit Panel for the Board Game"
date = "2026-08-22"
description = "Nicolas and I are starting a project to build a PCB companion for the cooperative board game Sky Team, which was game of the year 2024. The plan is to recreate the game's cockpit elements in hardware — switches with their corresponding LEDs, plus some LEDs that act as counters. The first step is simply getting hold of a copy of the game: Amazon.de doesn't carry it and Amazon isn't really a thing in Switzerland, so Nicolas tracked down the original French edition and is picking it up from a store in Zurich. Once he's had a chance to play it and the requirements stop being abstract, we'll brainstorm the design together. Right now we're focused on figuring out how to connect everything; the software can come much later."
slug = "sky-team-pcb-an-electronic-cockpit-panel-for-the-board-game"
[extra]
thread_id = "1540811780790558912"
channel = "makes"
author_id = "213433184409485312"
author_name = "Stavros"
images = []
+++
## What we're making

I roped Nicolas in to make a PCB for the Sky Team board game. Sky Team is a cooperative game where two players land a plane, and the catch is that you can't talk to your teammate at all — you have to reason about why they're doing what they're doing. That constraint is what makes it great, and it's part of why I'm excited to build hardware for it. It picked up game of the year 2024.

## Getting a copy

The first obstacle was surprisingly mundane: sourcing the game. Amazon.de doesn't have Sky Team at all. Nicolas pointed out that Amazon effectively isn't available in Switzerland — you can order from neighbouring countries and Amazon covers the fees, but the local option is Galaxus, which sounds like a supervillain. Nicolas offered to buy it since that's much simpler from his side, and he wanted a non-German edition out of principle even though I pointed out the game has basically no text on it so the language doesn't matter. He found it in a store in Zurich, and in the end tracked down the original French edition, which is now in the mail.

## The electronics problem

The panel breaks down into two kinds of indicator. Some LEDs turn on when the switch next to them is turned on, and some LEDs act as counters. For the first group, my thought is that we might be able to wire them with an actual switch in series rather than driving everything in software.

The open question I raised is whether a microcontroller INPUT can drive an LED — hopefully better than an OUTPUT can. Neither of us could test it immediately: I was away from all my hardware, Nicolas's gear is all at the shop, and he was ill with two functioning neurons at the time. We'd apparently discussed this before but I couldn't remember the outcome. Nicolas also recalled something about a case where a switch is off but the LED is still on, which is exactly the sort of detail that will decide whether the series-switch trick works.

## Next steps

Nicolas needs to actually play the game before we can pin down what's needed — it's still very abstract from his side. Once the game arrives and he's played a few rounds, we'll brainstorm properly. Priority order is: figure out how to connect the stuff first, and leave the actual software until much later. A game night is also on the cards.