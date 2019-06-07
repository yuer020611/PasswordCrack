import itertools
#repeat是密码组合的位数，0123 ... 是密码可以组合的元素
num = input("请输入组合位数：")
cc = int(num)

passwd = ("".join(x) for x in itertools.product("0123456789QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm!@#$%^&*().", repeat=cc))
while True:
    try:
        str = next(passwd)
        print(str)
    except StopIteration as e:
        break
