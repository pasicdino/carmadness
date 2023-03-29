# Car Madness
## Video link:
https://youtu.be/_6HhcDN6AKk
## File explanation
In the notebook file data_scraping the script can be found which was used to scrape the car listings from marktplaats

In the notebook file data_preproc, the preprocessing steps that were taken before exploring the data can be found. 
This ranges from translating strings of numbers into their values, to adding columns that will be important later on. 

In the notebook file EDA, the exploratory data analysis and the regression model can be found.

All data files, both raw, cleaned, and third party, can be found in the data folder.

## Important information
Most important things are discussed in the notebook files themselves, but some things will be mentioned here too.

When scraping the data from marktplaats, the intention was to seperate private and dealer listings. In practice,
many private listings were in fact dealers, and there was even overlap in both sets. I'm not sure if this is because 
dealers were listing under the private filter, or whether marktplaats' filtering is not working well, but we decided to 
make it one large dataset and discarded the research question related to this topic.

We added three columns to the dataset, province, make, and model. Province was added using an external dataset
(https://metatopos.dijkewijk.nl/metatopos-places.json), and make and model were added in a similar fashion 
(https://gist.github.com/OdeToCode/582e9c044eee5882d54a6e5997c0be52, https://parseapi.back4app.com/classes/Car_Model_List?limit=100000&keys=Model), however, 
the make and model information was automatically extracted from the title, meaning there could be inaccuracies. 

A small sample was manually reviewed,
but it is not necessarily 100% accurate. Moreover, the car make and model list were manually edited as to include more 
makes and models which were frequent in the dataset but not in the model. The files in the data folder are all final, 
including our own additions.

## Ethical Analysis, Bias, and weaknesses of the project

While scraping the data from marktplaats.nl, we got denied access after about 50 requests. As a consequence of this, we were limited by the amount of listings we could scrape per day. This is likely implemented by marktplaats on purpose to either protect from potential DDOS attacks, or perhaps even to prevent people from scraping their data.

Why would marktplaats not want their data scraped? Most listings are made by actual people, and to list something, you must be logged in. If you were to scrape one person's listings, and keep track of those, you could learn things about that person, especially since people have their town linked too. Realistically, this is not a big issue, as one could also just look at someones profile and look at their listings. Also, in this implementation, the scraped data is shared with no one, and the data is not used in a harmful way. We do scrape the sellers name, but this was only used to filter out companies. It could be deleted now, and would likely be smart, when looking at the ethical side of things.

The second ethical consideration is part of the regression model. If we were to deploy the model and have people use it to hint them toward the price they should sell their car for, would the developers be held accountable for inaccurate predictions? Of course, the model could underprice someone's vehicle, and if they were reckless and would not research the price further, they could lose a large amount of money.

If a deployment were to be made, clear terms and conditions would need to be specified, and it should be made clear to the user that the price is merely an indication.

A form of bias in the model is that people often list their vehicles for more money than they are worth, which leaves room for negotiation between the seller and the buyer.
If someone were to check what a fair price would be for a specific vehicle, they must realize that the prices that the model
was trained on are likely biased in the sellers favour, as we only look at listings, not actual sales.

During COVID and the global chip shortage have seen second hand vehicles prices increase vastly, in order to make the model 
future-proof, it would have to be retrained periodically on current prices to follow the market.


## Questions?
Please send an e-mail to d.pasic@student.maastrichtuniversity.nl