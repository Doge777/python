# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 21:29:16 2020

@author: USER
"""

n=0  #用n計算有幾個無重複的三位數
for i in range(1,5):  #for迴圈i從1開始到4停止
    for j in range(1,5):  #for迴圈j從1開始到4停止
        for k in range(1,5):  #for迴圈k從1開始到4停止
            if(i != k) and (i != j) and (j != k):  #用if來篩選i,j,k，如果三個都不一樣就把它印出來
                    print (i,j,k)
                    n+=1  #成功達成if的條件就+1     
print(n)  #把無重複三位數的數量印出來

                
        
    