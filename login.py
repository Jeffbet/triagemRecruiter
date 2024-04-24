import tkinter as tk
from tkinter import ttk
import webbrowser
import subprocess

def fazer_login():
    # Esta função verifica se o nome de usuário e senha correspondem ao usuário=tech e senha= recruiter
    if nome_usuario_entry.get() == "tech" and senha_entry.get() == "recruiter":
        print("Login bem-sucedido! Redirecionando para a triagem...")
        abrir_triagem()
    else:
        print("Nome de usuário ou senha incorretos!")

def abrir_triagem():
    # Adicionei aqui a lógica para abrir o diretório onde o arquivo triagem.py está localizado
    diretorio_triagem = r"C:\Users\ariel\OneDrive\Documentos\Área de Desenvolvimento\triagem\triagem.py"
    subprocess.Popen(["python", diretorio_triagem])

def abrir_whatsapp():
    webbrowser.open("https://wa.me/5583987444607")

# Cria a janela principal
root = tk.Tk()
root.title("Login")

# Defini o tamanho da janela
largura = 450
altura = 200
largura_tela = root.winfo_screenwidth()
altura_tela = root.winfo_screenheight()
pos_x = (largura_tela - largura) // 2
pos_y = (altura_tela - altura) // 2
root.geometry(f"{largura}x{altura}+{pos_x}+{pos_y}")

# Adiciona bordas
root.configure(borderwidth=5, relief="ridge")

# Cria rótulos e campos de entrada
tk.Label(root, text="Nome de Usuário:").grid(row=0, column=0, padx=10, pady=(20, 5), sticky="e")
nome_usuario_entry = ttk.Entry(root)
nome_usuario_entry.grid(row=0, column=1, padx=10, pady=(20, 5))
tk.Label(root, text="Senha:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
senha_entry = ttk.Entry(root, show="*")
senha_entry.grid(row=1, column=1, padx=10, pady=5)

# Botão de login
login_button = ttk.Button(root, text="Login", command=fazer_login)
login_button.grid(row=2, columnspan=2, pady=10)

# Rodapé
rodape_frame = tk.Frame(root, borderwidth=0)
rodape_frame.grid(row=4, columnspan=2, sticky="s", pady=(0, 10))

direitos_reservados_label = tk.Label(rodape_frame, text="Direitos reservados Jefferson Ricardo developer", font=("Arial", 8))
direitos_reservados_label.pack(side="left", padx=10)

whatsapp_button = ttk.Button(rodape_frame, text="Contato WhatsApp", command=abrir_whatsapp)
whatsapp_button.pack(side="right", padx=10)

# Executar aplicação
root.mainloop()
