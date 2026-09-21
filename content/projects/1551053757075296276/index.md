+++
title = "The Makery projects website"
date = "2026-09-20"
description = "I built a projects website for the Makery that is generated automatically from our Discord. I collect all the Discord messages in a database and use them both for the newsletter and for this site. The site looks at all the threads, and only threads, works out which ones are about a project, collects the text and images, and turns each one into a project page. It gives me somewhere to point people to for all the cool stuff we do here, since I like telling people about what I am building but cannot always find the time to do a proper writeup."
path = "projects/sw1zha/makery-discord-projects-website"
[taxonomies]
categories = ["Software"]
[extra]
thread_id = "1551053757075296276"
channel = "makes"
author_id = "213433184409485312"
author_name = "Stavros"
hero = "1551053819889057893.jpg"
thumb = "1551053819889057893.thumb.jpg"
images = ["1551053819889057893.jpg", "1551054084197458022.jpg"]
+++
I made the projects website for the Makery. I collect all Discord messages in a database and use them to generate the newsletter and this site. The site looks at all the threads (and only threads) in Discord, sees which one is about a project, collects text and images, and makes a nice project page out of it.

Right now it is a bit of a mishmash of everything because we have not had good hygiene with threads, but with a bit of curation I think it will be great. The text is going to be LLMese, but I will fix that later.

I asked whether anyone had privacy concerns about photos and details being posted publicly, since some of us might prefer not to share. Nicolas Mattia said he would rather not have all his pictures posted automatically and asked whether projects could be reviewed before going public. My first answer was that people could tell me not to publish something and I would remove it, and I wondered about adding something to the thread so you could specify whether you wanted it included. Nicolas Mattia suggested that using judgement during review, such as removing a picture with a face or personal data in it, would help, but that it is probably best to make it opt in. I agreed, and I am now deleting all the projects except a few and force pushing so I can make it opt in.