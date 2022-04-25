# The Look of Hate on Reddit

---
## Introduction
The goal of this project is to investigate details of hateful language on Reddit with an emphasis on gender. We wanted to know: what does this language looks like? Which terms are popular? Whether it has a gender imbalance--is it more prevalent in comments with references to female identifiers as opposed to comments with male identifiers?
__
## Method
Below are the steps we followed to complete the project

--
#### Hate definition research
The initial portion of the work involved understanding academic definitions of hate. There is not a definitive agreement about what constitutes hate speech or where the boundary exists between hate speech and offensive language. Different people will have different judgments. From this research, we obtained the classifier used to label comments as either hateful, offensive or neither (Davidson, Warmsley, Macy, & Weber, 2017). Part of this research was to developed a list of terms found in hateful speech, which was also largely from Davidson and colleagues (2017), but was ammended with terms from other research. 
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
* Classification into Davidson label categories (hate/offensive/neither) (Davidson, Warmsley, Macy, & Weber, 2017)
* Gender classification (using lists of gender identifiers that we researched and developed)
* Detoxify classification
* Filter out comments in foreign languages 

--
#### Research Questions
We developed numerous research questions -- and the number grew as the project progressed. We did not tackle all of them for this first phase of the project. The research questions are in ResearchQuestions.pdf. This document includes some project information as well as research questions, operationalized versions of the questions, some notes on statistical methods, and hypotheses.

In this phase of the project we addressed research questions 1-9, 11, and 15 - 17.

Each notebook is named using the research question numbers. If multiple questions are analyzed in one notebook, an underscore separates the question numbers. For example, Q11_15.ipynb examines research questions 11 and 15. The notebooks include the research question, operationalized question, hypothesis, and a brief description of the results in a section above the coding for each question. Visualizations are included amid the coding.

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
#### Statement of work
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

___
#### References Consulted

These sources were instrumental in developing our theoretical and practical approaches to this project. Not all of them are directly related to information included in the project article or github readme, but all contributed in some way to how we 

Appiah, K.A. (2022, April 5). Can I utter a racial slur in my classroom? The New York Times Magazine, https://www.nytimes.com/2022/04/05/magazine/racial-slur-classroom-ethics.html?algo=clicks_norm_diversified&block=1&campaign_id=142&emc=edit_fory_20220405&fellback=true&imp_id=510752434&instance_id=57678&nl=for-you&nlid=86087734&rank=5&regi_id=86087734&req_id=348953207&segment_id=87581&surface=for-you-email-wym&user_id=b88b7a994fb6ba33067106149a1b5101&variant=0_combo_lda_channelsize5_unique_edimp_fye_step50_diversified (appears in April 10, 2022 print edition)

Burnap, P. & Williams, M.L. (2015). Cyber hate speech on Twitter: An application of machine classification and statistical modeling for policy and decision making. Policy & Internet, 223 - 242.

Caren, N. (n.d.) Using Python to see how the Times writes about men and women. http://nealcaren.github.io/text-as-data/html/times_gender.html

Chandrasekharan, E., Samory, M., Jhaver, S., Charvat, H., Bruckman, A., Lampe, C., Eisenstein, J., & Gilbert, E. (2018). The internet’s hidden rules: An empirical study of Reddit norm violations at micro, memo, and macro scales. Proceedings of the ACM on Human-Computer Interaction, 2, CSCW, article 32.

Cinelli, M., Pelicon, A., Mozetic, I., Quattrociocchi, W., Novak, P.K., & Zollo, F. (2021). Dynamics of online hate and misinformation. Nature, 11, 22083. https://doi.org/10.1038/s41598-021-01487-w

Crabb, J. (2019, May 28). Classifying hate speech: An overview. townrdsdatascience.com

Davidson, T., Warmsley, D., Macy, M., & Weber, I. (2017). Automated hate speech detection and the problem of offensive language, Proceedings of the Eleventh International AAAI Conference on Web and Social Media. aaa.org

