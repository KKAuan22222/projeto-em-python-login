alunos = []
professores = []
materias = []
notas = []

def cadastrar_aluno():
    nome = input("Nome do aluno: ")
    curso = input("Curso do aluno: ")
    aluno = {'nome': nome, 'curso': curso}
    alunos.append(aluno)
    print("Aluno cadastrado com sucesso!\n") 

def cadastrar_professores():
    nome = input("Nome do professor: ")
    curso = input("Curso do professor: ")
    professor = {'nome': nome, 'curso': curso}
    professores.append(professor)
    print("Professor cadastrado com sucesso!\n") 

def cadastrar_materia():
    nome = input("Nome da matéria: ")
    professor = input("Professor responsável: ")
    materia = {'nome': nome, 'professor': professor}
    materias.append(materia)
    print("Matéria cadastrada com sucesso!\n")

def lancar_notas():
    aluno_nome = input("Nome do aluno: ")
    materia_nome = input("Matéria: ")
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    nota3 = float(input("Nota 3: "))

    media = (nota1 + nota2 + nota3) / 3
    situacao = 'Aprovado' if media >= 6 else 'Reprovado'

    registro = {
        'aluno': aluno_nome,
        'materia': materia_nome,
        'nota1': nota1,
        'nota2': nota2,
        'nota3': nota3,
        'media': media,
        'situacao': situacao
    }
    notas.append(registro)
    print(f"Notas lançadas para {aluno_nome} em {materia_nome}.\n")

def relatorio_final():
    print("\n--- RELATÓRIO FINAL ---")
    for registro in notas:
        print(f"Aluno: {registro['aluno']}")
        print(f"Matéria: {registro['materia']}")
        print(f"Nota 1: {registro['nota1']}")
        print(f"Nota 2: {registro['nota2']}")
        print(f"Nota 3: {registro['nota3']}")
        print(f"Média: {registro['media']:.2f}")
        print(f"Situação: {registro['situacao']}\n")

def menu():
    while True:
        print("1. Cadastrar Aluno")
        print("2. Cadastrar Professor")
        print("3. Cadastrar Matéria")
        print("4. Lançar Notas")
        print("5. Exibir Relatório Final")
        print("0. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cadastrar_aluno()
        elif opcao == '2':
            cadastrar_professores()
        elif opcao == '3':
            cadastrar_materia()
        elif opcao == '4':
            lancar_notas()
        elif opcao == '5':
            relatorio_final()
        elif opcao == '0':
            print("Encerrando o sistema.")
            break
        else:
            print("Opção inválida. Tente novamente.\n")

menu()