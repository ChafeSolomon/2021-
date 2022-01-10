#jumle up the numbers 

alg = {'1':'9','2':'8','3':'7','4':'6','5':'5','6':'4','7':'3','8':'2','9':'1'}
number = input("Enter a phone number: ")
new_numer = ""
for i in number:
    if i in alg:
        x = alg[i]
        new_numer = new_numer + x
new_numer = int(new_numer)
print(new_numer)
print(type(new_numer))