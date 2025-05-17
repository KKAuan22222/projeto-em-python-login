aluno = ('aluno', 'aluno')
nota = ('nota', 'nota')
professor = ('professor', 'professor')
curso = ('curso', 'curso')
materia = ('materia', 'materia')

# Aluno
nome_aluno = "João Silva"
idade_aluno = 20

# Nota
nota_prova = 8.5
nota_trabalho = 9.0

# Professor
nome_professor = "Maria Oliveira"
disciplina_professor = "Matemática"

# Curso
nome_curso = "Engenharia"
duracao_curso = 5  # em anos

# Matéria
nome_materia = "Cálculo I"
carga_horaria = 60  # em horas

#tela para login
import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import simpledialog

try:
    from PIL import Image, ImageTk  # pip install pillow
    PIL_OK = True
except ImportError:
    PIL_OK = False

alunos = []

def calcular_media(notas):
    return sum(notas) / len(notas)

def adicionar_aluno():
    janela = tk.Toplevel(root)
    janela.title("Cadastro de Aluno")
    janela.geometry("480x520")
    janela.resizable(False, False)
    janela.configure(bg="#f0f2f5")

    # Título
    tk.Label(janela, text="Cadastro de Aluno", font=("Segoe UI", 16, "bold"), bg="#f0f2f5", fg="#273c75").pack(pady=15)

    campos = {}
    labels = [
        ("Nome do Aluno:", "nome"),
        ("Professor:", "professor"),
        ("Curso:", "curso"),
        ("Matéria:", "materia"),
    ]
    for idx, (texto, chave) in enumerate(labels):
        frame = tk.Frame(janela, bg="#f0f2f5")
        frame.pack(fill='x', padx=40, pady=(8 if idx == 0 else 4, 0))
        tk.Label(frame, text=texto, font=("Segoe UI", 11, "bold"), bg="#f0f2f5", fg="#273c75", width=15, anchor="w").pack(side='left')
        entry = tk.Entry(frame, font=("Segoe UI", 11), width=25)
        entry.pack(side='left', padx=5)
        campos[chave] = entry

    notas_vars = []
    for i in range(1, 4):
        frame = tk.Frame(janela, bg="#f0f2f5")
        frame.pack(fill='x', padx=40, pady=4)
        tk.Label(frame, text=f"Nota {i}:", font=("Segoe UI", 11, "bold"), bg="#f0f2f5", fg="#273c75", width=15, anchor="w").pack(side='left')
        var = tk.DoubleVar()
        entry = tk.Entry(frame, font=("Segoe UI", 11), textvariable=var, width=25)
        entry.pack(side='left', padx=5)
        notas_vars.append(var)

    # Mensagem de status
    status_label = tk.Label(janela, text="", font=("Segoe UI", 10), bg="#f0f2f5", fg="red")
    status_label.pack(pady=5)

    def salvar():
        nome = campos["nome"].get().strip()
        professor = campos["professor"].get().strip()
        curso = campos["curso"].get().strip()
        materia = campos["materia"].get().strip()
        notas = []
        for var in notas_vars:
            try:
                nota = float(var.get())
                if nota < 0 or nota > 10:
                    raise ValueError
                notas.append(nota)
            except:
                status_label.config(text="Digite notas válidas (0 a 10).")
                return
        if not (nome and professor and curso and materia):
            status_label.config(text="Preencha todos os campos.")
            return
        alunos.append({
            "nome": nome,
            "professor": professor,
            "curso": curso,
            "materia": materia,
            "notas": notas
        })
        atualizar_todas()
        messagebox.showinfo("Cadastro", f"Aluno {nome} cadastrado com sucesso!")
        janela.destroy()

    # Botão Confirmar com destaque
    btn_confirmar = ttk.Button(janela, text="Confirmar", command=salvar)
    btn_confirmar.pack(pady=25, ipadx=10, ipady=4)

def atualizar_tabela():
    tabela.delete(*tabela.get_children())
    for aluno in alunos:
        media = calcular_media(aluno["notas"])
        situacao = "Aprovado" if media >= 7.0 else "Reprovado"
        if PIL_OK and img_aprovado and img_reprovado:
            icone = img_aprovado if situacao == "Aprovado" else img_reprovado
        else:
            icone = ""
        notas_str = ", ".join([f"{n:.1f}" for n in aluno["notas"]])
        tabela.insert(
            '', tk.END,
            values=('', aluno['nome'], aluno['professor'], aluno['curso'], aluno['materia'], notas_str, f"{media:.2f}", situacao),
            image=icone
        )

def atualizar_tabela_notas():
    tabela_notas.delete(*tabela_notas.get_children())
    for aluno in alunos:
        media = calcular_media(aluno["notas"])
        situacao = "Aprovado" if media >= 7.0 else "Reprovado"
        notas = aluno["notas"]
        tabela_notas.insert(
            '', tk.END,
            values=(aluno['nome'], aluno['materia'], f"{notas[0]:.1f}", f"{notas[1]:.1f}", f"{notas[2]:.1f}", f"{media:.2f}", situacao)
        )

