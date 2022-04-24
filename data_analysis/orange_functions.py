

import nltk
from nltk.tokenize import word_tokenize
nltk.download('punkt')

male_words = {'amigo','ape','apes','bastard','bastards','bear',
                'beast','beefcake','bloke','blokes','boy','boyfriend','boyfriends','boys','brah',
                'bro','brother','brothers','bruh','brute','buck','bud','buddies','buddy',
                'buds','bugger','bull','chad','chairman','chap','chum','dad','dads','dawg',
                'dick','dickhead','dickheads','dilf','dude','fag','faggot','father','father',
                'fella','fellow','fiance','fucker','gent','gent','gentleman','gentlemen',
                'grandfather','grandfathers','grandpa','grandpas','grandson','grandsons',
                'groom','grooms','guy','guys','he',"he'd","he's",'hero','him','himself',
                'his','hombre','hombres','hubby','hunk','husband','husbands','incel','incels',
                'king','kings','lad','lads','macho','machos','male','man','mankind','master','men',
                "men's",'mensch','mister','mr','muscle','nephew','nephews','papa','pop','prick',
                'pricks','priest','prince','run-on','sir','son','sonny','sons','stud','thug',
                'thugs','uncle','uncles','virile','waiter','waiters','wanker','widower','widowers'}


female_words = {'actress','actresses','amiga','amigas','aunt','aunts','babe','babes','biddy','bimbo',
                'bimbos','bride','brides','butch','chairwoman','chick','chicks','cow','cows',
                'cunt','cunts','dame','daughter','daughters','doe','dudess','dudette','dudine',
                'dyke','dykes','fag hag','fem','female','feme','femme','fiancee','floozy',
                'fusby','gal','girl','girlfriend','girlfriends','girls','goddess','goddesses',
                'granddaughter','granddaughters','grandma','grandmas','grandmother','grandmothers',
                'hag','hags','hay bag','hay-bag','her','heroine','hers','herself','hoe',
                'hoe bag','hoes','honey','hooker','hookers','hussy','jugs','karen','ladies',
                'lady','lost rib','lubra','mama','mamas','manhole','milf','mistress','mistresses',
                'mivvy','mom','moms','mother','mothers','mrs','ms','muff','niece','nieces',
                'priestess','princess','prostitute','prostitutes','pussies','pussy','queen',
                'queens','quim','scow','she',"she'd","she's",'shickster','sister','sisters',
                'skank','skanks','slut','sluts','spokeswoman','strumpet','tar leather',
                'tit','toots','tootsie','tramp','waitress','whore','whores','widow','widows',
                'wife','wimmin','wives','woman','womankind','women','women',"women's",'womyn'}

#function works on tokenized --but not lemmatized! -- comments

def find_gender(comment_tokens):
    M_length = len(male_words.intersection(word_tokenize(comment_tokens.casefold())))  
    F_length = len(female_words.intersection(word_tokenize(comment_tokens.casefold())))
    
    if M_length > 0 and F_length == 0:
        gender = 'male'
    elif M_length == 0 and F_length > 0:
        gender = 'female'
    elif M_length > 0 and F_length > 0:
        gender = 'both'
    else:
        gender = 'none'
        
    return gender




from tqdm import tqdm
import nltk
from nltk.stem import WordNetLemmatizer
from collections import Counter
import pandas as pd

from gensim.models.phrases import Phrases, ENGLISH_CONNECTOR_WORDS
from gensim.parsing.preprocessing import (remove_stopwords, preprocess_string, strip_short,
                                          strip_tags, strip_multiple_whitespaces, 
                                          strip_non_alphanum, strip_punctuation,
                                          remove_short_tokens, remove_stopword_tokens, 
                                          STOPWORDS, strip_numeric
                                         )  

nltk.download('wordnet')
nltk.download('omw-1.4')

def get_k_freq(data):

    CUSTOM_FILTERS = [strip_tags, 
                  strip_punctuation, 
                  strip_multiple_whitespaces, 
                  strip_non_alphanum, 
                  strip_numeric
                ]

    my_stopwords = STOPWORDS
    lemmatizer = WordNetLemmatizer()

    processed_docs = []
    for line in tqdm(data):
        pre = preprocess_string(line.casefold(), CUSTOM_FILTERS)
        filtered_tokens = remove_stopword_tokens(pre, my_stopwords)
        processed_docs.append([lemmatizer.lemmatize(x) for x in filtered_tokens if len(x) > 1])
    
    terms = []
    for doc in processed_docs:
        terms.extend(doc)

    return Counter(terms)



