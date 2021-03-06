## 불용어 처리 ##
'''
불용어 처리
- NLTK에 사전 등록된 불용어를 기준으로 토큰 목록에서 불필요한 토큰을 삭제함
'''
import nltk
from nltk.corpus import gutenberg
print(gutenberg.fileids())

gb_words = gutenberg.words('bible-kjv.txt')
words_filtered = [e.lower() for e in gb_words if len(e) >= 3]
stopwords = nltk.corpus.stopwords.words('english')
words = [w for w in words_filtered if w.lower() not in stopwords]

fdist = nltk.FreqDist(words)
fdist2 = nltk.FreqDist(gb_words)


print('Following are the most common 10 words in the bag')
print(fdist2.most_common(10))
print('Following are the most common 10 words in the bag minus the stopwords')
print(fdist.most_common(10))
fdist.plot()