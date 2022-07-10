---
title: Starting a Podcast
permalink: starting-a-podcast
date: 2020-12-14
---

So I started a [podcast](https://www.mql.fm/). And actually, I think this is Elliot's fault because I really enjoyed making an appearance on [emailtalk](https://www.emailtalk.fm/episodes/06-privacy-round-table-w-dylan-smith-jacques-corby-tuech-jay-oram). Or maybe I'm just a bit vain and ended up liking the sound of my own voice too much. I guess time will tell.

I just released Episode 2 last Friday so now seems like a good time to reflect a little on the journey and how I've put this together. I suspect I'm probably doing a lot wrong but this seems to be working for now[^1].


## The Recording Setup

I spent longer than I care to admit geeking out on microphone trivia, comparing XLR vs USB options, condenser vs dynamic and all that other junk. Eventually I realised I was probably overthinking this stuff so picked up an [Elgato Wave 3](https://www.elgato.com/en/wave-3) with the optional [pop filter](https://www.elgato.com/en/wave-pop-filter). USB definitely seemed like the way to go, I've got too much shit on my desk already to want to faff about with audio interfaces and a million more cables.

I could just as easily have gone with a classic Yeti or the Rode NT-USB. I doubt it'd have made any difference.

Right now the mic is sat on my desk so I have to be careful not to bash the desk too much when recording. I'll probably buy an arm at some point but this works for now.

I'm currently using the free version of Zoom to record audio, it lets me record a separate audio track per participant which gets handy in editing. There's a shit load of options here, but it's hard to argue with free. Particularly when it's a ubiquitous tool that guests are likely to be comfortable with.

An added side bonus is my audio now sounds great on work calls, so I guess that's a positive side effect to buying this thing? 🤷‍♂️


## Editing

I fucking hate audio editing. It's tedious as shit, and I suck at it. Fortunately I discovered [Descript](https://www.descript.com/podcasting) via their [rad product video](https://www.youtube.com/watch?v=Bl9wqNe5J8U) and it's an absolute life-saver. It automatically transcribes the recordings and lets me edit the audio by manipulating the transcript (ie deleting a word to delete that word in the recording). $30 a month is *not cheap* but it's fucking great and I'd rather pay these guys than give Adobe any more money.

The fact that I get a transcript is icing on the cake.

I bought a $9 jingle from Envato to act as an opening track. I've not got much more to say on that front. It does the job.


## Hosting

Okay so now I've recorded and edited a podcast. I need to put it online and distribute it.

I'm still not 100% on this one. After looking at a bunch of options I narrowed it to wanting this feature-set:

* Cheap[^2], ideally under a tenner a month
* Allows me to upload 80+ MB recordings (ie an hour of audio)
* decent embeddable player I can use on my own site
* Easy UI I can use to sync the feed to Spotify/Apple/whatever

Turns out the first two don't tend to play well together, most cheap or free options have fairly limited options when it comes to the size of the files they'll host. [Pinecast](https://www.pinecast.com/) looked great but their embedded player looks like shit and functions even worse. [Captivate](https://www.captivate.fm/) looks great but costs £19 per month. Fuck that.

Eventually I found [RedCircle](https://redcircle.com/), it costs £0, lets me upload files up to 200MB and has a decent audio player. Sold.

Hah, yeah. Not so fast. Turns out they embed Google Analytics and Facebook tracking in their player without consent. I complained so now they tell people they do this but they've not removed the tracking yet. This pissed me off.

I'm still on RedCircle, but I'm using a simple `<audio>` tag on my site to embed the audio at the moment which is pretty naff.

*Why the fuck do companies think it's okay to track visitors to my site without my or my visitor's consent?*

## Marketing

I built a [super simple site](https://www.mql.fm/) using Jekyll, it's hosted for free on [Netlify](https://www.netlify.com/).

I don't have any tracking on the website. [Fuck that](https://www.jacquescorbytuech.com/writing/marketers-addicted-bad-data).

The transcripts I get out of Descript are ace as I can use them for posts on the site, which is great for SEO and accessibility friendly. An hour of audio seems to be working out to about ~11k words. That's quite a lot. Another reason to be thankful for Descript I guess.

I've got a form on the site that's slowly collecting email addresses, I've not yet plugged it into an ESP but there are a few options I might use. I currently use [ConvertKit](https://convertkit.com/) for this website so I'll probably use that again. It's okay.

I've posted on [social](https://www.linkedin.com/posts/marketingops_talking-strategy-with-jenna-tiffany-activity-6740207867195916288-oZQx) [media](https://twitter.com/iamacyborg/status/1337337195208847362) when a new episode goes live.

RedCircle makes it easy to distribute the podcast to platforms like Spotify and Apple Podcasts so I made sure I'm doing that to try capture some earballs that way.

It doesn't need to be any more complicated than that for a project like this.

## Cost Breakdown

The mic cost me £159.95, the optional pop filter cost me an extra £26.48.

I'm paying nothing for Zoom, it lets me record multi-track audio and have hour+ long calls with a single guest for free.

Descript runs at $30 per month but I can do a big chunk of editing in a couple months, switch off the sub then turn it back on when I've got 2+ ready to edit.

The website is using open source software and is hosted for free.

Marketing costs are currently £0. That might go up if the email list grows but that won't be for a little while yet.

## Conclusion

Setting this up was surprisingly easy once I stopped overthinking decisions like hosting or what kind of mic to use. There's piles and piles of articles everywhere that get into as much geeky detail into every aspect of this thing that you could want, but you only need a surface level of understanding to get started.

People I've reached out to have been open to appearing on the podcast which has been ace and it's proven to be a great way to have chats with really fucking smart people that I wouldn't normally get the opportunity to speak with.

For that last point alone it's been worth it.

Do me a favour? Give [an episode a listen](https://www.mql.fm/) and <a href="mailto:jacquescorbytuech@gmail.com">shoot me an email</a> to let me know what you think?


[^1]: Famous last words...
[^2]: I don't want to spend a ton of money on what might just be a short flight of fancy.