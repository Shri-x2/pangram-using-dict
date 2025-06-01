import string
alphabet={}
print (string.ascii_lowercase)

for i in string.ascii_lowercase:
    alphabet[i]=0
print (alphabet)
se = input("Enter your sentence:")
for i in se:
    if i in alphabet:
        alphabet[i]+=1
print (alphabet)
count = 0
for i in alphabet:
    if alphabet[i] > 0:
        count=count+1

if count == 26:
    print("This is a pangram")
else:
    print("This is not a pangram")