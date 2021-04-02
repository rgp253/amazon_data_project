# Name: Raymund Palafox
# Date: 4/1/2021
# Course: JUMP plus

# --- Description ---
# In the original set of data, these were all the possible combinations
# within the 'Running Time' column in the original data set.
# This code converts all possible combinations of strings in a single
# integer representing the time in minutes. I compared there lengths
# and used string manipulation to get the result

# *** LIST OF ALL POSSIBLE COMBINATIONS ***
a = "2h"            #k[0-1] --> 2

#*** min ****
b = "50min"         #a[0-4] --> 5 # good
c = "56 min"        #b[0-5] --> 6 # good
d = "1h 3min"       #c[0-6] --> 7 # good
e = "2h 52min"      #d[0-7] --> 8 # good
f = "2 h 8min"      #e[0-7] --> 8 # good
g = "2h 5 min"      #f[0-7] --> 8 # good
h = "3 h 28min"     #g[0-8] --> 9 # good
i = "1h 18 min"     #h[0-8] --> 9 # good
j = "2 h 9 min"     #h[0-8] --> 9 # good
k = "1 h 42 min"    #j[0-9] --> 10 # good

#*** mins ***
l = "32mins"         #l[0-5] --> 6 # good
m = "45 mins"        #m[0-6] --> 7 # good
n = "4h 5mins"       #n[0-7] --> 8 # good
o = "1h 21mins"      #o[0-8] --> 9 # good
p = "1 h 3mins"      #p[0-8] --> 9 # good
q = "3h 7 mins"      #q[0-8] --> 9 # good
r = "1 h 11mins"     #r[0-9] --> 10 # good
s = "2h 54 mins"     #s[0-9] --> 10 # good
t = "3 h 2 mins"     #t[0-9] --> 10 # good
u = "1 h 22 mins"    #u[0-10] --> 11 # good

def getMinutes(x):
    temp_int = 0

    # a = "2h" 
    if(len(x) == 2):
        x = x.replace('h', '')
        temp_int = int(x)*60
        # return temp_int
        print("A in minutes: " + str(temp_int))

    # b = "50min"
    elif(len(x) == 5):
        x = x.replace("min", "")
        # return int(x)
        print("B in minutes: " + str(x))
    
    # c = "56 min" 
    # l = "32mins"
    elif (len(x) == 6):
        x = x.replace('m', ' ')
        s = x.split(' ')
        # return int(s[0])
        print("C then L in minutes: " + str(s[0]))
    
    # d = "1h 3min"
    # m = "45 mins" 
    elif(len(x) == 7):
        x = x.replace('m', ' ')
        x = x.replace('h','')
        s = x.split(' ')

        for value in range(len(s)-1):
            if(s[value] == ''):
                s.pop(value)

        if(len(s) == 3):
            temp_int = int(s[0])*60 + int(s[1])
            # return temp_int
            print("D and M in minutes: " + str(temp_int))
        
        elif(len(s) == 2):
            temp_int = int(s[0])
            # return temp_int
            print('D and M in minutes: ' + str(temp_int))

    # e = "2h 52min"
    # f = "2 h 8min"
    # g = "2h 5 min"
    # n = "4h 5mins"
    elif(len(x) == 8):
        x = x.replace('h', '')
        x = x.replace(' min','')
        x = x.replace('mins','')
        x = x.replace('min','')
        s = x.split(' ')

        for value in range(len(s)-1):
            if(s[value] == ''):
                s.pop(value)
        
        temp_int = int(s[0])*60 + int(s[1])
        # return temp_int
        print("E, F, G then N in minutes: " + str(temp_int))
    
    # h = "3 h 28min"
    # i = "1h 18 min"
    # j = "2 h 9 min"
    # o = "1h 21mins"
    # p = "1 h 3mins"
    # q = "3h 7 mins"
    elif(len(x) == 9):
        x = x.replace('h', '')
        x = x.replace('mins','')
        x = x.replace(' min','')
        x = x.replace('min','')
        s = x.split(' ')

        for value in range(len(s)-1):
            if(s[value] == ''):
                s.pop(value)

        temp_int = int(s[0])*60 + int(s[1])
        # return temp_int
        print("H, I, J, O, P, then Q in minutes: " + str(temp_int))

    # k = "1 h 42 min"
    # r = "1 h 11mins"
    # s = "2h 54 mins"
    # t = "3 h 2 mins"
    elif(len(x) == 10):
        x = x.replace('h', '')
        x = x.replace('mins','')
        x = x.replace(' min','')
        s = x.split(' ')

        for value in range(len(s)-1):
            if(s[value] == ''):
                s.pop(value)

        temp_int = int(s[0])*60 + int(s[1])
        # return temp_int
        print("K, R, S, then T in minutes: " + str(temp_int))
   
    # u = "1 h 22 mins"
    elif(len(x) == 11):
        x = x.replace('h', '')
        x = x.replace('mins','')
        s = x.split(' ')

        for value in range(len(s)-1):
            if(s[value] == ''):
                s.pop(value)

        temp_int = int(s[0])*60 + int(s[1])
        # return temp_int
        print("U in minutes: " + str(temp_int))

# length of 2
    # a = "2h"
getMinutes(a)

# length of 5
    # b = "50min"
getMinutes(b)

# length of 6
    # c = "56 min"
    # l = "32mins"
getMinutes(c)
getMinutes(l)

# length of 7
    # d = "1h 3min"
    # m = "45 mins"
getMinutes(d)
getMinutes(m)

# length of 8
    # e = "2h 52min"
    # f = "2 h 8min"
    # g = "2h 5 min"
    # n = "4h 5mins"
getMinutes(e)
getMinutes(f)
getMinutes(g)
getMinutes(n)

# length of 9
    # h = "3 h 28min"
    # i = "1h 18 min"
    # j = "2 h 9 min"
    # o = "1h 21mins"
    # p = "1 h 3mins"
    # q = "3h 7 mins"
getMinutes(h)
getMinutes(i)
getMinutes(j)
getMinutes(o)
getMinutes(p)
getMinutes(q)

# length of 10
    # k = "1 h 42 min"
    # r = "1 h 11mins"
    # s = "2h 54 mins"
    # t = "3 h 2 mins"
getMinutes(k)
getMinutes(r)
getMinutes(s)
getMinutes(t)

# length of 11
    # u = "1 h 22 mins"
getMinutes(u)