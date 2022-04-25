# The Look of Hate on Reddit

---
## Introduction
The goal of this project is to investigate details of hateful language on Reddit with an emphasis on gender. We wanted to know what does this language looks like--which terms are popular?--and whether it has a gender imbalance--is it more prevalent in comments that contain reference to female pronouns as opposed to comments that male pronouns?

We started by deciding on a definition of hate. 

--
`Ruth`
I think you would like to take this on and explain your research, correct?
Here, we're limited to discussing **our definition* of hate. 
__
## Method
Below are the steps we followed to complete the project

--
#### Hate definition research
`Ruth, would you like to work on this? let me know if you don't have time`

The initial portion of the work involved understanding academic definitions of hate. From that research, we obtained the classifier used to label comments as either hateful, offensive or neither. We also obtained a list of terms found in hateful speech. 
The list `hate_terms` was then used to retrieve data from Reddit's API. 

#### Data acquisition
The criteria for our data acquisition, then, was to scrape all comments created in January 2022 so long as they contain at least one of the terms in the hate_terms list.
There are different levels of moderation on Reddit, so to avoid working with survival data, we used data archived by Pushshift. Pushshift tends to retrieve Reddit data immediately after creation, which atenuates our risk of missing removed comments. 

One consequence of Pushshift's promptness is that some metrics, such as score and controversiality, have not yet accumulated data. So in addition, we also scraped some metrics for those comments in March 2022.
In addition to the comments, we scraped the original submission for each comment, and the user who created each submission. Both of these were scraped directly from Reddit's API.

Yet another data we acquired was a reference dataset. Given the overly imbalanced gender distribution of our primary dataset, we wanted to compare distribution of our comments.csv with the gender distribution of all Reddit. Since we cannot scrape comments at random, we opted to retrieve the first 70 comments created every hour of every day in January 2022 without filtering for terms. The result was a raw dataset containing 52000+ comments, which approximates to one quarter of our primary dataset.

#### Data processing
Reddit is infamous for having copious amounts of spam. We acknowledge that spams, especially for sexually oriented subreddits, may contain hateful/toxic language, but given its abundance, spams would have overwhelmed our analysis and skewed results. So we opted for a simple strategy. We dropped duplicate comments, comments made by bots, and comments from the most prolific spammer--7000+ comments containing links to the same porn subreddit.

Additional data processing:
* Date conversion from unix
* Gender classification
* Detoxify classification
* Filter out comments in foreign languages 

--
#### Research Questions
`Ruth please feel free to briefly discuss our RQs here.`

--
#### Sample of analysis result
`Ruth, please feel free to briefly discuss our RQs here.`

## Reproducibility

This project is still in development so some things will be simplified and refined in the near future.<br/>
To reproduce this project from beginning to end, please follow the steps below.

**Data acquisition and preparation**
1. Get reddit credentials and fill in `reddit_auth.py`
2. Run `scraper.ipynb`
3. Run classifiers inside `classification/`
4. Run `processing.ipynb`

**Data analysis**

5. Run RQ notebooks inside `data_analysis/`

**Communicating results**

6. Run `visualizations.ipynb`

___
#### Statement of work:
(names are in random order)

* Research questions: Ruth, with input from Mel
* Research (includes development of hate and gender terms to use in classification): Ruth, with input from Mel and Christian
* Scraper research and exploration: Mel, Christian, and Ruth
* Scraper coding and data acquisition: Mel
* Data preparation and data governance: Mel
* Classifiers: Christian, Ruth
* Analyses: Christian, Ruth, with input from Mel (RQs 3, 6.1)
* GitHub README: Mel, Christian, Ruth
* Github management: Mel
* Blog article: Ruth
* Visualizations for publication: Mel
* Publishing: Mel
* Liaison with instructors: Ruth