import nltk
nltk.download('stopwords')
import re

non_english_letters = ['à','â','ç','é','è','ê','ë','î','ï','ı',
                        'ô','ù','û','ü','ÿ','ã','õ','à','ì','ò',
                        'ä','ö','å','ø','æ','ő','ğ','ş','ß','и',
                        'э','ю','я','й','ы']
stopwords=nltk.corpus.stopwords.words("english")

def filter_foreign_language_comments(series):
# def filter_foreign_language_comments(dataframe, threshold = 0.11, filter_df = True):

    # The 10-15% stopword range seems ideal for preserving potentially valuable multi-lingual posts. 
    # I set the filter closer to 10% to err on the side of caution.
    english_comment_list = []
    for txt in series:
        if len(set(re.findall("|".join(non_english_letters), txt.lower()))) > 0:
            english_word_count = 0
            for w in stopwords:
                english_word_count += txt.lower().split().count(w)
                
            english_comment_list.append(english_word_count/len(txt.split()))

        else:
            english_comment_list.append(1)
                    
    return english_comment_list




f_df = pd.DataFrame({'identifier': list(female_words)})
m_df = pd.DataFrame({'identifier': list(male_words)})
f_df['gender'] = 'female'
m_df['gender'] = 'male'
gender_id_df = f_df.append(m_df, ignore_index=True)


def get_tokens(data):
    '''
    tokenize all comments and remove stopwords
    outputs a single list of tokens
    '''
    tokens = []
    print('tokenizing...',end='\r')
    for line in data.body.to_list():
        pre = preprocess_string(line.lower(), CUSTOM_FILTERS)
        tokens.extend(remove_stopword_tokens(pre, my_stopwords))
    print(' ')
    return [t for t in tokens if len(t)>1]


def get_dict(data, k):
    '''
    creates dictionary with 
    counter of terms for each gender
    '''
    top_tokens = defaultdict()
    print('counting tokens...',end='\r')
    top_tokens['all'] = Counter(get_tokens(data)).most_common(k)
    top_tokens['female'] = Counter(get_tokens(data[data.gender=='female'])).most_common(k)
    top_tokens['male'] = Counter(get_tokens(data[data.gender=='male'])).most_common(k)
    print(' ')
    return top_tokens


def identifiers_dict(data, k):
    '''
    creates a dictionary with counter of 
    gender identifiers for each gender
    '''
    global gender_id_df

    pattern = re.compile('|'.join(gender_id_df.identifier.to_list()))

    words = []
    print('finding identifiers...',end='\r')
    for txt in data.body.to_list():
        words.extend(re.findall(pattern, txt.lower()))

    top_tokens = defaultdict()
    top_tokens['f_terms'] = Counter([w for w in words if w in female_words]).most_common(k)
    top_tokens['m_terms'] = Counter([w for w in words if w in male_words]).most_common(k)

    tokens=[]
    for line in data.body.to_list():
        pre = preprocess_string(line.lower(), CUSTOM_FILTERS)
        tokens.extend(remove_stopword_tokens(pre, my_stopwords))

    top_tokens['both_terms'] = Counter([w for w in tokens if w in gender_id_df.identifier.to_list()]).most_common(k)
    print(' ')
    return top_tokens


def get_top_k_tokens(data, k, gender_id=False):
    '''
    creates df with k most frequent tokens 
    for each gender and for all data
    '''
    if gender_id:
        data_dict = identifiers_dict(data, k)
    else:
        data_dict = get_dict(data, k)

    print('creating the dataframe...',end='\r')
    for i,key in enumerate(data_dict.keys()):
        cat_df = pd.DataFrame(data_dict[key])
        cat_df.insert(0, 'gender', key)
        if i==0:
            df = cat_df.copy()
        else:
            df = df.append(cat_df, ignore_index=True)
    df.columns = ['gender', 'token', 'freq']
    df['rank'] = list(range(k))*3
    print(' ')
    return df


def get_percentage(data):
    '''
    takes df with top_k gender identifiers (for all genders) 
    and calculates percentage of frequency within each gender
    '''
    for i,g in enumerate(['f_terms', 'm_terms', 'both_terms']):
        df = data[data['gender'] == g].copy()
        df['percentage'] = 100 * df.freq/df.freq.sum()
        if i==0:
            perc_id = df.copy()
        else:
            perc_id = perc_id.append(df, ignore_index=True)
        perc_id = perc_id.round(2)
    return perc_id
