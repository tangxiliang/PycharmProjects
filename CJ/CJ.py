#coding=utf-8
# -*-coding:utf-8 -*-
import random


# 定义对象
class Prize(object):

    def __init__(self, prize_name, prize_weight):
        # self.id

        self.prize_name = prize_name
        self.prize_weight = prize_weight


def getPrizeIndex(lst):
    rand = -1
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
    p1 = Prize(u"魏晨上海演唱会门票VIP", 5)
    p2 = Prize(u"魏晨白日梦想家专辑带签名一张", 4)
    p3 = Prize(u"魏晨白日梦想家专辑内地一张", 3)
    p4 = Prize(u"糖粒子一把",7)
    lst = [p1,p2,p3,p4,]
    firstprizequantity = 5
    twoprizequantity = 5
    threeprizequantity = 5
    fourprizequantity = 8

    first=0
    second=0
    three=0
    four=0
    for i in range(6):
        selected = getPrizeIndex(lst)
        selected = int(selected)
        print u"第%d次抽中的奖品为" % i + lst[selected].prize_name
        if selected==1:
            first+=1
        if selected==2:
            second+=1
        if selected==3:
            three+=1
        else:
            four+=1

    print u"抽奖结束"
    print "一等奖%d" %first ,"二等奖%d" %second,"三等奖%d" %three,"参与奖%d"%four
    if firstprizequantity-first< 0:
        print "一等奖库存：0"
    elif firstprizequantity - first > 0:
        print "一等奖,魏晨上海演唱会门票VIP剩余%d"%(firstprizequantity-first)
    if twoprizequantity -first < 0:
        print "二等奖库存：0"
    elif twoprizequantity - first > 0:
        print "二等奖,魏晨白日梦想家专辑带签名一张剩余%d"%(twoprizequantity-second)
    if threeprizequantity - first< 0 :
        print "三等奖库存：0"
    

    elif threeprizequantity - first > 0:
        print "三等奖,魏晨白日梦想家专辑内地一张剩余%d"%(threeprizequantity-three)
    if fourprizequantity - four < 0:
        print "参与奖库存：0"
    elif fourprizequantity - four >= 0:
        print "参与奖,糖粒子剩余%d"%(fourprizequantity-four)





if __name__ == "__main__":
    main()
