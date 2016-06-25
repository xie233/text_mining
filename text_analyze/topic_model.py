# -*- coding: utf-8 -*-
"""  基于主题模型计算文档相似度 """
from gensim import corpora, models, similarities
import numpy as np
from scipy.spatial import distance

corpus = corpora.BleiCorpus('data.dat', 'data.txt')
#建立lda主题模型，主题数取100
model = models.ldamodel.LdaModel(corpus, num_topics=100, id2word=corpus.id2word, alpha=None)
#[[(topic_id，weight),...],...,[]]
thetas = [model[c] for c in corpus]

th = np.zeros((len(thetas),100),float)
for i,c in enumerate(thetas):
    for ti,v in c:
        th[i,ti] += v
#计算文档之间基于主题的相似度
pair = distance.squareform(distance.pdist(th))
#主对角为自身，因而取极大
large = pair.max() + 1
for i in xrange(len(pair)): pair[i,i] = large

doc_id = 3
#doc_id的最相近文档索引
pair[doc_id].argmin()