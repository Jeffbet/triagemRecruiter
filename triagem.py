import os
import shutil
import tkinter as tk
from tkinter import ttk, filedialog
from typing import Any

import fitz  # PyMuPDF
from docx import Document

# Caminhos/Diretórios
pasta_origem = ""
pasta_destino_filtrados = ""

def selecionar_diretorio_origem():
    global pasta_origem
    pasta_origem = filedialog.askdirectory()

def selecionar_diretorio_destino():
    global pasta_destino_filtrados
    pasta_destino_filtrados = filedialog.askdirectory()

def pesquisa_palavras_chave(texto, palavras_chave):
    return any(palavra.lower() in texto.lower() for palavra in palavras_chave)


def extrair_texto_de_pdf(caminho_pdf):
    texto = ""
    try:
        with fitz.open(caminho_pdf) as pdf_document:
            for pagina_numero in range(pdf_document.page_count):
                pagina = pdf_document[pagina_numero]
                texto += pagina.get_text()
    except Exception as e:
        print(f"Erro ao extrair texto do PDF: {e}")
    return texto


def extrair_texto_de_docx(caminho_docx):
    texto = ""
    try:
        document = Document(caminho_docx)
        for paragrafo in document.paragraphs:
            texto += paragrafo.text + "\n"
    except Exception as e:
        print(f"Erro ao extrair texto do arquivo DOCX: {e}")
    return texto


def filtrar_curriculos(palavras_chave, estado):
    curriculos_filtrados = []

    for curriculo in os.listdir(pasta_origem):
        caminho_curriculo = os.path.join(pasta_origem, curriculo)

        if os.path.isfile(caminho_curriculo):
            _, extensao = os.path.splitext(curriculo.lower())
            if extensao in {".txt", ".pdf", ".docx"}:
                conteudo = (
                    open(caminho_curriculo, "r", encoding="utf-8").read()
                    if extensao == ".txt"
                    else (
                        extrair_texto_de_pdf(caminho_curriculo)
                        if extensao == ".pdf"
                        else extrair_texto_de_docx(caminho_curriculo)
                    )
                )

                if pesquisa_palavras_chave(conteudo, palavras_chave) and (
                    estado.lower() == "todos" or estado.lower() in conteudo.lower()
                ):
                    curriculos_filtrados.append(curriculo)

    return curriculos_filtrados


def iniciar_triagem():
    if not pasta_origem or not pasta_destino_filtrados:
        # Verificar se os diretórios foram selecionados
        resultado_text.delete(1.0, tk.END)
        resultado_text.insert(tk.END, "Por favor, selecione os diretórios.")
        return

    # Remove widgets existentes na parte inferior da interface
    for widget in app.winfo_children():
        if widget.winfo_y() > 400:
            widget.destroy()

    # Adiciona um layout na parte inferior para indicar o carregamento
    loading_label = ttk.Label(
        app, text="Aguarde, realizando triagem...", style="TLabel"
    )
    loading_label.place(relx=0.5, rely=0.85, anchor="center")

    # Adiciona uma barra de progresso para indicar o carregamento
    progress_bar = ttk.Progressbar(
        app, orient="horizontal", length=300, mode="indeterminate", style="TProgressbar"
    )
    progress_bar.place(relx=0.5, rely=0.9, anchor="center")
    progress_bar.start()

    # Agora, a barra de carregamento e a mensagem de carregamento aparecerão por 2 segundos
    app.after(2000, processar_triagem)


