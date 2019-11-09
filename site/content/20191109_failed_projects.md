Title: A Long List of Failed Projects
Slug: failed-projects
Date: 2019-11-09 11:46

I've had a lot of projects fail over the years, here's a non-exhaustive list of them and some reasons why they failed

## Love Community Site
Love was an online procedurally generated video game released by Eskil Steenberg in [2010](http://www.quelsolaar.com/love/).
 
One of the modules in the second year of my Digital Arts degree was around creating online community platforms (I forget the precise name of the module), which I took entirely too literally and thus built a forum and wiki website for this game. The site was a simple vBulletin forum with a MediaWiki wiki, running on a crappy shared hosting provider.

While the community picked up quickly and I managed to do remarkably well on the SEO front for this site, ultimately the game was never a big success which led to the site slowly dying off. Thus would begin a recurring theme with online communities I've tried to build...

*Minecraft came out around the same time, maybe I should have tried to do something with that* 🤔

## Path of Exile Wiki

I first disovered Path of Exile through  Total Biscuit's [WTF is... - Path of Exile](https://www.youtube.com/watch?v=k8779Ff_qoc) video (this was before TB turned out to be a massive chud) and was instantly hooked as it reminded me so much of Diablo 2, which I'd played a ridiculous amount of.

The site [went live on September 25th 2011](https://pathofexile.gamepedia.com/index.php?title=Path_of_Exile_Wiki&oldid=1) and [quickly picked up steam within the community](https://www.pathofexile.com/forum/view-thread/9046) - I'd got the timing right and got in there before anyone else, which was pure luck.

The site soon became a victim of it's own success and as it was hosted on my crappy shared hosting provider, kept going down as the game approached the big Open Beta launch phase in early 2013. I tried to move it but database extracts kept failing because of the size of the cache tables and my hosting provider didn't seem to care to give me a hand.

It was at this moment that [Curse](https://en.wikipedia.org/wiki/Curse_LLC) swooped in and offered to buy the site out from me - the offer seemed good at the time so I signed on the dotted lined and gave up control of my baby.

That decision opened up a lot of opportunities for me, but in hindsight turned out to have probably been a mistake. The site still does millions of pageviews a month and was firmly within the top 10 for traffic within Gamepedia (Curse's wiki farm) when I last had access to stats.

I couldn't ever have predicted the scale of success that this reached but hindsight's a bitch and I do regret selling this.

[Path of Exile Wiki](https://pathofexile.gamepedia.com/Path_of_Exile_Wiki) is still live if you want to check out what it looks like now.

## Hellgate Forums

Hellgate: London  was a game [released in 2007](https://en.wikipedia.org/wiki/Hellgate:_London) that turned out to be a commercial failure.

It was, however, a ton of fun and as the studio responsible for the game was dissolved in 2008 the rights were snapped up and eventually the game was re-released in 2014 as Hellgate: Global.

I setup another Forum and Wiki combo but it was not to be - the game was heavily monetised and never picked up as well as the first iteration did.

I quickly folded the site and gave up.

## BFGA Wiki

I'm a **BIG** Warhammer nerd, so when I found out that a game was being made licensing Games Workshop's [Battlefleet Gothic](https://en.wikipedia.org/wiki/Battlefleet_Gothic) IP I lept at the chance to quickly build a wiki for it.

This was actually part of a wider project - while at Curse I'd spoken to my boss about the lack of clear community platforms for the GW videogaming community and while he wasn't enthused about the idea that didn't deter me from running with it when I left Curse. That wider project involved a large forum and news combo site built on Invision Power Board and a network of related MediaWiki sites. I couldn't get sufficient traffic to those properties so quickly killed them off, but BFGA Wiki was working, for a time.

If you're not familiar with MediaWiki, there's a fantastic extension called [Semantic: Mediawiki](https://www.semantic-mediawiki.org/wiki/Semantic_MediaWiki) which allows you to store and query data directly within your wiki pages and templates. We'd used this on the PoE Wiki and it was hugely important there so I made use of it again to be able to quickly build queryable pages to minimise duplicate work. For example, with SMW you can [create a table of specific results](https://www.semantic-mediawiki.org/wiki/Help:Inline_queries) that match a query and output specific data values into that table. In the context of a videogame site you can quickly see how this can be used to generate lists of skills, ships, etc that are then easy to keep up to date.

Ultimately this never really picked up and I burnt out on it and let the domain expire.

You can see a snapshot of this wiki on the [Wayback Machine](https://web.archive.org/web/20170426103307/http://www.bfgawiki.com/wiki/Battle_Cruiser).

## Appel du Vide

For some reason, I thought I could build a business selling made to measure shearling jackets.

I had a sample bomber jacket made on Brick Lane by the folks at [Upperclass Fashions](https://www.upperclassfashion.co.uk/) and shopped around for trims at London Trimmings in Whitechapel (they have awesome [Riri and YKK Excella zips](http://www.londontrimmings.co.uk/category.php?cat_id=32)), I also spent a lot of time looking around for shearling suppliers in the UK and finding UK based companies that could make small batch jackets.

I then built an ecommerce site on Shopify and ran some ad campaigns on Facebook and Instagram. I ended up with a few people reaching out to me who were interested and met a couple of them to show them the sample jacket and to learn more about what they were after and how I could make it for them.

I didn't have a real budget for this though and I felt way out of my depth trying to get samples made, patterns cut, etc so I ended up killing this project off before it ever had the chance to go anywhere. That sample jacket is still sitting in my wardrobe.

But hey, the domain name is still cool, I've got some future ideas for it...

## Old World Wiki

Remember how I said I was a BIG Warhammer nerd? 

This was another Warhammer community site, this time for [Total War: Warhammer](https://en.wikipedia.org/wiki/Total_War:_Warhammer), a game released by Creative Assembly in 2016.

Helpfully, the game has great mod support and as a result you can easily export the game files in usable formats. This  meant I could build a custom Drupal site that would automatically create pages based on imported CSV data, and through abundant usage of the [Views module](https://www.drupal.org/docs/8/core/modules/views/overview) I could link these files together and populate site pages, and example of which [you can see here](https://web.archive.org/web/20180124015058/http://oldworldwiki.com:80/grave-guard-0).

I'd never really been properly exposed to SQL or database joins so this project really tested me and I learn a ton.

The site was never a big success though, so I let it die off slowly.


## Rend Forums

There's a theme here...

[Rend](https://www.rendgame.com/) is an online survival game by Frostkeep Studios.

When I saw the trailer for this game I knew I had to get involved in it. I'd seen how successful similar genre games were like ARK: Survival Evolved and Rust and thought this could be an opportunity to build a community site.

I got stuck in and quickly setup a forum and wiki using IPB and MediaWiki but quickly hit a roadblock.

Curse had announced that they were the "official" wiki partner to Rend, and Frostkeep built an in-house forum.

Under those conditions I knew there was little I could do to get the site going and quickly gave up on it.

## What's Next ...?

If you've got to the bottom of this, you can probably see that there's an ongoing theme here.

I like building online gaming communities, but all but one of them have ultimately been a failure.

I think there are a few reasons for this - but the biggest one was my lack of recognition that the internet itself has changed. People no longer look to join independent forums, indeed, what's the point when you can just easily join a specific subreddit or Facebook group?

Similarly, Curse and Wikia (now Fandom) were in a huge growth phase and very quickly came to dominate the online gaming wiki world - with absolutely unbeatable SEO from their huge scale and a budget allowing them to attend conventions and make deals to host official communities with game developers and publishers.

Curse were recently bought by Fandom so this is now much worse, I'd estimate that at least 90% of English speaking videogame community wikis are owned by a single company.

Is there any future for online community builders? Yeah, maybe, but there are also huge barriers to entry that will be all but insurmountable for all but the most dedicated.

I've learnt a lot which has helped me in my professional career and have had access to opportunities that I never could have thought of had I not built these sites.

Ultimately I enjoy having side projects and don't consider any of the above to have been wasted time, despite them not getting anywhere.

**I'm now working on [something I find really exciting](https://www.inkfolio.co/), hopefully you will too.**