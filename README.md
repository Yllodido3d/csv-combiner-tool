CSV Combiner
A simple Python application that combines multiple CSV files from a selected folder into a single CSV file, adding a "Processing Date" column to the output. The tool features a user-friendly graphical interface built with Tkinter.

🇧🇷 Descrição (Português)
Este é um programa em Python que permite combinar vários arquivos CSV de uma pasta específica em um único arquivo CSV. Ele adiciona uma coluna "Data de Processamento" com a data atual a cada linha do arquivo resultante.
A interface gráfica, construída com Tkinter, facilita a escolha da pasta e a definição do nome do arquivo final.
Funcionalidades

Seleção de pasta com arquivos CSV através de uma interface gráfica.
Combinação de todos os arquivos CSV em um único arquivo.
Adição de uma coluna "Data de Processamento" com a data atual (formato AAAA-MM-DD).
Barra de progresso para acompanhar o processamento.
Suporte a codificação UTF-8 para compatibilidade com caracteres especiais.
Mensagens de erro ou sucesso para feedback ao usuário.


🇺🇸 Description (English)
This is a Python program that combines multiple CSV files from a specified folder into a single CSV file. It adds a "Processing Date" column with the current date to each row of the resulting file.
The graphical interface, built with Tkinter, makes it easy to select the folder and specify the output file name.
Features

Folder selection for CSV files via a graphical interface.
Merging of all CSV files into a single file.
Addition of a "Processing Date" column with the current date (YYYY-MM-DD format).
Progress bar to track processing.
UTF-8 encoding support for compatibility with special characters.
Error and success messages for user feedback.


Requisitos / Requirements

Python 3.x
Bibliotecas Python necessárias / Required Python libraries:
pandas
tkinter (usually included with Python)


Sistema operacional / Operating system: Windows, macOS, or Linux

Instalação / Installation

Certifique-se de ter o Python instalado / Ensure Python is installed.
Instale a biblioteca pandas com / Install the pandas library using:pip install pandas


Clone ou baixe este repositório / Clone or download this repository.
Execute o script csv_combiner.py / Run the csv_combiner.py script.


Como Usar / How to Use

Execute o programa / Run the program:python csv_combiner.py


Na interface gráfica / In the graphical interface:
Clique em "Selecionar" para escolher a pasta com os arquivos CSV / Click "Select" to choose the folder containing CSV files.
Insira o nome do arquivo final (sem extensão, será adicionado .csv automaticamente) / Enter the name of the output file (without extension, .csv will be added automatically).
Clique em "Processar" para combinar os arquivos / Click "Process" to combine the files.


O arquivo combinado será salvo na mesma pasta escolhida / The combined file will be saved in the selected folder.
Verifique as mensagens de erro ou sucesso / Check the error or success messages for feedback.


Exemplo / Example
Arquivos de entrada / Input files:

dados1.csv:Nome,Idade
Ana,25
João,30


dados2.csv:Nome,Idade
Maria,28
Pedro,35



Arquivo de saída / Output file (resultado.csv):
Nome,Idade,Data de Processamento
Ana,25,2025-08-16
João,30,2025-08-16
Maria,28,2025-08-16
Pedro,35,2025-08-16


Contribuições / Contributions
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests com melhorias ou correções de bugs. / Contributions are welcome! Feel free to open issues or pull requests with improvements or bug fixes.

Licença / License
Este projeto está licenciado sob a MIT License. / This project is licensed under the MIT License.

Contato / Contact
Para dúvidas ou sugestões, abra uma issue no repositório. / For questions or suggestions, open an issue in the repository.
