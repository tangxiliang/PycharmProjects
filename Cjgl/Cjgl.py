# -*-coding:utf-8 -*-
import random


# 定义对象
class Prize(object):

    def __init__(self, prize_name, prize_weight):
        # self.id=id
        self.prize_name = prize_name
        self.prize_weight = prize_weight


def getPrizeIndex(lst):
    rand = 1
    sumWeight = 0
    # 循环，把所有的权重都加上
    for item in lst:
        sumWeight += item.prize_weight
        # 生成一个随机数
        randomNumber = random.uniform(0, 5)
        d1 = 0
        d2 = 0
        try:
            for p in lst:
                d2 += p.prize_weight / float(sumWeight)
                if lst.index(p) == 0:
                    d1 = 0
                else:
                    d1 += lst[lst.index(p) - 1].prize_weight / float(sumWeight)
                    if randomNumber >= d1 and randomNumber <= d2:
                        rand = lst.index(p)
                        break
        except:
            print "抽奖失败"
    return rand


def main():
    p1 = Prize(u"魏晨上海演唱会门票VIP", 100)
    p2 = Prize(u"魏晨白日梦想家专辑带签名一张", 30)
    p3 = Prize(u"魏晨白日梦想家专辑内地一张", 40)
    p4 = Prize(u"魏晨远专辑带签名一张", 30)
    p4 = Prize(u"魏晨远专辑台版一张", 40)
    p5 = Prize(u"魏晨吊牌一个", 50)
    p6 = Prize(u"参与奖", 20)
    lst = [p1, p2, p3, p4, p5, p6,p1]
    first=0
    second=0
    three=0
    for i in range(500):
        selected = getPrizeIndex(lst)
        selected = int(selected)
        print u"第%d次抽中的奖品为" % i + lst[selected].prize_name
        if selected==1:
            first+=1
        if selected==2:
            second+=1
        if selected==3:
            three+=1

    print u"抽奖结束"
    print "一等奖%d" %first ,"二等奖%d" %second,"三等奖%d" %three


if __name__ == "__main__":
    main()
