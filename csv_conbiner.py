import os
import pandas as pd
from datetime import datetime
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

def selecionar_pasta():
    """
    Abre uma janela para o usuário escolher a pasta.
    O caminho selecionado é inserido no campo de entrada.
    """
    pasta = filedialog.askdirectory()
    if pasta:
        entrada_pasta.delete(0, tk.END)  # Apaga texto atual
        entrada_pasta.insert(0, pasta)   # Insere caminho escolhido

def processar_csv():
    """
    Lê todos os arquivos CSV da pasta escolhida,
    adiciona a coluna 'Data de Processamento',
    junta em um único arquivo e salva.
    """
    pasta_entrada = entrada_pasta.get()
    nome_arquivo_final = entrada_nome.get()

    # Valida se os campos foram preenchidos
    if not pasta_entrada or not nome_arquivo_final:
        messagebox.showerror("Erro", "Preencha todos os campos!")
        return

    # Garante que o arquivo final terá extensão .csv
    if not nome_arquivo_final.lower().endswith(".csv"):
        nome_arquivo_final += ".csv"

    caminho_saida = os.path.join(pasta_entrada, nome_arquivo_final)

    # Lista para armazenar os DataFrames
    lista_df = []

    # Lista de arquivos CSV na pasta
    arquivos_csv = [f for f in os.listdir(pasta_entrada) if f.lower().endswith(".csv")]

    # Se não houver arquivos, avisa e para
    if not arquivos_csv:
        messagebox.showwarning("Aviso", "Nenhum arquivo CSV encontrado.")
        return

    # Configura barra de progresso
    barra["maximum"] = len(arquivos_csv)
    barra["value"] = 0

    try:
        for i, arquivo in enumerate(arquivos_csv, start=1):
            caminho_arquivo = os.path.join(pasta_entrada, arquivo)

            # Lê o CSV
            df = pd.read_csv(caminho_arquivo)

            # Adiciona a coluna de data
            df["Data de Processamento"] = datetime.now().strftime("%Y-%m-%d")

            # Adiciona à lista final
            lista_df.append(df)

            # Atualiza barra de progresso
            barra["value"] = i
            janela.update_idletasks()  # Atualiza interface

        # Junta todos os DataFrames
        df_final = pd.concat(lista_df, ignore_index=True)

        # Salva o arquivo final
        df_final.to_csv(caminho_saida, index=False, encoding="utf-8-sig")

        # Mensagem de sucesso
        messagebox.showinfo("Sucesso", f"Arquivo salvo em:\n{caminho_saida}")

    except Exception as e:
        messagebox.showerror("Erro", str(e))


# === INTERFACE GRÁFICA (Tkinter) ===

# Cria a janela principal
janela = tk.Tk()
janela.title("Unir CSVs com Data de Processamento")
janela.geometry("450x250")

# Rótulo e campo para escolher pasta
tk.Label(janela, text="Pasta de Entrada:").pack(pady=5)
frame_pasta = tk.Frame(janela)
frame_pasta.pack()
entrada_pasta = tk.Entry(frame_pasta, width=35)
entrada_pasta.pack(side=tk.LEFT, padx=5)
btn_pasta = tk.Button(frame_pasta, text="Selecionar", command=selecionar_pasta)
btn_pasta.pack(side=tk.LEFT)

# Rótulo e campo para nome do arquivo final
tk.Label(janela, text="Nome do Arquivo Final:").pack(pady=5)
entrada_nome = tk.Entry(janela, width=40)
entrada_nome.pack()

# Barra de progresso
barra = ttk.Progressbar(janela, length=300, mode="determinate")
barra.pack(pady=15)

# Botão para iniciar o processamento
tk.Button(janela, text="Processar", command=processar_csv, bg="green", fg="white").pack(pady=10)

# Inicia o loop da janela
janela.mainloop()
