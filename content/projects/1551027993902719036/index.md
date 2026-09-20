+++
title = "An Android digital assistant app with custom actions"
date = "2026-09-20"
description = "I built a digital assistant app for Android that registers itself as the system assistant, so long-pressing the power button pops it up and starts recording audio. You can add various actions to it, including adding calendar events and alarms, and anything it doesn't handle falls through to my own digital assistant, Stavrobot. It transcribes with the OpenAI or ElevenLabs API and uses OpenAI as a lightweight LLM to parse the actions, and if you're offline it keeps retrying everything until it works."
slug = "android-digital-assistant-app"
[taxonomies]
categories = ["Software"]
[extra]
thread_id = "1551027993902719036"
channel = "makes"
author_id = "213433184409485312"
author_name = "Stavros"
hero = "1551028159015690340.jpg"
thumb = "1551028159015690340.thumb.jpg"
images = ["1551028159015690340.jpg", "1551028162404814848.jpg", "1551028469562081320.jpg", "1551029055460089897.jpg"]
+++
I've made a digital assistant app for Android. It can register as an assistant, so long-pressing the power button makes it pop up and record audio.

You can add various actions to it, and the fallback goes to my digital assistant, [Stavrobot](https://github.com/skorokithakis/stavrobot). If you're offline it keeps retrying everything until it works.

It uses the OpenAI or ElevenLabs API for transcription, and OpenAI as a lightweight LLM to parse the actions. You can tell it to add calendar events and alarms as well.