import numpy as np
from nltk.corpus import sentiwordnet as swn
from nltk import pos_tag, word_tokenize

class SentiScorer():
    """
    ====Params====
    transform_POS: boolean; whether to transform the nltk.pos_tag to user-define POS
    POS_mapper: dictionary; to map the POS from nltk.pos_tag to user-define POS e.g. 'n','v','a','r'
    dropna: boolean; whether dropping SentiSynsets whose POS is not in the user-define POS
    synsets_aggregation: {'avg','max'}; aggregation method applied to SentiSynsets' scores for a single given word
    
    ====Methods====
    get_POS: tokenises a given document and returns the Part of Speech for each token
    senti_score_word: returns the positive score and the negative score for a given word
    senti_score_text: returns the aggregated(sum) positive score and the aggregated(sum) negative score for a given document
    """
    def __init__(self, transform_POS=True, POS_mapper=None, dropna=True, synsets_aggregation=None):
        self.transform_POS = transform_POS
        self.dropna = dropna
        self.aggregation = synsets_aggregation or 'avg'
        self.mapper = POS_mapper or {
                "JJ": 'a',
                "JJR": 'a',
                "JJS": 'a',
                "NN": 'n',
                "NNS": 'n',
                "NNP": 'n',
                "NNPS": 'n',
                "RB": 'r',
                "RBR": 'r',
                "RBS": 'r',
                "VB": 'v',
                "VBD": 'v',
                "VBG": 'v',
                "VBN": 'v'
            }
    
    def get_POS(self, doc, transform_POS=None, mapper=None, dropna=None):
        transform_POS = transform_POS or self.transform_POS
        dropna = dropna or self.dropna    
        text = word_tokenize(doc)
        tags = pos_tag(text)
        if transform_POS:
            mapper = mapper or self.mapper
            tags_tf = [(t[0], mapper.get(t[1])) for t in tags]
            if dropna:
                tags_tf = [t for t in tags_tf if t[1]!=None]
            return tags_tf
        return tags

    def senti_score_word(self, token, pos=None, synsets_aggregation=None):
        if synsets_aggregation not in ['mean','avg', 'sum', 'max', None]:
            raise ValueError('Aggregation method not recognised!')
        aggregation = synsets_aggregation or self.aggregation
        synsets = list(swn.senti_synsets(token, pos=pos))
        if not synsets:
            return 0, 0
        pos_scores = [s.pos_score() for s in synsets]
        neg_scores = [s.neg_score() for s in synsets]

        if aggregation=='avg' or aggregation=='mean':
            pos_aggr_scores = sum(pos_scores)/len(pos_scores)
            neg_aggr_scores = sum(neg_scores)/len(pos_scores)
        if aggregation=='max':
            pos_aggr_scores = max(pos_scores)
            neg_aggr_scores = max(neg_scores)
        if aggregation=='sum':
            pos_aggr_scores = sum(pos_scores)
            neg_aggr_scores = sum(neg_scores)
        return pos_aggr_scores, neg_aggr_scores

    def senti_score_text(self, doc:str, synsets_aggregation=None):
        aggregation = synsets_aggregation or self.aggregation
        text_POS = self.get_POS(doc)
        word_scores = [self.senti_score_word(token=t[0], pos=t[1], synsets_aggregation=aggregation)
                       for t in text_POS]
        text_pos_score = sum([s[0] for s in word_scores])
        text_neg_score = sum([s[1] for s in word_scores])
        return text_pos_score, text_neg_score

    def fit(self):
        pass

    def transform(self, docs:list, synsets_aggregation=None):
        """
        docs: a iterable list of documents or transcription segments
        """
        scores = [list(self.senti_score_text(doc=d, synsets_aggregation=synsets_aggregation)) for d in docs]
        return np.array(scores)
