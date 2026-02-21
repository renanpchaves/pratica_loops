while True:
    user = input('Digite o usuário:')
    senha = input('Digite a senha:')

    if len(user) <5:
        print ('Usuário deve ter pelo mennos 5 caracteres')
        continue
    if len(senha) < 8:
        print ('Senha deve ter pelo menos 8 caracteres.')
        continue
    
    print ('Cadastro realizado')
    break