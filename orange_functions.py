

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
    
    # dataframe['english'] = english_comment_list
    # if filter_df:
    #     return dataframe[dataframe.english > threshold].drop(['english'], axis=1)
    # else:
    #     return dataframe 