Faal, F., Schmitt, K., Yu, J.Y. (2022, February 28). Reward modeling for mitigating toxicity in transformer-based language models. arXiv. 2022.09662v4 [cs.CL]

Fischer, S. (2020, August 20). Reddit says new policies have lowered hate speech posts by 18%. Axios, https://www.axios.com/reddit-hate-speech-policies-reduction-72fa6b6b-7774-409a-9e91-ced3b3d90d4b.html

Hamilton, W.L., Ying, R., & Leskovec, J. (2018, September 10). Inductive representation learning on large graphs. 31st Conference on Neural Information Processing Systems, arXiv: 1706.02216v4 [cs.SI]

Hanu, L. (2020, November 13). How well can we detoxify comments online? Medium.com, https://medium.com/unitary/how-well-can-we-detoxify-comments-online-bfffe5f716d7

Hemphill, L. (2017). Very fine people: What social media platforms miss about white supremacist speech. ADL, https://www.adl.org/language-of-white-supremacy

Kennedy, C.J., Bacon, G., Sahn, A., & von Vacano, C. (2020). Constructing interval variables via faceted Rasch measurement and multitask deep learning: a hate speech application. arXiv: 2009.10277v1 [cs.CL]

Kim, J.W., Guess, A., Nyhan, B., & Reifler, J. (2021). The distorting prism of social media: How self-selection and exposure to incivility fuel online comment toxicity. Journal of Communication, 71, 922-946.

Kovacs, G., Alonso, P., & Saini, R. (2021). Challenges of hate speech detection in social media. SN Computer Science, 2, 95.

Law, T.J. (2021, January 1). What is Reddit? The ultimate quickstart guide for 2021. https://www.oberlo.com/blog/what-is-reddit

Li, C. (2018). I made a news scraper with 100 lines of Python. medium.com

Livni, E. (2018, April 24). The most offensive curse word in English has powerful feminist origins. Quartz.

MacAvaney, S., Yao, H-R, Yang, E., Russell, K., Goharian, N., & Frieder, O. (2019, August 20). Hate speech detection: Challenges and solutions. PLOS ONE, https://doi.org/10.137/journal.pone.0221152

Marx, D. (2018). PSAW: Python pushshift.io API wrapper (for comment/submission search). PSAW, https://psaw.readthedocs.io/en/latest

Moriarty, M. (2018, February 9). A brief history of the c-word. The Establishment, https://theestablishment.co/a-brief-history-of-the-cunt-a755b5df4a4/index.html

Podolak, M. (2021). How to scrape large amounts of Reddit data. Medium.com

Rathje, S., Van Bavel, J.J., van der Linden, S. (2021, June 23). Out-group animosity drives engagement on social media. PNAS, https://doi.org/10.1073/pnas.2024292118

Sap, M., Card, D., Gabriel, S., Choi, Y. & Smith, N.A. (2019). The risk of racial bias in hate speech detection. Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics, 1688 - 1678.

Sivak, E. (n.d.). SICSS-HSE tutorial: Reddit as a source of data. https://sicss.io/2021/materials/hse/reddit_html
Tanner, G. (2019). Scraping Reddit data. townrdsdatascience.com

Townsend, L & Wallace, C. (n.d.) Social media research: A guide to ethics. Economic & Social Research Council. https://www.gla.ac.uk/media/Media_487729_smxx.pdf

urvismahajan (2021). Scraping Reddit data using Python. Geeksforgeeks.com, https://www.geeksforgeeks.org/scraping-reddit-using-python

Walsh, M. (2021). Reddit data collection and analysis with PSAW. https://melaniewalsh.github.io/Intro-Cultural_Analytics/04-Data-Collection/14-Reddit-Data.html

Wang, Y. & Goutte, C. (2018). Real-time change point detection using on-line topic models. Proceedings of the 27th International Conference on Computational Linguistics, 2505 - 2515.

