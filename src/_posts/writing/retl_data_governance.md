---
title: Don't Throw Data Governance Out With the Bathwater
permalink: writing/retl-cdp-data-activation-governance/
date: 2022-04-23
---

A post by the folks over at Hightouch[^hightouch] caught my eye yesterday.

In it, they argue that the [Customer Data Platform is dead](https://hightouch.io/blog/cdps-are-dead/)[^cdp].

> Customer Data Platforms (CDPs) as we know them are fundamentally broken. In the next few years, every CDP vendor (Segment, mParticle, Treasure Data, etc.) will either pivot their offering to an unbundled, warehouse-first offering or completely lose relevance in the market.

It's an interesting premise, and one that I think is worth exploring.[^apps]

CDP's are platforms that fulfil a few key functions in an operational data stack. Firstly, they facilitate data collection through tracking scripts, while helping to resolve and unify customer identity. Secondly, they allow data to be activated, that is sent from one tool to another. For example you can send an `Order Placed` event to your email marketing platform, allowing you to send an order confirmation email to the customer. Thirdly, they provide some degree of data transformation and calculation, allowing you to create custom calculated traits on customer profiles that can then be activated and sent to external tools, for example, the total number of pages a customer has viewed in the last 7 days can be sent to your CRM.

These, as they propose, are all things that are ripe to be replaced through more specialised tools, I won't go into the specifics as there are literally hundreds of players in the space, but one could easily unbundle a CDP if these three components are all you care about.

But there's more to it than that. 

Almost four years ago, the [GDPR](https://en.wikipedia.org/wiki/General_Data_Protection_Regulation) came into effect, a month later, [CCPA](https://en.wikipedia.org/wiki/California_Consumer_Privacy_Act) followed. Organisations that use data have a legal obligation to collect and use data in a manner that is compliant with the law.

CDP's understand this and they provide tools[^privacy] to their customers to ensure that there are layers of data governance at the user and destination level.

Unfortunately, the same cannot be said for rETL vendors. This problem is particularly jarring given that they are starting to position themselves as tools for non-technical users through [Hightouch Audiences](https://hightouch.io/audiences/) and [Census Segments](https://www.getcensus.com/segments).

This isn't an impossible problem for them to solve, but it's painful to see a data vendor ignoring this critical aspect of data governance. And look, I get it, you're a hot startup that's received giant globs of VC money and now you need to make good on it, but please, *do better*.

Allowing a free-for-all with customer's personal data will not end well for anyone.



[^hightouch]: Hightouch are a reverse ETL (rETL) vendor, they allow data to be sent from a data warehouse to an external application
[^cdp]: In this case, Customer Data Platform meaning tools like [Segment](https://segment.com/), [mParticle](https://www.mparticle.com/) and [Tealium](https://tealium.com/)
[^apps]: If I were an rETL vendor I'd be more concerned about the rise of [apps built directly on top of the warehouse](https://benn.substack.com/p/the-data-app-store)...
[^privacy]: Examples from [Segment](https://segment.com/docs/privacy/portal/), [mParticle](https://docs.mparticle.com/guides/data-privacy-controls/) and [Tealium](https://community.tealiumiq.com/t5/iQ-Tag-Management/Consent-Preferences-Manager/ta-p/22715)
