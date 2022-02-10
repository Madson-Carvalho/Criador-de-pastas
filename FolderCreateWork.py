import os

def createFolder():
    #caminho onde será criado o diretório
    path = 'C:\\Users\\User\\Desktop'
    while True:
        check_1 = str(input('Deseja criar uma nova pasta? "s" para sim, e "n" para não: '))
        check = check_1.lower()

        if(check != 's' and check != 'n'):
            print('Você digitou um caractere inválido!!!')
            continue
        elif(check == 's'):
            clientName = input('Digite o nome do diretório: ')
            os.chdir(path)
            newFolder = clientName

            # checando se o diretório já existe
            if(os.path.isdir(clientName)):
                print('Já existe um pasta com esse nome!')
            else:
                #criando um diretório filho do criado acima
                os.makedirs(newFolder)

                path_2 = path+'\\'+newFolder

                os.chdir(path_2)

                newFolder_2 = 'Nome do diretório'
                os.makedirs(newFolder_2)

                path_3 = path+'\\'+newFolder

                os.chdir(path_3)

                newFolder_3 = 'Nome do diretório'
                os.makedirs(newFolder_3)

                print(f'Pasta "{clientName}" criada com sucesso!')
            continue
        elif(check == 'n'):
            #encerrando o laço
            print('Você optou por não cirar mais pastas.\n')
            x = str(input('Digite enter pra encerrar o programa.'))
            break

createFolder()
