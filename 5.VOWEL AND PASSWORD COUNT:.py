v_count=0
c_count=0
V="aeiou"
INPUT_STRING=input("Please enter a string:").lower()
for char in INPUT_STRING:
    if 'a' <=char <='z':
        if char in V:
            v_count+=1
        else:
            c_count+=1
print("vowels:",v_count)
print("consonants:",c_count)
