a_0 = int(input('Qual o primeiro termo da PA? \n'))
r =  int(input('Qual a razão da PA? \n'))

print('Os três primeiros termos são:')

for n in range (0,10):
    print(a_0 + n * r)