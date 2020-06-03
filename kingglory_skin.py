# coding: utf-8

import requests
import re
import os

#拼接url使其完整，返回拼接好的英雄url
def concat_url(url):
    return "https://pvp.qq.com/web201605/"+url

#处理英雄url，返回皮肤url列表
def deal_url(url):
    response = requests.get(url)
    response.encoding = "gbk"
    #print(response.text)
    name = re.findall(r'"cover-name">(.+)</',response.text)[0]
    #n为皮肤个数
    n = len(re.findall(r'data-imgname="(.*)"',response.text)[0].split("|"))
    #存放对应英雄所有皮肤url
    skin_url_list = []
    #皮肤url的基础格式(只有一个序号不同，下面进行了拼接)
    base_url = re.findall(r"(game.gtimg.cn/images/yxzj/img201606/skin/hero-info/.*)\.jpg",response.text)[0]
    #遍历生成所有皮肤url，存放在列表中
    for i in range(1,n+1):
        skin_url_list.append(base_url[:-1]+str(i)+".jpg")
    #返回列表
    return skin_url_list,name

def get_skin(skin_url):
    response = requests.get(skin_url)
    return response.content

def main():
    start_url = "https://pvp.qq.com/web201605/herolist.shtml"
    
    response = requests.get(start_url)
    print("status code: ",response.status_code)
    #获取所有英雄网址列表
    urllist = re.findall(r"herodetail/\d*\.shtml",response.text)
    save_dir = "pic/"
    if not os.path.exists(save_dir):
        os.mkdir(save_dir)
    for url in urllist[:3]:
        hero_id = re.findall(r"\d+",url)[0]
        n = urllist.index(url)+1
        url = concat_url(url)
        skinlist,heroname = deal_url(url)
        for skin_url in skinlist:
            skin = get_skin("http://"+skin_url)
            with open(save_dir+heroname+skin_url[-5:],"wb") as f:
                f.write(skin)

        print(heroname+"英雄已下载ok")
main()
