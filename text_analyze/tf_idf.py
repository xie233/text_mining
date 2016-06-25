
#-*- coding:utf-8 -*-
"""tf-idf表示文档特征"""
import os
import nltk.stem
from sklearn.feature_extraction.text import TfidfVectorizer
path = r"data_path"
posts = [open(os.path.join(path, f)).read() for f in os.listdir(path)]
#对英语词干处理
english_stemmer = nltk.stem.SnowballStemmer('english')
#创建类   Tfidf向量化文档并且词干处理
class StemmedTfidfVectorizer(TfidfVectorizer):
    def build_analyzer(self):
        analyzer = super(StemmedTfidfVectorizer, self).build_analyzer()
        return lambda doc: (english_stemmer.stem(w) for w in analyzer(doc))
#使用类 处理
vectorizer = StemmedTfidfVectorizer(
    min_df=1, stop_words='english')
train = vectorizer.fit_transform(unicode(d,errors="replace") for d in posts)

print train.shape

train.toarray()