#coding=utf-8
import re #正则表达式模块
from urllib import request #通过request对象获取html页面
class Spider():
    #url = 'https://www.panda.tv/cate/lol'
    url = 'https://17.live'
    root_pattern = '<div class="video-info">([\s\S]*?)</div>' #()表示只提取定位标签中间内容
    name_pattern = '</i>([\s\S]*?)</span>'
    number_pattern = '<span class="video-number">([\s\S]*?)</span>'
    def __fetch_content(self): #私有方法，获取html页面
        r = request.urlopen(Spider.url) #在实例方法里读取类变量url
        htmls = r.read() #字节码
        htmls = str(htmls,encoding = 'utf-8') #将字节码转为字符串
        print(htmls)
        return htmls
    def __analysis(self,htmls):#分析htmls文本，通过正则表达式提取html文本中的主播名和人气值
        root_html = re.findall(Spider.root_pattern,htmls)
        anchors = []
        for html in root_html:
            name = re.findall(Spider.name_pattern,html)
            number = re.findall(Spider.number_pattern,html)
            anchor = {'name':name,'number':number}
            anchors.append(anchor)
        print(anchors)
        return anchors
    def __refine(self,anchors): #精炼数据，剔除文本中的空格和换行符等内容，规范成易读的数据
        targets = []
        for target_list in anchors:
            name = target_list['name'][0].strip()
            number = target_list['number'][0]
            one_people = {'name':name,'number':number}
            targets.append(one_people)
        print(targets); 
        return targets
    def __sort(self,anchors): #对精炼后的数据按主播人气值进行排序
        anchors = sorted(anchors,key = self.__sort_seed,reverse = True)
        return anchors
    #设置排序规则
    def __sort_seed(self,anchor):
        r = re.findall('\d*',anchor['number'])
        number = float(r[0])
        if  '万' in anchor['number']:
            number *= 10000
        return number
    def __show(self,anchors): #展示最终爬取的数据
        for rank in range(0,len(anchors)):
            print('rank ' + str(rank+1)
            + ':' +anchors[rank]['name'] 
            + '    ' + anchors[rank]['number'])
    def go(self): #公开方法，go方法是Spider的入口方法
        htmls = self.__fetch_content()
        anchors = self.__analysis(htmls)
        anchors = self.__refine(anchors)
        anchors = self.__sort(anchors)
        self.__show(anchors)
spider  = Spider()
spider.go()

