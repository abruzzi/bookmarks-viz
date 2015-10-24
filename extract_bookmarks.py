# encoding=utf-8
import nltk
import jieba

import matplotlib
import matplotlib.pyplot as plt

from bs4 import BeautifulSoup
from nltk.corpus import stopwords

soup = BeautifulSoup(open('bookmarks_10_21_15.html').read(), "html.parser")
data = soup.get_text()

stoplist = stopwords.words('english')
stoplist.extend(['...', 'com', 'using', u'使用', 'blog', u'博客', u'博客园', u'做法', u'论坛', u'部分', u'天下'])

seg_list = jieba.cut(data, cut_all=False)
filtered = [seg.strip().lower() for seg in seg_list if len(seg) > 1]
freq_dist_nltk = nltk.FreqDist([word for word in filtered if word not in stoplist])	

# import json
# print json.dumps(dict(freq_dist_nltk.most_common(100)), ensure_ascii=False).encode('utf8')

# for item in freq_dist_nltk.most_common(100):
#     print unicode(item[0])

import pandas as pd
from pandas import DataFrame, Series

frame = DataFrame(freq_dist_nltk.most_common(20), columns=['keywords', 'frequencies'])

myfont = matplotlib.font_manager.FontProperties(fname='/Library/Fonts/AdobeSongStd-Light.otf') 

ax = frame.plot(kind='bar')
for rect, keyw in zip(ax.patches, frame['keywords']) :
    height = rect.get_height()
    ax.text(rect.get_x()+rect.get_width()/2., 1.05*height, unicode(keyw),
                 ha='center', va='bottom', fontproperties=myfont, rotation=45)

# legend(bbox_to_anchor=(1.02, 1), loc=2, borderaxespad=0.)
plt.savefig('destination_path.png', format='png', dpi=600, fontproperties=myfont)   

