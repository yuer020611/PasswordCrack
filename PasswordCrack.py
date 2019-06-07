import itertools
num = input("Please enter the password length：")
cc = int(num)
passwd = ("".join(x) for x in itertools.product("0123456789QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm!@#$%^&*().", repeat=cc))
while True:
    try:
        str = next(passwd)
        print(str)
    except StopIteration as e:
        break
