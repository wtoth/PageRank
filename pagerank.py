import pandas as pd
from ast import literal_eval

def create_scoring_dict():
    score_list = {}
    new_list = {}
    df = pd.read_csv("cleaned_site.csv", converters={"links": literal_eval})
    score = 1.0/(len(df.index)+1)
    for page in df['urls']:
        page = page.split(".com")[-1]
        score_list[page] = score
        new_list[page] = 0
    return score_list, new_list

def pagerank_alg(score, new_score, iterations=1):
    i = 0
    blank_score = new_score
    while i < iterations:
        df = pd.read_csv("cleaned_site.csv", converters={"links": literal_eval})
        #new_score = df.apply(lambda x: score_eval(x['urls'], x['links'], score, new_score), axis=1)
        for url, link in zip(df['urls'], df['links']):
            #print(url, link)
            new_score = score_eval(url, link, score, new_score)
        score = new_score
        new_score = blank_score
        i += 1
    return score

def score_eval(url, links, score, new_score):
    #adjusts url to standardize
    url = url.split(".com")[-1]
    #print(url)
    score_val = score[url]/len(links)
    for link in links:
        try:
            new_score[link] = new_score[link] + score_val
        except:
            pass
    #todo:
    #iterate through links and start constructing new_score as a dict
    #maybe construct new_score in create_scoring_dict and set all vals to 0 upon creation
    #this will help down the road as we can just add all values directly into the already constructed list
    return new_score