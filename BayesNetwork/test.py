#coding=utf-8
from sklearn.feature_extraction.text import TfidfVectorizer
document = ["I have a pen.",
            "I have an apple."]
tfidf_model = TfidfVectorizer().fit(document)
sparse_result = tfidf_model.transform(document)     # 得到tf-idf矩阵，稀疏矩阵表示法
print(sparse_result)

print(sparse_result.todense())                     # 转化为更直观的一般矩阵

print(tfidf_model.vocabulary_)                      # 词语与列的对应关系
