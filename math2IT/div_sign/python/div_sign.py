str01 = "123hjkhsdf kjhdfk j lkjshdkjfh lkjlkjd sdlfkj l ldskjflkj l;kjsdlkfj l;klkjsdf lkj lkjsdf lkj  lsdkjfl kjlksjdf lkj l"

str02 = ''

n=1


for el in str01:
    str02+=el
    if (n%10==0):
        str02+='\r\n'
    n+=1
print(str02)
