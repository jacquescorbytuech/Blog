Title: An Email Marketer's Take on Apple Mail Privacy Protection
Slug: email-marketers-take-apple-mail-privacy-protection
Date: 2021-06-10 17:56

At their WWDC21 event on Monday, Apple announced a host of new privacy changes coming to iOS15, not least of which is [Mail Privacy Protection](https://developer.apple.com/videos/play/wwdc2021-10085/?time=708), billed as a way to protect privacy for users reading their emails.

> In order to make email rich and engaging, emails often contain remotely-hosted images. When a mail program displays one of those emails, remote images are fetched, revealing when, roughly where, and on what kind of device the mail was opened. Many marketing emails now include unique image URLs for each user, or even invisible pixels, specifically to link this information to people when they read their messages. This resulted in people choosing between text-only emails to preserve privacy, or rendering emails with full content, but revealing mail activity. In iOS 15, we're introducing Mail Privacy Protection. People can choose to have iOS privately load remote message content, hiding their mail activity. This is really cool! And it's great news for you. More people will read your emails, with all the images and visuals you included.

In the past, I've written about the [legal issues](https://www.jacquescorbytuech.com/writing/gdpr-email-tracking) I see surrounding open tracking. I've also spoken about the issue on the excellent [EmailTalk podcast](https://www.emailtalk.fm/episodes/06-privacy-round-table-w-dylan-smith-jacques-corby-tuech-jay-oram) alongside some great email marketers.

Unfortunately, nothing's changed since.

As an industry, we've failed to do the right thing. And now, well, Apple are forcing the issue for us. Understandably, many aren't happy about this. We *need* that data, don't we?

There's been an outpouring of opinion and think pieces from folks in the email industry since Monday, including these particular highlights from [Justine Jordan](https://docs.google.com/document/d/1sSaXryabL5zqQorDncmgC_o7wcEwvkkbDiXp2gd2EHk/edit) and [Laura Atkins](https://wordtothewise.com/2021/06/about-the-apple-thing/). They're both worth reading as they expose several issues from a broader marketing and deliverability perspective. Particularly the overreliance of email marketers on weak signals (opens).

Others are predicting the [apocalypse](https://www.theverge.com/2021/6/8/22525195/apple-mail-protection-privacy-pixel-tracking-newsletters-substack), it's not an opinion I share but I mention it for the sake of balance.


What MPP means for Apple Mail users is the following:

* The sender will not know whether you opened an email or not
* The sender will not know how many times you opened the email
* The sender will not know where you are when you opened the email (based on IP address)
* The sender will not know what device you are opening the email on

These are all inarguably good things from a privacy point of view. I wish Apple would go further and block click tracking outright too, but I suspect that's rather more complex.

From a sender perspective this will happen:

* You won't have accurate open reporting for MPP protected recipients
* You won't know when a recipient opened an email
* You won't know where the recipient is who opened the email
* You won't know what device the recipient is using to read their email

Given Apple Mail's 45% market share[^1] this quickly puts open data into the not-worth-looking-at category. We will have to adapt our email programs to look at harder to measure signals.

What Apple are doing here with MPP isn't radical, if anything it's an extension to the [image caching gmail rolled out](https://gmail.googleblog.com/2013/12/images-now-showing.html) way back in 2013. At the time, many thought that'd be the end for tracking opens, but that turned out not to be the case.

What's going to be interesting to see is who else follows Apple in rolling this out. I would be shocked if Google didn't introduce something similar in the very near future. It's a no-brainer way for them to score some pro-privacy points without any effect on their core advertising business.

On that front, I think we're about to see the inbox get radically shaken up.

Last year, Verizon announced their new [View Time Optimization](https://blog.postmaster.verizonmedia.com/post/616023179026202624/increasing-relevance-performance-through-vto) product, allowing marketers to get their email directly in front of a subscriber right as they're interacting with the inbox. With send time optimisation[^2] effectively becoming worthless in a post-MPP world I think we'll soon see similar commercial offerings get rolled out by Google and Microsoft for their own email inbox products. I don't think this is a good thing, but there's too much money to be made here for it to not become *a thing*.

From a recipient perspective, I like this. *I don't want to be tracked by marketers without my express consent*. And marketers is a best case scenario here, there are plenty of nefarious use cases for email tracking. More privacy in email is a *good thing*.

I hope this provides the shakeup the email marketing industry sorely needs.

[^1]: According to [Litmus](https://emailclientmarketshare.com/).
[^2]: Send Time Optimisation typically works by sending emails based on when the recipient has historically engaged with past emails. If you always open emails at 9am, you'll be sent them at 9am. 