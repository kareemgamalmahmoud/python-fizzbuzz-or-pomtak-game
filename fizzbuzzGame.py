# i will make num from 0 to 20 
# any num %3 and num %5 ==> fizzbuzz
# num %3 only ==> fizz
# num %5 only ==> buzz
# else display the num

FB = []
#list to add the data on it

for t in range (21):
    if t%5==0 and t%3 == 0 : 
        FB.append("fizzbuzz")
    elif  t%5==0 and t%3 != 0 : 
        FB.append("buzz")
    elif  t%5!=0 and t%3 == 0 : 
        FB.append("fizz")
    else :    
        FB.append(t)
print(FB)