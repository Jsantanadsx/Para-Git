import tkinter as tk

# PopUp

janela = tk.Tk()
janela.title("Semáforo")

canvas = tk.Canvas(janela, width=200, height=400, bg="black")
canvas.pack()

# Criando as luzes

vermelho = canvas.create_oval(50, 50, 150, 150, fill="gray")
amarelo = canvas.create_oval(50, 170, 150, 270, fill="gray")
verde = canvas.create_oval(50, 290, 150, 390, fill="gray")

# Função de controle para o semáforo

estado = 0 

def atualizar_semaforo():
    global estado

    # Apaga todas as luzes (deixa cinza)
    canvas.itemconfig(vermelho, fill="gray")
    canvas.itemconfig(amarelo, fill="gray")
    canvas.itemconfig(verde, fill="gray")

    if estado == 0:
        canvas.itemconfig(verde, fill="green")
        estado = 1
        janela.after(5000, atualizar_semaforo)
    
    elif estado == 1:
        canvas.itemconfig(amarelo, fill="yellow")
        estado = 2
        janela.after(2500, atualizar_semaforo)

    elif estado == 2:
        canvas.itemconfig(vermelho, fill="red")
        estado = 0
        janela.after(5000, atualizar_semaforo)

# Inicia o ciclo
atualizar_semaforo()

janela.mainloop()
