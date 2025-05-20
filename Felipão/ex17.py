import random

tupla = tuple(random.randint(1, 100000) for _ in range(5))

print('A tupla gerada é: {}'.format(tupla))
print('O menor número é: {}'.format(min(tupla)))
print('O maior número é: {}'.format(max(tupla)))