me_do_aluno = ('thiago', 'rafael', 'luan', 'andre', 'laysla','edvaldo', 'andreia', 'luan', 'kauan')
materia = ('calculo', 'corpo humano','historia do brasil', 'geografia do mundo')
profesor = ('andre', 'rafael', 'luan', 'thiiago')
curso =('matematica', 'ciências', 'historia', 'geografia') 
media = ('7.0', '8.0', '9.0', '10.0') 

nome_do_aluno = input("Digite o seu nome : ")
materia = input("Digite a materia : ")
professor = input("Digite o nome do professor : ") 
curso = input("Digite o nome do curso : ")

materias = ['calculo', 'corpo humano', 'historia do brasil', 'geografia do mundo']
medias = {}

for materia in materias:
    notas = []
    print(f"\nInforme as notas para a matéria: {materia}")
    for i in range(1, 4):  # Supondo 3 notas por matéria
        nota = float(input(f"Digite a nota {i} para {materia}: "))
        notas.append(nota)
    media = sum(notas) / len(notas)
    medias[materia] = media

print("\nMédia de cada matéria:")
for materia, media in medias.items():
    print(f"{materia}: {media:.2f}")

