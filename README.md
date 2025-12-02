# 🚀 Upload Drive - Sistema Avançado de Upload para Google Drive

<div align="center">

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![PyQt5](https://img.shields.io/badge/PyQt5-5.15.9-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

**Sistema moderno e futurista para upload automático de arquivos para o Google Drive com interface gráfica intuitiva.**

[Características](#-características) • [Instalação](#-instalação) • [Configuração](#-configuração) • [Uso](#-uso) • [Build](#-build) • [Documentação](#-documentação)

</div>

---

## ✨ Características

- 🎨 **Interface Moderna**: Design futurista com tema escuro e cores vibrantes
- 🔐 **Gerenciamento de Conta**: Conecte e desconecte facilmente sua conta Google
- 📤 **Upload Automático**: Envia todos os arquivos de uma pasta automaticamente
- 🔗 **Links Públicos**: Gera links públicos para todos os arquivos enviados
- 📁 **Nomes Inteligentes**: Arquivo de links nomeado com o nome da pasta
- 🚀 **Executável Standalone**: Crie um .exe para distribuição sem precisar de Python
- ✅ **Suporte Completo**: Vídeos, imagens, documentos e qualquer tipo de arquivo

---

## 📋 Pré-requisitos

- Python 3.7 ou superior
- Conta Google com acesso ao Google Drive
- Projeto no Google Cloud Platform com API do Google Drive ativada

---

## 🚀 Instalação

### Clone o repositório

```bash
git clone https://github.com/seu-usuario/upload-drive.git
cd upload-drive
```

### Instale as dependências

```bash
pip install -r requirements.txt
```

---

## ⚙️ Configuração

### 1. Criar Projeto no Google Cloud Console

1. Acesse [Google Cloud Console](https://console.cloud.google.com)
2. Crie um novo projeto
3. Ative a API do Google Drive
4. Configure a Tela de Consentimento OAuth (tipo: Externo)
5. Crie credenciais OAuth 2.0 (tipo: Aplicativo de desktop)

📖 **Guia completo:** Veja [docs/CRIAR_PROJETO_E_VINCULAR.md](docs/CRIAR_PROJETO_E_VINCULAR.md)

### 2. Configurar Credenciais

1. Baixe o arquivo JSON das credenciais OAuth
2. Renomeie para `credentials.json`
3. Coloque na raiz do projeto (mesma pasta do `upload_drive.py`)

⚠️ **IMPORTANTE:** O arquivo `credentials.json` contém informações sensíveis. **NUNCA** faça commit deste arquivo no GitHub!

### 3. Tornar o App Público (Opcional)

Para permitir que qualquer conta Google use o app:

1. Acesse: APIs e Serviços → Tela de Consentimento OAuth
2. Clique em "PUBLICAR APP"
3. Confirme a publicação

📖 **Guia detalhado:** Veja [docs/CONFIGURAR_OAUTH_PUBLICO.md](docs/CONFIGURAR_OAUTH_PUBLICO.md)

---

## 🎮 Uso

### Executar o Programa

```bash
python upload_drive.py
```

### Como Usar

1. **Conectar Conta**: Clique em "🔗 Conectar Conta" e autorize no navegador
2. **Selecionar Pasta**: Clique em "📂 Selecionar Pasta" e escolha a pasta com os arquivos
3. **Iniciar Upload**: Clique em "🚀 Iniciar Upload" e aguarde
4. **Links Gerados**: Os links serão salvos em `link{nome_da_pasta}.txt`

### Exemplo

```
Pasta selecionada: "Minhas Fotos"
→ Arquivo gerado: linkMinhas Fotos.txt
```

---

## 🔨 Build - Criar Executável

### Opção 1: Script Automático

```bash
python build_executavel.py
```

O executável será criado em `dist/UploadDrive-v2.exe`

### Opção 2: PyInstaller Manual

```bash
pyinstaller --name=UploadDrive --onefile --windowed upload_drive.py
```

📖 **Instruções detalhadas:** Veja [docs/COMO_USAR_EXECUTAVEL.md](docs/COMO_USAR_EXECUTAVEL.md)

---

## 📁 Estrutura do Projeto

```
upload-drive/
├── upload_drive.py              # Programa principal
├── build_executavel.py          # Script para criar executável
├── requirements.txt             # Dependências Python
├── README.md                    # Documentação principal
├── LICENSE                      # Licença MIT
├── CONTRIBUTING.md              # Guia de contribuição
├── .gitignore                   # Arquivos ignorados pelo Git
├── credentials.json.example     # Exemplo de estrutura do credentials.json
├── docs/                        # Documentação detalhada
│   ├── README.md
│   ├── CRIAR_PROJETO_E_VINCULAR.md
│   ├── CONFIGURAR_OAUTH_PUBLICO.md
│   ├── GUIA_COMPLETO_OAUTH.md
│   ├── COMO_PUBLICAR_NA_NOVA_INTERFACE.md
│   └── COMO_USAR_EXECUTAVEL.md
└── credentials.json             # ⚠️ NÃO COMMITAR! (criar localmente)
```

---

## 🔧 Configuração Avançada

### Criar seu próprio credentials.json

⚠️ **IMPORTANTE:** Cada usuário precisa criar seu próprio arquivo `credentials.json` com suas próprias credenciais do Google Cloud. O projeto não inclui credenciais pré-configuradas por questões de segurança.

**📖 Guia completo passo a passo:** Veja [docs/CRIAR_PROJETO_E_VINCULAR.md](docs/CRIAR_PROJETO_E_VINCULAR.md)

**Estrutura do arquivo (exemplo):**
```json
{
  "installed": {
    "client_id": "SEU-CLIENT-ID-AQUI.apps.googleusercontent.com",
    "project_id": "seu-projeto-id",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_secret": "SEU-CLIENT-SECRET-AQUI",
    "redirect_uris": ["http://localhost"]
  }
}
```

**Resumo rápido:**
1. Acesse [Google Cloud Console](https://console.cloud.google.com)
2. Crie um novo projeto (se ainda não tiver)
3. Ative a API do Google Drive
4. Configure a Tela de Consentimento OAuth (tipo: Externo)
5. Crie credenciais OAuth 2.0 (tipo: Aplicativo de desktop)
6. Baixe o arquivo JSON e renomeie para `credentials.json`
7. Coloque na raiz do projeto (mesma pasta do `upload_drive.py`)

⚠️ **SEGURANÇA:** 
- **NUNCA** faça commit do arquivo `credentials.json` no GitHub!
- Mantenha suas credenciais seguras e privadas
- Use `credentials.json.example` apenas como referência da estrutura
- Cada usuário deve usar suas próprias credenciais

### Personalizar Interface

As cores e estilos podem ser ajustados no método `apply_futuristic_style()` em `upload_drive.py`:

```python
def apply_futuristic_style(self):
    """Aplica estilo futurista à janela principal"""
    self.setStyleSheet("""
        QMainWindow {
            background: qlineargradient(...);
        }
        ...
    """)
```

---

## 📚 Documentação

Toda a documentação está na pasta `docs/`:

- **[CRIAR_PROJETO_E_VINCULAR.md](docs/CRIAR_PROJETO_E_VINCULAR.md)** - Guia completo para criar projeto e vincular ao app
- **[CONFIGURAR_OAUTH_PUBLICO.md](docs/CONFIGURAR_OAUTH_PUBLICO.md)** - Como tornar o app público
- **[GUIA_COMPLETO_OAUTH.md](docs/GUIA_COMPLETO_OAUTH.md)** - Guia detalhado de configuração OAuth
- **[COMO_PUBLICAR_NA_NOVA_INTERFACE.md](docs/COMO_PUBLICAR_NA_NOVA_INTERFACE.md)** - Publicar app na nova interface do Google Cloud
- **[COMO_USAR_EXECUTAVEL.md](docs/COMO_USAR_EXECUTAVEL.md)** - Como usar o executável gerado

---

## 🐛 Solução de Problemas

### Erro: "credentials.json não encontrado"

- Certifique-se de que o arquivo está na mesma pasta do `upload_drive.py`
- Verifique se o nome está exatamente `credentials.json` (sem espaços, tudo minúsculo)

### Erro: "403: access_denied"

- O app está em modo de teste. Veja [docs/CONFIGURAR_OAUTH_PUBLICO.md](docs/CONFIGURAR_OAUTH_PUBLICO.md)
- Ou adicione seu email em "Usuários de teste" no Google Cloud Console

### Erro ao criar executável

- Certifique-se de que o PyInstaller está instalado: `pip install pyinstaller`
- Verifique se todas as dependências estão instaladas: `pip install -r requirements.txt`

---

## 🔒 Segurança

⚠️ **IMPORTANTE:**

- **NUNCA** faça commit do arquivo `credentials.json` no GitHub
- **NUNCA** compartilhe publicamente seu `client_secret`
- O arquivo `token.pickle` contém tokens de autenticação - mantenha seguro
- Use `.gitignore` para proteger arquivos sensíveis

---

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

---

## 👨‍💻 Autor

Samuel Else fullstack developer  .

---

## 🙏 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou pull request.

---

## 📞 Suporte

Para dúvidas ou problemas:

1. Verifique a [documentação](docs/)
2. Abra uma [issue](https://github.com/seu-usuario/upload-drive/issues)
3. Consulte os [guias de configuração](docs/)

---

<div align="center">

**⭐ Se este projeto foi útil, considere dar uma estrela! ⭐**

</div>
