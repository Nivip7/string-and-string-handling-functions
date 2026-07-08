p=input("Password:")
if(8<=len(p)<=15 and
   any(ch.islower() for ch in p) and
   any(ch.isupper() for ch in p) and
   any(ch.isdigit() for ch in p) and
   any(not ch.isalnum() for ch in p) and
   not any(ch.isspace() for ch in p)):
    print("your password is valid!!!")
else:
    print("invalid password!!!!")
