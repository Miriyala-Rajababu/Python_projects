import string
import random
def Passwordgenerator(Length,numbers=False, specailchar=False):
    Letters=string.ascii_letters
    Numbers=string.digits
    Punctuation=string.punctuation
    
    Password=''
    while len(Password)<=Length:
        if numbers:        
            Password+=random.choice(Numbers)
            
        if specailchar:
            Password+=random.choice(Punctuation)
        Password+=random.choice(Letters)
    return Password
n=input("Include special characters? (y/n): ").strip().lower() == 'y'
p= input("Include numbers? (y/n): ").strip().lower() == 'y'
l=int(input("length"))
print(Passwordgenerator(l,n,p))
