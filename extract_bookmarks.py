# encoding=utf-8
import jieba

import matplotlib
import matplotlib.pyplot as plt

from bs4 import BeautifulSoup
from pandas import DataFrame
from collections import Counter

def load_bookmarks_data():
	soup = BeautifulSoup(open('bookmarks_10_21_15.html').read(), "html.parser")
	return soup.get_text()

def extract_segments(data):
	seg_list = jieba.cut(data, cut_all=False)
	return [seg.strip().lower() for seg in seg_list if len(seg) > 1]

def tokenize():	
	stoplist = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', 'her', 'hers', 'herself', 'it', 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', 'should', 'now']
	stoplist.extend(['...', 'com', 'using', u'使用', 'blog', u'博客', u'博客园', u'做法', u'论坛', 'part', u'部分', u'天下'])
	filtered = extract_segments(load_bookmarks_data())
	
	return Counter([word for word in filtered if word not in stoplist])

def visualize():
	frame = DataFrame(tokenize().most_common(20), columns=['keywords', 'frequencies'])
	myfont = matplotlib.font_manager.FontProperties(fname='/Library/Fonts/AdobeSongStd-Light.otf') 

	plt.style.use('ggplot')
	
	ax = frame.plot(kind='bar')
	for rect, keyw in zip(ax.patches, frame['keywords']) :
	    height = rect.get_height()
	    ax.text(rect.get_x()+rect.get_width()/2., 1.05*height, unicode(keyw),
	                 ha='center', va='bottom', fontproperties=myfont, rotation=45)

	plt.savefig('bookmarks_trending.png', format='png', dpi=600, fontproperties=myfont)   

if __name__ == "__main__":
	visualize()