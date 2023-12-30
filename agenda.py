from time import sleep

AGENDA = {}

def mostrar_contatos():
    if AGENDA:      # se a agenda existir (não estiver vazia)
        for contato in AGENDA:
            buscar_contato(contato)
    else:
        print('>>>> Agenda vazia')
        sleep(1)

def buscar_contato(contato):
    try:
        print('-' * 20)
        print('Nome: ', contato)
        print('Telefone: ', AGENDA[contato]['telefone'])
        print('Email: ', AGENDA[contato]['email'])
        print('Endereço: ', AGENDA[contato]['endereco'])
        print('-' * 20)
    except KeyError:
        print(f'O contato "{contato}" não existe')
    except Exception as error:
        print('Um erro inesperado ocorreu')

sleep(1)

def ler_detalhes_contato():
    telefone = input('Digite o telefone do contato: ')
    email = input('Digite o email do contato: ')
    endereco = input('Digite o endereço do contato: ')
    return telefone, email, endereco

def incluir_editar_contato(contato, telefone, email, endereco):
    AGENDA[contato] = {
        'telefone': telefone,
        'email': email,
        'endereco': endereco,
    }


def excluir_contato():
    pergunta = str(input('Digite o nome do contato a ser excluído: '))
    try:
        AGENDA.pop(pergunta)
        salvar()
        print()
        print(f'>>>>> Contato {pergunta} excluído com sucesso!')
        print('Atualizando a agenda...')
        sleep(2)
        print()
        mostrar_contatos()
        sleep(2)
    except KeyError:
        print('Contato não encontrado')
        sleep(2)
    except Exception as error:
        print('Um erro inesperado ocorreu')

def exportar_contatos(nome_do_arquivo):
    try:
        with open(nome_do_arquivo, 'w') as arquivo:
            print_executado = False
            for contato in AGENDA:
                telefone = AGENDA[contato]['telefone']
                email = AGENDA[contato]['email']
                endereco = AGENDA[contato]['endereco']
                arquivo.write(f'{contato}, {telefone}, {email}, {endereco}\n')
            print('>>>> Agenda exportada com sucesso')
    except Exception as error:
        print('Algum erro ocorreu')
        print(error)

def importar_contatos(nome_do_arquivo):
    try:
        with open(nome_do_arquivo, 'r') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                detalhes = linha.strip().split(',')
                nome = detalhes[0]
                telefone = detalhes[1]
                email = detalhes[2]
                endereco = detalhes[3]
                incluir_editar_contato(nome, telefone, email, endereco)
                salvar()
    except FileNotFoundError:
        print('>>>>> Arquivo não encontrado')
    except Exception as error:
        print('>>>>> Algum erro inesperado ocorreu')

def salvar():
    exportar_contatos('database.csv')

def carregar():
    try:
        with open('database.csv', 'r') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                detalhes = linha.strip().split(',')
                nome = detalhes[0]
                telefone = detalhes[1]
                email = detalhes[2]
                endereco = detalhes[3]

                AGENDA[nome] = {
                    'telefone': telefone,
                    'email': email,
                    'endereco': endereco,
                }


        print('>>>>> Database carregado com sucesso')
        print(f'>>>>> {len(AGENDA)} contatos carregados')
    except FileNotFoundError:
        print('>>>>> Arquivo não encontrado')
    except Exception as error:
        print('>>>>> Algum erro inesperado ocorreu')
        print(error)

def imprimir_menu():
    print(' 1 -> Mostrar todos os contatos da agenda\n',
          '2 -> Buscar contato\n',
          '3 -> Incluir contato\n',
          '4 -> Editar contato\n',
          '5 -> Excluir contato\n',
          '6 -> Exportar contatos para csv\n',
          '7 -> Importar contatos\n',
          '0 -> Fechar agenda')

carregar()
while True:
    imprimir_menu()
    print()
    opcao = input('Escolha uma opção: ')
    if opcao == '1':
        mostrar_contatos()

    elif opcao == '2':
        contato = str(input('Digite o nome do contato: '))
        buscar_contato(contato)

    elif opcao == '3':
        contato = input('Digite o nome do contato: ')

        try:
            AGENDA[contato]     # se o contato existir na agenda, edite
            print(f'>>>> Editando contato {contato}')
            incluir_editar_contato(contato, telefone, email, endereco)
            print()
            print('>>>> Contato editado com sucesso!')
            sleep(1)
        except KeyError:
            telefone, email, endereco = ler_detalhes_contato()
            incluir_editar_contato(contato, telefone, email, endereco)
            print()
            print('>>>> Contato adicionado com sucesso!')
            salvar()
            sleep(1)

    elif opcao == '4':
        contato = input('Digite o nome do contato: ')

        try:
            AGENDA[contato]
            print(f'>>>> Editando contato {contato}')
            telefone, email, endereco = ler_detalhes_contato()
            incluir_editar_contato(contato, telefone, email, endereco)
            salvar()
        except KeyError:
            print('>>>> Contato inexistente')
            sleep(1)

    elif opcao == '5':
        excluir_contato()

    elif opcao == '6':
        nome_do_arquivo = input('Digite o nome do arquivo a ser exportado: ')
        exportar_contatos(nome_do_arquivo)

    elif opcao == '7':
        nome_do_arquivo = input('Digite o nome do arquivo a ser importado: ')
        importar_contatos(nome_do_arquivo)
        print()
        print('>>>> Contato adicionado/editado com sucesso!')
        sleep(1)
        print('Atualizando a agenda...')
        sleep(2)
        print()
        mostrar_contatos()
        print()
        sleep(1)

    elif opcao == '0':
        print('Saindo...')
        sleep(1)
        break
    else:
        print('Opção inválida')
