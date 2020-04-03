import random
a_count = 0
b_count = 0
for i in range(10):
    a_mima = random.randrange(100000,999999)
    b_mobile = random.randrange(10000000000,19999999999)
    c_list = [a_mima,b_mobile]
    print('请输入：%d'%c_list[random.randrange(0,2)])
    a_input = int(input())
    if a_input == a_mima or a_input == b_mobile:
        print('正确，请继续')
        a_count += 1
        continue
    else:
        print('错误，请继续')
print('您的正确率是：%d'%(a_count/100))