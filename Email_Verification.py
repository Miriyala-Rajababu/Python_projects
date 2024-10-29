import re
def Email_valid(mail):
    if re.match("[A-Z]*[a-z]+[0-9]*@gmail.com$",mail):
        return True
    else:
        return False
print(Email_valid(input()))
