"""
Script para criar executável do aplicativo Upload Drive

Este script utiliza PyInstaller para criar um executável standalone (.exe)
do aplicativo Upload Drive. O executável inclui todas as dependências
necessárias e pode ser distribuído sem necessidade de Python instalado.

Uso:
    python build_executavel.py

O executável será criado em: dist/UploadDrive-v2.exe

Autor: Samuel Else full stack developer
Licença: MIT
"""

import PyInstaller.__main__
import os
import sys

# Configurações do PyInstaller
args = [
    'upload_drive.py',                    # Script principal
    '--name=UploadDrive-v2',              # Nome do executável com versão
    '--onefile',                          # Criar um único arquivo executável
    '--windowed',                         # Não mostrar console (GUI apenas)
    '--icon=NONE',                        # Sem ícone (pode adicionar .ico depois)
    '--add-data=credentials.json;.',      # Incluir credentials.json se existir
    '--hidden-import=PyQt5.QtCore',       # Importações ocultas necessárias
    '--hidden-import=PyQt5.QtGui',
    '--hidden-import=PyQt5.QtWidgets',
    '--hidden-import=google.oauth2.credentials',
    '--hidden-import=google_auth_oauthlib.flow',
    '--hidden-import=googleapiclient.discovery',
    '--collect-all=google_auth_oauthlib',  # Coletar todos os módulos do pacote
    '--collect-all=googleapiclient',
    '--clean',                            # Limpar cache antes de construir
]

# Verificar se credentials.json existe
# IMPORTANTE: Por padrão, NÃO incluímos credentials.json no executável
# para que cada usuário use suas próprias credenciais
if not os.path.exists('credentials.json'):
    print("="*60)
    print("AVISO: Arquivo 'credentials.json' não encontrado!")
    print("="*60)
    print("\nO executável será criado SEM o arquivo credentials.json.")
    print("Cada usuário precisará criar seu próprio credentials.json seguindo")
    print("as instruções em docs/CRIAR_PROJETO_E_VINCULAR.md")
    print("\n" + "="*60)
    # Remover a linha que adiciona credentials.json
    args = [arg for arg in args if not arg.startswith('--add-data=credentials.json')]
else:
    print("="*60)
    print("AVISO: Arquivo 'credentials.json' encontrado!")
    print("="*60)
    print("\nPor padrão, o executável NÃO incluirá o credentials.json")
    print("para proteger suas credenciais e permitir que cada usuário")
    print("use suas próprias credenciais do Google Cloud.")
    print("\nSe você realmente quiser incluir, descomente a linha abaixo.")
    print("Mas NÃO faça commit do executável com credenciais no GitHub!")
    print("="*60)
    # Por padrão, não incluir credentials.json
    args = [arg for arg in args if not arg.startswith('--add-data=credentials.json')]
    # Se quiser incluir, descomente a linha abaixo:
    # args.append('--add-data=credentials.json;.')

print("Iniciando construção do executável...")
print("Isso pode levar alguns minutos...")

try:
    PyInstaller.__main__.run(args)
    print("\n" + "="*50)
    print("Executável criado com sucesso!")
    print("Arquivo: dist/UploadDrive-v2.exe")
    print("="*50)
    if os.path.exists('credentials.json'):
        print("\n✓ O arquivo credentials.json foi incluído no executável!")
        print("  Você pode distribuir apenas o UploadDrive-v2.exe")
    else:
        print("\n⚠ Lembre-se de colocar o credentials.json na mesma pasta do executável")
except Exception as e:
    print(f"\nErro ao criar executável: {e}")
    sys.exit(1)

