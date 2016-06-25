#-*- coding:utf-8 -*-
"""载入20news数据集，经过tf_idf特征表示后，进行简单聚类"""
from sklearn import datasets
import nltk.stem
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import metrics
groups = [
    'comp.graphics', 'comp.os.ms-windows.misc', 'comp.sys.ibm.pc.hardware',
    'comp.sys.ma c.hardware', 'comp.windows.x', 'sci.space']
train = datasets.load_files("20news/train",categories=groups)
# print len(train.data)

# print len(train.target_names)


english_stemmer = nltk.stem.SnowballStemmer('english')

from sklearn.feature_extraction.text import TfidfVectorizer


class StemmedTfidfVectorizer(TfidfVectorizer):
    def build_analyzer(self):
        analyzer = super(TfidfVectorizer, self).build_analyzer()
        return lambda doc: (english_stemmer.stem(w) for w in analyzer(doc))

vector = StemmedTfidfVectorizer(min_df=10, max_df=0.5,
                                    
                                    stop_words='english', decode_error='ignore'
                                    )
vec = vector.fit_transform(train.data)
print vec.shape



from sklearn.cluster import KMeans
num = 30
km = KMeans(n_clusters=num, init='k-means++', n_init=1,
            verbose=1)

clustered = km.fit(vec)
labels = dataset.target

print("Homogeneity: %0.3f" % metrics.homogeneity_score(labels, km.labels_))