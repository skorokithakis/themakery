+++
title = "Makery projects website"
date = "2026-09-21"
description = "A website that turns the Makery's Discord threads into project pages, so the things people build here have somewhere to live and somewhere to be pointed at."
path = "projects/rskwmz/makery-projects-website"
[taxonomies]
categories = ["Software"]
[extra]
thread_id = "1551538154014777354"
channel = "projects"
author_id = "213433184409485312"
author_name = "Stavros"
hero = "1551538285371723776.jpg"
thumb = "1551538285371723776.thumb.jpg"
images = ["1551538285371723776.jpg", "1551538408738791424.jpg"]
captions = ["The projects website Stavros built for the Makery.", "A project page assembled from the text and images of a Discord thread."]
+++
Stavros built the projects website for the Makery, and the machinery behind it starts further back than the pages themselves. They collect all the Discord messages into a database, and use that same store to generate both the newsletter and the site.

From there the site does the reading. It looks at all the threads, and only the threads, works out which ones are about a project, gathers up the text and the images, and turns each one into a project page.

As they put it, the result is "a bit of a mishmash of everything" for now, because thread hygiene in the server has not been perfect, though with a bit of curation they think it will be great. The point of it is to have something to point people to for all the cool stuff done here: Stavros generally likes telling everyone about what they are building, but cannot always find the time for a proper writeup. The generated text still reads like an LLM wrote it, which they plan to fix later.