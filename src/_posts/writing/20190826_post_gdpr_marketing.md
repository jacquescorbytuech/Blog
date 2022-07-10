Title: Digital Marketing in the Age of the GDPR
Slug: digital-marketing-post-gdpr
Date: 2019-08-26 19:44
Summary: Houston, we have a problem.

*What does marketing look like in post GDPR world where everyone is compliant?*

Last June, to the surprise of many, [a Tweet](https://twitter.com/adam_rose/status/1140151337834962944) was widely shared online, showing the ICO admitting that their own cookie policy "doesn't meet the required GDPR standard".

In early July, this was followed up with [new guidance on cookie usage](https://ico.org.uk/for-organisations/guide-to-pecr/guidance-on-the-use-of-cookies-and-similar-technologies/) that clearly exposes the way the industry has been mistreating customer data, and the ways we need to change.

## Digital Marketing Today

First, let's take a look at some ways digital marketers collect data:

* ### Form Submission  
  Unsurprisingly, data collected when a user submits a form is often used in marketing, for example an email address collected via a form will typically be sent marketing emails, or shared with Facebook to receive targeted advertising. It is not always explicitly explained at the point of form submission what data will be used for what and where the collected data may end up being sent to.

* ### Cookies  
  <ol>
  <li>**Analytics**  
  Sites will typically use a cookie-based analytics tool, such as Google Analytics to identify how individuals use a website. This allows them to see precisely what pages an individual has visited, what elements of the website they've interacted with, what devices they're using to access the site, where they're physically located (via IP), etc. Typically, this information is collected by third party services such as Google or Adobe.</li><br/>
<li>**Personalisation**  
  These cookies are used to collect precise behavioural information about a unique individual. For example, knowing what someone has added to their shopping basket on an ecommerce site, or keeping track of what pages someone has looked at to build up a personalised behavioural profile to later target them with more direct product messaging. These cookies can be first or third party, meaning that information is often sent off to opaque third party services that provide some form of personalisation engine to the business.</li><br/>
<li>**Retargeting**  
  Cookies like Facebook or Google Doubleclick (amongst others) collect information on an individual's website visit for the purpose of later identifying that individual across multiple separate websites which allows the cookie owner to build up a large data profile on the individual. Examples of the type of information collected are<sup>1</sup>:<ul>
  <li>Age</li>
  <li>Gender</li>
  <li>Location</li>
  <li>Interests</li>
  <li>Behaviour on your website</li>
  <li>Behaviour on search engines</li>
  <li>Behaviour on social media</li></ul>  
  This data collection happens in the background of most websites and tends to be incredibly opaque as to how and what data is collected specifically and where it is sent to.</li><br/>
<li>**Advertising**  
  Due to the way advertising works online, a publisher (a site or app running adverts) typically uses an auction system to determine which adverts to display to an individual user. This auction system involves sending data back and forth from the website to numerous online advertising exchanges to determine which specific advert should be shown.<br/><br/>It should therefore come as no surprise that this process allows advertisers to create highly specific profiles of individuals and their behaviour online as they collect data through this auction mechanism.</li></ol>

* ### Telemetry  
  When you use applications on your desktop,mobile or on the web, information about your specific interactions with the product may be recorded and sent directly to the product developer, for example to understand what specifically you have interacted with. [Microsoft calls this data a "gold mine"](https://blogs.windows.com/windowsdeveloper/2014/03/20/instrumenting-your-app-for-telemetry-and-analytics/).

* ### Email Tracking  
  When you receive a marketing email from a company, the email will contain tracking pixels telling the sender when (and often where and with what device) you open the email. They also contain tracking links allowing them to know specifically what an individual has clicked on in a received email. Furthermore the email may also contain additional third party tracking which function like the retargeting and advertising cookies mentioned above.

* ### Data brokerage  
  Companies like Experian and Equifax allow others to purchase personal information about you so that they can then target you for marketing. This frequently occurs without your knowledge or consent.

*This is by no means an exhaustive list and brands and marketers continue to innovate in the ways in which they can acquire your data without your express knowledge or consent.*

Taken in combination, you can see how a business can quickly start to build an incredibly detailed view of an individual, how they can start to access that data directly as a first party or even start to target individuals through data held by third parties, such as when running advertising campaigns.

Ostensibly, marketers like to tell themselves that this is all above board – data is collected usually but not always for specific purposes and this data provides value to the business and hopefully (we like to tell ourselves) to the individual. The problem is in the opaqueness of the processes involved and the lack of consent or even knowledge by the end-user about the scope of the data collection taking place

## So what are we doing with all this data?

* ### Programmatic Advertising  
  Advertising based on individual user profiles and website placement. Look at any news website or your Instagram feed and you'll see this in action.

* ### Retargeting  
  Similar to programmatic but based explicitly on targeting people who've performed a specific action that has been tracked, such as looking at a particular product.

* ### Targeted Advertising  
  Sending email addresses or phone numbers to Google or Facebook so that individuals can be specifically targeted or lookalike audiences can be built based on a specific subset of customers provided by email address or phone number.

* ### Email Marketing  
  Sending emails to individuals to get them to perform a specific action, such as signing up to your product or purchasing your latest widget.

* ### SMS  
  Similar to email, but via SMS. For example informing your customers of a sale or for shorter and more actionable messaging.

* ### Push notifications  
  Like email but frequently based on more specific actions having occurred in an app, for example someone responding to a message you posted on social media or an action taking place in a mobile game. 

* ### Optimisation  
  We look at data collected from telemetry and various cookies to optimise our products and our sales funnels

* ### Nothing at all  
  Sometimes businesses collect  data and just let it sit in a database without doing anything with it, go figure 🤷‍♂️


*This is by no means an exhaustive list and is merely used to demonstrate some common scenarios in which data is used for marketing.*

We'd all like to think all this data is being handled carefully and responsibly, but ask any marketer and they'll have stories to tell about customer data being shared across the company through CSV files or the business CRM, without any oversight or mechanism to protect an individual's private information.

## So where does that leave us?

Thanks to this new guidance, some things have become abundantly clear:

* You cannot rely on implied consent to use cookies
* Analytics cookies require consent
* Legitimate Interests cannot be used as a reason for processing analytics or advertising cookies

This is a **BIG** deal. Websites currently assume you consent to cookies until you tell them otherwise and will gleefully suck up as much data as they can collect until you stop them. This new guidance makes it explicitly clear that this is no longer allowed and that a business *must* obtain consent before they engage in these activities.

### Analytics
Dead. Switch to a log-based analytics system and strip out PII. You might be able to obtain consent for your analytics cookies but hey, who am I kidding, we've trained people to hit the big ❌ button on popups so they'll close your popup immediately without giving you consent.

### Programmatic advertising
You'll still be able to target people based on the website you wish to place an advert on, but advertising brokers will no longer have monolithic profiles of profiles you can target based on interests, demographics, etc. This is a big loss for businesses and a *HUGE* win for individual privacy.

### Retargeting
Dead. Deader than dead. Good luck obtaining consent when you have to explain to your users that you want to stalk them around the web for products they spent all of 3 seconds looking at on your site. Good fucking riddance.

### Targeted Advertising
Dead. No one will want to give you consent to send off their personal data to third parties. Advertisers will also struggle to obtain interest and demographic data making lookalike audiences much less valuable.
 
### Email
[Legitimate interest isn't good enough](https://www.jacquescorbytuech.com/writing/gdpr-email-tracking.html), you need to obtain consent for marketing emails<sup>2</sup> and unless you have explicitly collected consent for tracking you cannot track how individuals behave within your emails.

### SMS
Like email, you're going to need to collect consent to use SMS for marketing. There's some real opportunties to demonstrate the value of SMS to customers here, you'll just have to think creatively.

### Push Notifications
You'll need consent, but you already needed that. Push notifications are probably going to suffer the least because there have been solid mechanisms in place for years to prevent misuse from marketers.

### Social
Do you *really* want to be paying Facebook or YouTube given what they're up to?

## What happens next?

The big winners are going to be the channels which can most clearly communicate an obvious value exchange between the individual customer and the business. Unsurprisingly, given what I do, I think these are channels like email, SMS and push notifications. Once you've built an existing relationship with an individual, they are more likely to see the benefit in giving you permission to  message them via these channels.

Advertising(⚰️) in all forms is the clear loser - this new cookie guidance effectively put the nail in the coffin of digital advertising as we know it. You'll no longer be able to target individuals based on what pages of your website they've visited or their interests, geographical location or demographic data. [DuckDuckGo already demonstrates](https://help.duckduckgo.com/duckduckgo-help-pages/company/advertising-and-affiliates/) how we can move towards a more compliant and a more ethical take on advertising. Budgets will inevitable suffer as performance decreases across digital advertising channels.

Customer acquisition optimisation is going to suffer. Without clear analytics across the board we'll have to do a lot more work done to understand how individual campaigns have performed. There are plenty of ways we can do this, for example having personalised landing pages per campaign and measuring the aggregate number of visits to that page (ie without PII to identify unique visits) vs the number of purchases or form submissions. I think we'll see more investment in this area as gauging the effectiveness of our marketing spend becomes increasingly challenging.

Marketers are going to have to adapt to these changes and we're going to have to take a very close look at how permission is currently obtained in mobile apps. It's clear that they're leading the way in this area and understand that progressively obtaining permission (consent, in our case) based on specific interactions (for example, asking for camera permissions when the app user wishes to take a photo in the app) is the way we're going to have to go.

To this purpose it behoves all of us in marketing to propose a new framework for ethical marketing and more purposeful and transparent data collection. It is a position of extreme arrogance on the behalf of marketers and businesses to believe that our bottom line is more important than an individual's privacy. What the EU has achieved with the GDPR is making it clear that this is absolutely not the case.

**In an age in which marketing data is used to enable electoral fraud and strip our civil liberties, we need to do better.**

<br>
<br>
****
<br>

#### Notes and References

1. [Taken from TargetInternet](https://www.targetinternet.com/digital-marketing-guide-to-cookies/)
2. there are of course other types of email and reasons other than marketing to send emails which I won't cover here

