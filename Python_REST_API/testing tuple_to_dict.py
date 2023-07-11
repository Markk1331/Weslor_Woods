y = ('a',1,'b',2,'c',3)

y_dic = {y[i]:y[i+1] for i in range(0,len(y),2)}

print(y_dic)