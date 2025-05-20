n = int(input())

n50 = int(n/50)

n20 = int((n-(n50*50))/20)

n10 = int((n-(n50*50+n20*20))/10)

n1 = int((n-(n50*50+n20*20+n10*10)))

print(n50,n20,n10,n1)