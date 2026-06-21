import tkinter as tk
import random

def mostrar_popup_virus():
    popup = tk.Tk()
    popup.title("⚠️ ATENÇÃO ⚠️")
    popup.geometry("600x400")
    popup.configure(bg='red')
    popup.attributes('-topmost', True)
    popup.protocol("WM_DELETE_WINDOW", lambda: None)
    texto = tk.Label(
        popup,
        text="🚨 VOCÊ ESTÁ COM VÍRUS! 🚨",
        font=("Arial", 60, "bold"),
        bg='red',
        fg='white'
    )
    texto.pack(expand=True, pady=20)
    subtitulo = tk.Label(
        popup,
        text="LIGUE IMEDIATAMENTE PARA O SUPORTE!",
        font=("Arial", 24, "bold"),
        bg='red',
        fg='yellow'
    )
    subtitulo.pack(pady=10)
    btn = tk.Button(
        popup,
        text="CLIQUE AQUI PARA REMOVER VÍRUS",
        font=("Arial", 20, "bold"),
        bg='yellow',
        fg='red',
        command=lambda: popup.destroy()
    )
    btn.pack(pady=30)
    icones = tk.Label(
        popup,
        text="⚠️ ⚠️ ⚠️ ⚠️ ⚠️",
        font=("Arial", 30),
        bg='red',
        fg='white'
    )
    icones.pack()
    popup.mainloop()
if __name__ == "__main__":
    mostrar_popup_virus()
