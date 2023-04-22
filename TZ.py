print ('A,B,C,D')
for a in 0,1:
    for b in 0,1:
        for c in 0,1:
            for d in 0,1:
                x = a!=b
                y = not x
                w = not b
                z =y or w
                k = z and c
                l = c or d
                m = not l
                n = k!=m
                if n == True:
                    print (a,b,c,d)