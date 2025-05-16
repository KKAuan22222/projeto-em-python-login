import tkinter as tk
from tkinter import ttk

nome_do_aluno = ['thiiago', 'rafael', 'luan', 'andre', 'laysla','edvaldo', 'andreia', 'luan', 'kauan']
materia = ['matematica', 'ciências', 'historia', 'geografia']
profesor = ['andre', 'rafael', 'luan', 'thiiago']
curso = ['calculo', 'corpo humano', 'historia do brasil', 'geografia do mundo']

# Cria a janela principal
root = tk.Tk()
root.title("Informações dos Alunos")

# Cria a tabela
tree = ttk.Treeview(root, columns=('Aluno', 'Matéria', 'Professor', 'Curso'), show='headings')
tree.heading('Aluno', text='Nome do Aluno')
tree.heading('Matéria', text='Matéria')
tree.heading('Professor', text='Professor')
tree.heading('Curso', text='Curso')

# Preenche a tabela com os dados existentes
for i in range(min(len(nome_do_aluno), len(materia), len(profesor), len(curso))):
    tree.insert('', tk.END, values=(nome_do_aluno[i], materia[i], profesor[i], curso[i]))

tree.pack(expand=True, fill='both')

# Campos de entrada
frame = tk.Frame(root)
frame.pack(pady=10)

entry_aluno = tk.Entry(frame)
entry_aluno.grid(row=0, column=0)
entry_aluno.insert(0, "Nome do Aluno")

entry_materia = tk.Entry(frame)
entry_materia.grid(row=0, column=1)
entry_materia.insert(0, "Matéria")

entry_professor = tk.Entry(frame)
entry_professor.grid(row=0, column=2)
entry_professor.insert(0, "Professor")

entry_curso = tk.Entry(frame)
entry_curso.grid(row=0, column=3)
entry_curso.insert(0, "Curso")

def inserir():
    aluno = entry_aluno.get()
    mat = entry_materia.get()
    prof = entry_professor.get()
    cur = entry_curso.get()
    if aluno and mat and prof and cur:
        tree.insert('', tk.END, values=(aluno, mat, prof, cur))
        entry_aluno.delete(0, tk.END)
        entry_materia.delete(0, tk.END)
        entry_professor.delete(0, tk.END)
        entry_curso.delete(0, tk.END)

btn_inserir = tk.Button(frame, text="Inserir", command=inserir)
btn_inserir.grid(row=0, column=4, padx=5)

root.mainloop()