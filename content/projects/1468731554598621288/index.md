+++
title = "A compact case for Milwaukee screwdriver bits"
date = "2026-02-04"
description = "I bought a set of Milwaukee screwdriver bits and loved them immediately, but the case they came in was pretty massive, so I designed a much smaller one and printed it. The lettering on the lid is embossed and flood filled in a second colour, which meant working out how to do a multi colour print while my AMS was misbehaving. In the end the AMS held together long enough to get the part printed, and the result is fantastic."
path = "projects/4gwhkf/a-compact-case-for-milwaukee-screwdriver-bits"
[taxonomies]
categories = ["Making and fabrication"]
[extra]
thread_id = "1468731554598621288"
channel = "makes"
author_id = "213433184409485312"
author_name = "Stavros"
hero = "1468731571790938255.jpg"
thumb = "1468731571790938255.thumb.jpg"
images = ["1468731571790938255.jpg", "1468731997139763433.jpg", "1468732260063908124.jpg", "1468777679091138671.jpg", "1468934881768636416.jpg", "1468966944358010881.jpg"]
captions = ["", "", "", "", "", ""]
+++
I bought some Milwaukee screwdriver bits, which are apparently the best bits in the universe because I love them already. The only problem was that their case was pretty massive, so I designed a smaller one.

The lid has lettering on it, and I never managed to figure out how to paint the same surface in two colours, so instead I embossed the text and flood filled the embossed part. That put the second colour on a different layer rather than on the face, which meant several manual filament swaps once my AMS broke down and I could not print the white part.

Nicolas Mattia pointed me at a much better approach: in the slicer you add a second extruder, enable single extruder MMU, and set the custom tool change G code to M600 so the tool change becomes a filament swap. You use two models, assign each a colour, and slice them together, and since slicing always starts with the first extruder, putting white first gets it down to a single swap near the beginning of the print. Agisilaos also suggested slicing the letters and the case as two separate files and printing the letters first, aligning them carefully and keeping the toolhead from crashing into them, which would work for a single layer of letters but left me worried about homing the bed between two prints.

I also noticed after printing that I forgot the chamfer: the design has one, but the printed version is flat and only has the corners chamfered, since the chamfer is only on the vertical edges while the big case has one all the way around.

In the end the AMS worked long enough for me to print this. I do not really know what was wrong with it, I just restart it until it works and then it breaks again when I turn it off, and I am waiting for Bambu to get back to me about it. The case is fantastic and I love it.