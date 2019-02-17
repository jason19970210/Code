from urllib import request
import re

class Spider():
    # 定義需要的變量和正則表達式
    url = 'https://www.panda.tv/cate/lol?pdt=1.24.s1.2.4jhlr7qfu0h'
    root_pattern = '<div class="video-info">([\s\S]*?)</div>'
    name_pattern = '<span class="video-nickname" title="([\s\S]*?)">'
    number_pattern='<i class="ricon ricon-eye"></i>([\s\S]*?)</span>'
    # 獲取html
    def __fetch_content(self):
        r = request.urlopen(Spider.url)
        #r.read返回的是字節碼格式，需要用字符串轉換
        htmls = r.read()
        htmls = str(htmls,encoding="utf-8")
        return htmls
#主要爬取主播姓名video-nickname和主播人氣值video-number  video-info標籤包含這兩個標籤而且是閉合的
    def __analysis(self,htmls):
         root_html = re.findall(Spider.root_pattern,htmls)
         anchors = []
         for html in root_html:
             name = re.findall(Spider.name_pattern,html)
             number = re.findall(Spider.number_pattern,html)
             anchor = {'name':name,'number':number}
             anchors.append(anchor)
         return anchors
    # 對獲取的數據進行處理
    def refine(self,anchors):
         l = lambda anchor:{
             "name":anchor["name"][0].strip(),
             "number":anchor["number"][0]
         }
         return map(l, anchors)
    # 在控制檯輸出結果
    def __show(self,anchors):
        for rank in range(0,len(anchors)):
            print('rank'+str(rank + 1)
            +"  :  "+anchors[rank]['name']
            +"    "+anchors[rank]['number'])
    # 降序排序
    def __sort(self,anchors):
        anchors = sorted(anchors,key=self.__sort_seed,reverse=True)
        return anchors
    #對降序需要的字段進行處理
    def __sort_seed(self,anchor):
        r = re.findall('\d*',anchor['number'])
        number = float(r[0])
        if "萬" in anchor['number']:
            number *=10000
        return number

    #主方法
    def go(self):
        htmls = self.__fetch_content()
        anchors = self.__analysis(htmls)
        anchors = list(self.refine(anchors))
        anchors = self.__sort(anchors)
        self.__show(anchors)

spider =Spider()
spider.go()