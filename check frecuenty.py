test_dict = {"codingal:3 is:2 best:2 for:2 coding:1"}
print("the original dictionary :" + str(test_dict))
res=dict()
x=list(test_dict)
y=list(set(x))
for i in y:
    res[i]=x.count(i)
print("the frequency value is:" + str(res))