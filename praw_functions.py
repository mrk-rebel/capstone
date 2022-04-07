

import reddit_auth
import praw
import numpy as np
import time

def update_log(epoch):
    '''
    takes in current epoch,
    loads log_df from local folder,
    appends it with current time (for better control), and
        epoch in which scraper reached limit, and
    saves the file in local folder
    '''
    log = pd.read_csv('log.csv')
    log = log.append({
        'time': time.time(),
        'epoch': epoch
    }, ignore_index=True)

    log.to_csv('log.csv', index=False)


def get_submissions_data(c):
    '''
    takes in a df with unique submissions_id, and 
    scrapes live data on each submission using praw

    outputs df with retrieved data
    '''     
    reddit = praw.Reddit(
        client_id=reddit_auth.client_id,
        client_secret=reddit_auth.client_secret,
        user_agent=reddit_auth.user_agent, 
        password=reddit_auth.password,
        username=reddit_auth.username
    )

    submissions_data = defaultdict(list)
    for submission_id in tqdm(c):
        submission = reddit.submission(reddit.submission(submission_id))
        try: 
            submissions_data['created_utc'].append(submission.created_utc)
            submissions_data['author'].append(submission.author)
            submissions_data['edited'].append(submission.edited)
            submissions_data['id'].append(submission.id)
            submissions_data['is_created_from_ads_ui'].append(submission.is_created_from_ads_ui)
            submissions_data['is_original_content'].append(submission.is_original_content)
            submissions_data['is_self'].append(submission.is_self)
            submissions_data['is_video'].append(submission.is_video)
            submissions_data['media_only'].append(submission.media_only)
            submissions_data['num_comments'].append(submission.num_comments)
            submissions_data['over_18'].append(submission.over_18)
            submissions_data['quarantine'].append(submission.quarantine)
            submissions_data['score'].append(submission.score)
            submissions_data['selftext'].append(submission.selftext)
            submissions_data['stickied'].append(submission.stickied)
            submissions_data['subreddit'].append(submission.subreddit)
            submissions_data['subreddit_subscribers'].append(submission.subreddit_subscribers)
            submissions_data['title'].append(submission.title)
            submissions_data['total_awards_received'].append(submission.total_awards_received)
            submissions_data['upvote_ratio'].append(submission.upvote_ratio)
            submissions_data['url'].append(submission.url)
            
        except:
            submissions_data['created_utc'].append(np.nan)
            submissions_data['author'].append(np.nan)
            submissions_data['distinguished'].append(np.nan)
            submissions_data['edited'].append(np.nan)
            submissions_data['id'].append(submission.id)
            submissions_data['is_created_from_ads_ui'].append(np.nan)
            submissions_data['is_original_content'].append(np.nan)
            submissions_data['is_self'].append(np.nan)
            submissions_data['is_video'].append(np.nan)
            submissions_data['media_only'].append(np.nan)
            submissions_data['num_comments'].append(np.nan)
            submissions_data['over_18'].append(np.nan)
            submissions_data['quarantine'].append(np.nan)
            submissions_data['removal_reason'].append(np.nan)
            submissions_data['score'].append(np.nan)
            submissions_data['selftext'].append(np.nan)
            submissions_data['stickied'].append(np.nan)
            submissions_data['subreddit'].append(np.nan)
            submissions_data['subreddit_subscribers'].append(np.nan)
            submissions_data['title'].append(np.nan)
            submissions_data['total_awards_received'].append(np.nan)
            submissions_data['upvote_ratio'].append(np.nan)
            submissions_data['url'].append(np.nan)
            continue

        try:
            submissions_data['distinguished'].append(submission.distinguished)
        except:
            submissions_data['distinguished'].append(submission.np.nan)
        try:
            submissions_data['removal_reason'].append(submission.removal_reason)
        except:
            submissions_data['removal_reason'].append(submission.np.nan)


    df = pd.DataFrame(submissions_data)

    return df



def get_users_data(c):
    '''
    takes in a df with unique user_id, and 
    scrapes live data on each user via praw

    outputs df with retrieved data
    ''' 
    
    r = praw.Reddit(
        client_id=reddit_auth.client_id,
        client_secret=reddit_auth.client_secret,
        user_agent=reddit_auth.user_agent, 
        password=reddit_auth.password,
        username=reddit_auth.username
    )

    users_data = defaultdict(list)
    for author in tqdm(c):
        user = r.redditor(author)
        users_data['name'].append(author) 

        try:
            users_data['id'].append(user.id)
        except:
            users_data['id'].append(np.nan)
        
        try: 
            users_data['created_utc'].append(user.created_utc)
        except:
            users_data['created_utc'].append(np.nan)
        
        try:
            users_data['comment_karma'].append(user.comment_karma)
        except:
            users_data['comment_karma'].append(np.nan)

        try:
            users_data['link_karma'].append(user.link_karma)
        except:
            users_data['link_karma'].append(np.nan)

        try:
            users_data['total_karma'].append(user.total_karma)
        except:
            users_data['total_karma'].append(np.nan)
        
        try:
            users_data['has_verified_email'].append(user.has_verified_email)
        except:
            users_data['has_verified_email'].append(np.nan)

        try:
            users_data['is_mod'].append(user.is_mod)
        except:
            users_data['is_mod'].append(np.nan)

        try:
            users_data['is_gold'].append(user.is_gold)
        except:
            users_data['is_gold'].append(np.nan)

        try:
            users_data['trophies'].append(user.trophies())
        except:
            users_data['trophies'].append(np.nan)

        try:
            users_data['subreddit'].append(user.subreddit)
        except:
            users_data['subreddit'].append(np.nan)

        try:
            users_data['subreddit_over_18'].append(user.subreddit.over_18)
        except:
            users_data['subreddit_over_18'].append(np.nan)

    df = pd.DataFrame(users_data)

    return df



def update_comments(c):
    '''
    takes in a df with unique comment_id, and 
    scrapes live up to date data for each comment via praw

    outputs df with retrieved data
    ''' 
    
    reddit = praw.Reddit(
        client_id=reddit_auth.client_id,
        client_secret=reddit_auth.client_secret,
        user_agent=reddit_auth.user_agent, 
        password=reddit_auth.password,
        username=reddit_auth.username
    )

    time_now = round(time.time())
    comments_new = defaultdict(list)

    for comment_id in tqdm(c):
        comments_new['id'].append(comment_id)
        com = reddit.comment(comment_id)
        try:
            comments_new['score'].append(com.score)
            comments_new['edited'].append(com.edited)
            comments_new['all_awardings'].append(com.all_awardings)
            comments_new['gildings'].append(com.gildings)
            comments_new['controversiality'].append(com.controversiality)
            comments_new['status'].append(time_now)

        except:
            comments_new['score'].append(np.nan)
            comments_new['edited'].append(np.nan)
            comments_new['all_awardings'].append(np.nan)
            comments_new['gildings'].append(np.nan)
            comments_new['controversiality'].append(np.nan)
            comments_new['status'].append('ndr')

    df = pd.DataFrame(comments_new)

    return df