nome = input('Digite o seu nome completo:')
print ('Nome em letras maiusculas:', nome.upper())
print ('Nome em letras maiusculas:', nome.lower())

sem_espaços = nome.replace ('','')
total_letras = len(sem_espaços)

print ('Esta é a quantidade de letras (sem espaço): {}' .format(sem_espaços))

primeiro_nome = len(nome.strip().split()[0])
print ('Está é a quantidade de letras no primeiro nome: {}'.format(primeiro_nome))