def mostrar_detalhes():
    selecao = tabela.selection()
    if not selecao:
        messagebox.showinfo("Detalhes", "Selecione um aluno na tabela.")
        return
    idx = tabela.index(selecao[0])
    aluno = alunos[idx]
    media = calcular_media(aluno["notas"])
    situacao = "Aprovado" if media >= 7.0 else "Reprovado"
    detalhes = (
        f"Nome: {aluno['nome']}\n"
        f"Professor: {aluno['professor']}\n"
        f"Curso: {aluno['curso']}\n"
        f"Matéria: {aluno['materia']}\n"
        f"Notas: {', '.join([str(n) for n in aluno['notas']])}\n"
        f"Média: {media:.2f}\n"
        f"Situação: {situacao}"
    )
    messagebox.showinfo("Detalhes do Aluno", detalhes)

def remover_aluno():
    selecao = tabela.selection()
    if not selecao:
        messagebox.showinfo("Remover", "Selecione um aluno na tabela.")
        return
    idx = tabela.index(selecao[0])
    nome = alunos[idx]['nome']
    if messagebox.askyesno("Remover", f"Tem certeza que deseja remover {nome}?"):
        alunos.pop(idx)
        atualizar_todas()

root = tk.Tk()
root.title("Gestão Escolar Profissional")
root.geometry("1250x600")
root.configure(bg="#000000")  # fundo preto

style = ttk.Style()
style.theme_use("clam")
style.configure("Treeview.Heading", font=("Segoe UI", 11, "bold"), background="#000000", foreground="#ffffff")  # cabeçalho preto e texto branco
style.configure("Treeview", font=("Segoe UI", 10), rowheight=32, background="#1a1a1a", fieldbackground="#1a1a1a", foreground="#ffffff")  # linhas da tabela em preto/cinza escuro e texto branco
style.map("Treeview", background=[('selected', '#333333')])

# Notebook para abas
notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill='both', padx=10, pady=10)

# --- Aba Alunos ---
aba_alunos = tk.Frame(notebook, bg="#000000")
notebook.add(aba_alunos, text="Alunos")

frame_botoes = tk.Frame(aba_alunos, bg="#000000")
frame_botoes.pack(pady=10, fill='x')

btn_adicionar = ttk.Button(frame_botoes, text="Adicionar Aluno", command=adicionar_aluno)
btn_adicionar.pack(side='left', padx=5)

btn_detalhes = ttk.Button(frame_botoes, text="Ver Detalhes", command=mostrar_detalhes)
btn_detalhes.pack(side='left', padx=5)

btn_remover = ttk.Button(frame_botoes, text="Remover Aluno", command=remover_aluno)
btn_remover.pack(side='left', padx=5)

colunas = ('Status', 'Nome', 'Professor', 'Curso', 'Matéria', 'Notas', 'Média', 'Situação')
tabela = ttk.Treeview(aba_alunos, columns=colunas, show='headings', selectmode='browse')
tabela.heading('Status', text=' ')
tabela.column('Status', width=40, anchor='center')
tabela.heading('Nome', text='Nome')
tabela.column('Nome', width=150, anchor='center')
tabela.heading('Professor', text='Professor')
tabela.column('Professor', width=150, anchor='center')
tabela.heading('Curso', text='Curso')
tabela.column('Curso', width=150, anchor='center')
tabela.heading('Matéria', text='Matéria')
tabela.column('Matéria', width=150, anchor='center')
tabela.heading('Notas', text='Notas')
tabela.column('Notas', width=150, anchor='center')
tabela.heading('Média', text='Média')
tabela.column('Média', width=80, anchor='center')
tabela.heading('Situação', text='Situação')
tabela.column('Situação', width=100, anchor='center')
tabela.pack(expand=True, fill='both', padx=10, pady=10)

# --- Aba Notas ---
aba_notas = tk.Frame(notebook, bg="#000000")
notebook.add(aba_notas, text="Notas")

colunas_notas = ('Nome', 'Matéria', 'Nota 1', 'Nota 2', 'Nota 3', 'Média', 'Situação')
tabela_notas = ttk.Treeview(aba_notas, columns=colunas_notas, show='headings', selectmode='browse')
for col in colunas_notas:
    tabela_notas.heading(col, text=col)
    tabela_notas.column(col, anchor='center', width=120)
tabela_notas.pack(expand=True, fill='both', padx=10, pady=10)

# --- Aba Sobre ---
aba_sobre = tk.Frame(notebook, bg="#000000")
notebook.add(aba_sobre, text="Sobre")
label_sobre = tk.Label(
    aba_sobre,
    text="Sistema de Gestão Escolar Profissional\nDesenvolvido em Python com Tkinter.\n\nContato: seu@email.com",
    font=("Segoe UI", 14),
    bg="#000000",
    fg="#ffffff",
    justify="center"
)
label_sobre.pack(expand=True)

def atualizar_todas():
    atualizar_tabela()
    atualizar_tabela_notas()

atualizar_todas()
root.mainloop()