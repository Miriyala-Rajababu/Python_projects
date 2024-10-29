import random
def OTPgenerator():
    return ''.join(str(random.randint(0,9)) for x in range(4))
print(OTPgenerator())
