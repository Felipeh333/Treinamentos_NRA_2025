range1 = 0
range2 = 10

for i in range(range1,range2):
    print(i*2)

print('Gostaria de mais termos?(y/n)')

r = input().strip()

while r!='n':
    range1=range2
    range2=range2+10
    for i in range(range1,range2):
        print(i*2)

    print('Gostaria de mais termos?(y/n)')
    r=input().strip()