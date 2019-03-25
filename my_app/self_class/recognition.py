import os

import requests
from bs4 import BeautifulSoup
import jieba
from wordcloud import WordCloud
from snownlp import SnowNLP
import time


class Recognition:
    def __init__(self, url):
        res = requests.get(url)
        res.encoding = 'utf-8'
        soup = BeautifulSoup(res.text, 'html.parser')
        self.text = ''.join([news.text.strip() for news in soup.select("p")][1:-6])

    def get_wordcloud(self):
        con = jieba.lcut(self.text)  # 分词
        words = " ".join(con)  # 分词后插入空格
        wordcloud = WordCloud(font_path="simkai.ttf",background_color="white",width=800, height=600).generate(words)
        timestamp = str(time.strftime('%Y%m%d_%H%M%M',time.localtime(time.time())))
        img_path = 'my_app/static/image/'+timestamp+'.png'
        wordcloud.to_file(img_path)
        return img_path.replace("my_app", "..")

    def get_summary(self, limit):
        s = SnowNLP(self.text)
        return "\n".join(s.summary(limit=limit))
