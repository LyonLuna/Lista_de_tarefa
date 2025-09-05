def adicionar_tarefa (lista_de_tarefas, tarefa):
    """ adiciona tarefa a lista"""
    lista_de_tarefas.append(tarefa) 
    print ("Tarefa adicionada com sucesso!\n")
    print ("*" * 40)
    return  lista_de_tarefas
def listar_tarefas (lista_de_tarefas): 
    """ exibe a lista"""
    print ("\n")
    print ("*" * 20)
    print ("\n  Lista de Tarefas:")
    print ("_" * 20)
    n = 1
    for tarefa in lista_de_tarefas:
        print(f"* {n}-{tarefa}")
        n += 1
    print( "_" * 20)
    print ('\n'
       )
def exibir_menu():
    print ("Escolha uma opção:\n" \
    "1 - Inserir nova tarefa:\n" \
    "2 - Listar tarefas:\n" \
    "3 - Deletar tarefa: \n" \
    "4 - Cadastrar usuário: \n"\
    "5 - Exibir cadastrados: \n" \
    "6 - Sair \n " \
    "")
def deletar_tarefa(lista_de_tarefas, tarefa):
    lista_de_tarefas.pop(tarefa - 1)
    return lista_de_tarefas
def exibir_usuario(Artistas, artista):
    n = 1
    for artista in Artistas:
        print(f"* {n}-{artista}")
        n += 1
    print ("\n")
        
Artistas = []
lista_de_tarefas = []
continuar = True
print ("\n")
print ("                      Bem vindes ao meu Projeto Final!")
print ("        Meu nome é Lyon Luna, sou Transmasc e agradeço a oportunidade! ")

print("_" * 80)
print ("\n")
print ("          LISTA DE TAREFA DO CATÁLOGO DE ARTISTAS DA MOSTRA HORIZONTE")
print ("\n")


while continuar:
    exibir_menu()
    opção = input("Insira o que deseja fazer: ")
    if opção == "1":
        tarefa = input("Nova tarefa: ")
        lista_de_tarefas = adicionar_tarefa(lista_de_tarefas, tarefa)
        
    elif opção == "2":
        listar_tarefas(lista_de_tarefas)

    elif opção == "3":
        tarefa = input("Insira o número da tarefa que deseja apagar:")
        if not tarefa.isnumeric():
            print ("Número inválido! Tente novamente. ")
            listar_tarefas(lista_de_tarefas)
            continue
            
        if int(tarefa) > len(lista_de_tarefas):
            print ("Número inválido! Tente novamente. ")
            print ("\n")
            print ("-" * 40 )

        elif int(tarefa) <= 0:
            print ("Número inválido! Tente novamente. ")
            print ("\n")
            print ("-" * 40 )

        else:
            deletar_tarefa(lista_de_tarefas,int(tarefa))
            tarefa = int(tarefa)
            print ("\n")
            
        
    elif opção == "4":
            nome = input("Nome:") 
            obra = input("Obra:")
            material = input("Material:")
            dimensões = input("Dimensões:")
            região = input("Região:")
            
            artista = {"nome":nome, "obra":obra, "material":material,"dimensões":dimensões,"região":região}
            Artistas.append(artista)

    elif opção == "5":
        exibir_usuario(Artistas, artista)

    elif opção == "6":
        continuar = False

    else:
        print ("*" * 40)
        print ("\n")
        print("Opção inválida. Tente de novo!")
        print ("\n")