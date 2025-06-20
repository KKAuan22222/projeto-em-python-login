import tkinter as tk
import random

# Função para iniciar/reiniciar o jogo
def iniciar_jogo():
    global numero_secreto, tentativas
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    entry_palpite.delete(0, tk.END)
    label_resultado.config(text="Tente adivinhar o número entre 1 e 100!", fg="white")

def verificar_palpite():
    global tentativas
    try:
        palpite = int(entry_palpite.get())
    except ValueError:
        label_resultado.config(text="Digite um número válido!", fg="red")
        return

    tentativas += 1
    if palpite < numero_secreto:
        label_resultado.config(text="Tente um número maior!", fg="yellow")
    elif palpite > numero_secreto:
        label_resultado.config(text="Tente um número menor!", fg="yellow")
    else:
        label_resultado.config(
            text=f"Parabéns! Você acertou em {tentativas} tentativas!", fg="lime"
        )

# Janela principal
root = tk.Tk()
root.title("Jogo de Adivinhação")
root.geometry("400x250")
root.configure(bg="#222222")

# Título
label_titulo = tk.Label(root, text="Jogo de Adivinhação", font=("Arial", 18, "bold"), bg="#222222", fg="cyan")
label_titulo.pack(pady=10)

# Instrução
label_instrucao = tk.Label(root, text="Adivinhe o número entre 1 e 100", font=("Arial", 12), bg="#222222", fg="white")
label_instrucao.pack()

# Campo de entrada
entry_palpite = tk.Entry(root, font=("Arial", 14), justify="center")
entry_palpite.pack(pady=10)

# Botão de verificar
btn_verificar = tk.Button(root, text="Verificar", font=("Arial", 12, "bold"), bg="cyan", fg="black", command=verificar_palpite)
btn_verificar.pack(pady=5)

# Resultado
label_resultado = tk.Label(root, text="", font=("Arial", 12), bg="#222222", fg="white")
label_resultado.pack(pady=10)

# Botão de novo jogo
btn_novo = tk.Button(root, text="Novo Jogo", font=("Arial", 10), bg="#444444", fg="white", command=iniciar_jogo)
btn_novo.pack(pady=5)

# Iniciar o jogo pela primeira vez
iniciar_jogo()

root.mainloop()