def processar_triagem():
    palavras_chave = entrada_palavras_chave.get().split(
        ","
    )  # Obter palavras-chave do Entry
    palavras_chave = [
        palavra.strip() for palavra in palavras_chave
    ]  # Remover espaços em branco
    estado_selecionado = combo_estado.get()  # Obter estado selecionado

    try:
        if not os.path.exists(pasta_destino_filtrados):
            os.makedirs(pasta_destino_filtrados)

        curriculos_filtrados = filtrar_curriculos(palavras_chave, estado_selecionado)

        for curriculo in curriculos_filtrados:
            caminho_origem = os.path.join(pasta_origem, curriculo)
            caminho_destino = os.path.join(pasta_destino_filtrados, curriculo)
            shutil.copy2(caminho_origem, caminho_destino)

        resultado_text.delete(1.0, tk.END)
        resultado_text.insert(tk.END, "Currículos triados com sucesso!")
    except Exception as e:
        resultado_text.delete(1.0, tk.END)
        resultado_text.insert(tk.END, f"Erro durante a triagem: {e}")
    finally:
        # Remove widgets de carregamento após a triagem
        for widget in app.winfo_children():
            if widget.winfo_y() > 400:
                widget.destroy()


# Interface Gráfica
app = tk.Tk()
app.title("Ferramenta de Triagem de Currículos")
app.geometry("800x800")  # Define o tamanho da janela

style = ttk.Style(app)
style.configure("TButton", font=("Roboto", 18, "bold"), padding=10)
style.configure("TLabel", font=("Roboto", 18, "bold"), padding=10)
style.configure("TEntry", font=("Roboto", 18, "bold"), padding=10)
style.configure("TCombobox", font=("Roboto", 18, "bold"), padding=10)
style.configure("TProgressbar", thickness=10)

selecionar_diretorio_origem_button = ttk.Button(
    app, text="Selecionar Pasta do Banco de Talentos", command=selecionar_diretorio_origem, style="TButton"
)
selecionar_diretorio_origem_button.place(relx=0.5, rely=0.05, anchor="center")

selecionar_diretorio_destino_button = ttk.Button(
    app, text="Selecionar Pasta de Destino", command=selecionar_diretorio_destino, style="TButton"
)
selecionar_diretorio_destino_button.place(relx=0.5, rely=0.15, anchor="center")

entrada_palavras_chave_label = ttk.Label(
    app, text="Palavras-chave (separadas por vírgula):", style="TLabel"
)
entrada_palavras_chave_label.place(relx=0.5, rely=0.25, anchor="center")

entrada_palavras_chave = ttk.Entry(app, width=50, style="TEntry")
entrada_palavras_chave.place(relx=0.5, rely=0.35, anchor="center")

estado_label = ttk.Label(app, text="Selecione o estado:", style="TLabel")
estado_label.place(relx=0.5, rely=0.45, anchor="center")

# Lista de estados brasileiros
estados: list[str | Any] = [
    "Acre",
    "Alagoas",
    "Amapá",
    "Amazonas",
    "Bahia",
    "Ceará",
    "Espírito Santo",
    "Goiás",
    "Maranhão",
    "Mato Grosso",
    "Mato Grosso do Sul",
    "Minas Gerais",
    "Pará",
    "Paraíba",
    "Paraná",
    "Pernambuco",
    "Piauí",
    "Rio de Janeiro",
    "Rio Grande do Norte",
    "Rio Grande do Sul",
    "Rondônia",
    "Roraima",
    "Santa Catarina",
    "São Paulo",
    "Sergipe",
    "Tocantins",
    "Todos",
]

# Adiciona "Todos" à lista de estados
# Variável para armazenar o estado selecionado
combo_estado = tk.StringVar()
combo_estado.set(estados[0])  # Estado padrão

# Dropdown (menu suspenso) para selecionar o estado
estado_combobox = ttk.Combobox(
    app, textvariable=combo_estado, values=estados, style="TCombobox"
)
estado_combobox.place(relx=0.5, rely=0.55, anchor="center")

iniciar_triagem_button = ttk.Button(
    app, text="Iniciar Triagem", command=iniciar_triagem, style="TButton"
)
iniciar_triagem_button.place(relx=0.5, rely=0.65, anchor="center")

resultado_text = tk.Text(app, height=10, width=50, font=("Roboto", 14))
resultado_text.place(relx=0.5, rely=0.85, anchor="center")


app.mainloop()
# Deus me codificou!
