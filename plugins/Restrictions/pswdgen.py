import random 

Lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num = "1234567890"
symb =  "@#₹&%*-=()~±×÷°•´´}££¥;><"

ans = Lower_case + upper_case + num + symb

Length = 8

PASSWORD_GEN = ""join.(random.sample(ans,length))
