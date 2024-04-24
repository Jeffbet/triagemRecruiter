# Ferramenta de Triagem de Currículos para RH

Este é um aplicativo para triagem de currículos desenvolvido para o setor de Recursos Humanos (RH). O objetivo é automatizar o processo de triagem de currículos para identificar candidatos que atendam aos critérios específicos de seleção.

## Funcionalidades

- **Filtragem por Palavras-chave:** Permite filtrar os currículos com base em palavras-chave específicas, como habilidades, tecnologias ou experiência relevante.
  
- **Filtragem por Estado:** Possibilita a filtragem dos currículos por estado de residência do candidato.

- **Suporte a Diferentes Formatos de Arquivo:** Aceita currículos nos formatos de arquivo TXT, PDF e DOCX.

- **Interface Gráfica de Usuário (GUI):** Oferece uma interface gráfica intuitiva para facilitar a interação com o aplicativo.

## Tecnologias Utilizadas

- **Python:** Linguagem de programação utilizada para desenvolver a lógica do aplicativo.

- **Tkinter:** Biblioteca padrão do Python para criação de interfaces gráficas.

- **PyMuPDF:** Biblioteca para manipulação de arquivos PDF.

- **python-docx:** Biblioteca para manipulação de arquivos DOCX.

## Como Usar

1. Clone este repositório para o seu ambiente de desenvolvimento local.

2. Certifique-se de ter o Python instalado em seu sistema.

3. Instale as dependências necessárias executando o seguinte comando:
   
   ```bash
   pip install -r requirements.txt

4. Para criar um executável, utilize o PyInstaller. Na linha de comando, navegue até o diretório onde está o arquivo triagem.py e execute o seguinte comando:
   
   ```bash
   pyinstaller --onefile triagem.py

5. Para executar o aplicativo, navegue até o diretório onde está o arquivo triagem.exe e execute o seguinte comando:
   
   ```bash
   triagem.exe

6. Para criar um instalador para distribuir sua aplicação, você pode usar o Inno Setup. O Inno Setup é uma ferramenta gratuita para criar instaladores para programas do Windows. Você pode baixá-lo em Inno Setup - Downloads. Na linha de comando, navegue até o diretório onde está o arquivo triagem.py e execute o seguinte comando:
   
   ```bash
   innosetup.exe triagem.iss

7. Após instalar o Inno Setup, você pode criar um script de instalação (.iss) para sua aplicação. Aqui está um exemplo básico de script de instalação: 

[Setup]
AppName=Ferramenta de Triagem de Currículos
AppVersion=1.0
DefaultDirName={pf}\TriagemCurriculos
DisableDirPage=yes
DisableProgramGroupPage=yes
OutputDir=userdocs:Inno Setup Output
OutputBaseFilename=FerramentaTriagemCurriculosSetup
Compression=lzma
SolidCompression=yes

[Files]
Source: "dist\triagem.exe"; DestDir: "{app}"

[Icons]
Name: "{commondesktop}\Ferramenta de Triagem de Currículos"; Filename: "{app}\triagem.exe"

Salve este script como instalador.iss no mesmo diretório onde você tem o executável triagem.exe. Este script incluirá o executável triagem.exe no instalador e criará um atalho na área de trabalho.  

8. Compile o script de instalação (.iss) usando o Inno Setup Compiler. Isso criará um instalador executável para sua aplicação.

9. Distribua o instalador para os usuários finais. Eles podem executá-lo para instalar sua aplicação em seus sistemas Windows.


## Como Usar a Interface

Execute o aplicativo executando o arquivo triagem.exe.

Na interface do aplicativo, busque no seu computador a pasta onde está os currículos, após selecione a pasta de destino onde ficarão os 
currículos triados, insira as palavras-chave desejadas e selecione o estado de residência, em seguida, clique no botão "Iniciar Triagem".

Os currículos que atendem aos critérios de seleção serão movidos para a pasta "CurriculosFiltrados".

## Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir um Pull Request para sugerir melhorias, adicionar novos recursos ou corrigir problemas.

## Autor
Jefferson Ricardo Fonseca - arielfonsek5@gmail.com

## Licença
Este projeto é licenciado sob a MIT License.



