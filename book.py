import requests
from lxml import etree

fp = open("中华书局书目.txt",'a',encoding='gb18030')
price_list=[]
a = 1241
for num in range(1,int(a)):
    payload = {'ordertype': '1', 'num': '%s'%num}
    print("正在获取……第%s页"%num)
    r = requests.post("http://www.zhbc.com.cn/zhsj/fg/book/booklist.html", params=payload)
    tree = etree.HTML(r.text)
    title_list = tree.xpath('//*[@id="bookhtml"]/li/span/a/@title')
    time_list = tree.xpath('////*[@id="bookhtml"]/li/i[1]/text()')
    banci_list = tree.xpath('//*[@id="bookhtml"]/li/i[2]/text()')
    writer_list = tree.xpath('//*[@id="bookhtml"]/li/i[3]/@title')
    prices = tree.xpath('//*[@id="bookhtml"]/li/i[4]/strong/text()')
    for i in prices:
        price = "价格：" + str(i)
        price_list.append(price)
    ISBN_list = tree.xpath('//*[@id="bookhtml"]/li/i[5]/text()')
    book_list = tree.xpath('//*[@id="bookhtml"]/li/i[6]/text()')
    for i in zip(title_list,time_list,banci_list,writer_list,price_list,ISBN_list,book_list):
        i='///'.join(i)
        fp.write(i+'\n')
fp.close()

