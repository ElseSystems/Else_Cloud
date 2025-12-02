# 🚀 Guia de Setup para GitHub

Este guia ajuda você a preparar o projeto para fazer upload no GitHub como portfólio.

## ✅ Checklist Antes de Fazer Upload

- [x] ✅ Código organizado e limpo
- [x] ✅ Documentação completa (README.md)
- [x] ✅ .gitignore configurado
- [x] ✅ Arquivos sensíveis protegidos (credentials.json no .gitignore)
- [x] ✅ Estrutura de pastas organizada
- [x] ✅ Licença adicionada (MIT)
- [x] ✅ Guia de contribuição criado

## 📋 Passos para Fazer Upload no GitHub

### 1. Criar Repositório no GitHub

1. Acesse [GitHub](https://github.com)
2. Clique em **"New repository"** ou **"Novo repositório"**
3. Preencha:
   - **Nome**: `upload-drive` (ou outro nome de sua escolha)
   - **Descrição**: "Sistema moderno de upload para Google Drive com interface gráfica"
   - **Visibilidade**: Público (para portfólio)
   - **NÃO** marque "Initialize with README" (já temos um)
4. Clique em **"Create repository"**

### 2. Inicializar Git Localmente

```bash
# Inicializar repositório Git
git init

# Adicionar todos os arquivos
git add .

# Fazer commit inicial
git commit -m "Initial commit: Upload Drive - Sistema de upload para Google Drive"

# Adicionar remote do GitHub (substitua SEU-USUARIO pelo seu usuário)
git remote add origin https://github.com/SEU-USUARIO/upload-drive.git

# Renomear branch para main (se necessário)
git branch -M main

# Fazer push
git push -u origin main
```

### 3. Verificar Arquivos Sensíveis

**IMPORTANTE:** Certifique-se de que estes arquivos NÃO estão no Git:

```bash
# Verificar se credentials.json está sendo ignorado
git check-ignore credentials.json

# Se retornar o caminho, está OK. Se não retornar nada, adicione ao .gitignore
```

**Arquivos que NUNCA devem ir para o GitHub:**
- ❌ `credentials.json` (contém credenciais OAuth)
- ❌ `token.pickle` (contém tokens de autenticação)
- ❌ `build/` (arquivos temporários de build)
- ❌ `dist/*.exe` (executáveis - especialmente se contiverem credenciais)
- ❌ `__pycache__/` (cache do Python)

⚠️ **IMPORTANTE:** Se você criou um executável com `credentials.json` incluído, **NÃO** faça commit dele no GitHub!

### 4. Estrutura Final no GitHub

Seu repositório deve ter esta estrutura:

```
upload-drive/
├── .gitignore
├── LICENSE
├── README.md
├── CONTRIBUTING.md
├── requirements.txt
├── upload_drive.py
├── build_executavel.py
├── credentials.json.example
└── docs/
    ├── README.md
    ├── CRIAR_PROJETO_E_VINCULAR.md
    ├── CONFIGURAR_OAUTH_PUBLICO.md
    ├── GUIA_COMPLETO_OAUTH.md
    ├── COMO_PUBLICAR_NA_NOVA_INTERFACE.md
    └── COMO_USAR_EXECUTAVEL.md
```

## 🎨 Personalizar README para Portfólio

### Adicionar Badges

Você pode adicionar badges no topo do README.md:

```markdown
![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![PyQt5](https://img.shields.io/badge/PyQt5-5.15.9-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)
```

### Adicionar Screenshots

1. Tire screenshots da aplicação
2. Crie uma pasta `screenshots/` (adicione ao .gitignore se necessário)
3. Adicione no README:

```markdown
## 📸 Screenshots

![Interface Principal](screenshots/interface.png)
![Upload em Progresso](screenshots/upload.png)
```

## 🔒 Segurança

### Verificar Antes de Fazer Push

```bash
# Ver o que será commitado
git status

# Ver diferenças
git diff

# Se credentials.json aparecer, NÃO faça commit!
```

### Se Acidentalmente Commitar Credenciais

Se você acidentalmente fez commit de `credentials.json`:

1. **IMEDIATAMENTE** revogue as credenciais no Google Cloud Console
2. Crie novas credenciais
3. Remova do histórico do Git:
```bash
git filter-branch --force --index-filter \
  "git rm --cached --ignore-unmatch credentials.json" \
  --prune-empty --tag-name-filter cat -- --all
```

## 📝 Boas Práticas

- ✅ Commits descritivos e claros
- ✅ README completo e profissional
- ✅ Código bem documentado
- ✅ Estrutura organizada
- ✅ .gitignore configurado corretamente
- ✅ Licença incluída

## 🎯 Próximos Passos

Após fazer upload:

1. ✅ Adicionar descrição no repositório GitHub
2. ✅ Adicionar tags/tópicos (python, pyqt5, google-drive, gui)
3. ✅ Criar releases (se quiser versionar)
4. ✅ Adicionar ao seu portfólio pessoal

## 💡 Dicas

- Use commits frequentes e descritivos
- Mantenha o README atualizado
- Responda a issues e pull requests
- Adicione screenshots para melhor apresentação

---

**Pronto!** Seu projeto está organizado e pronto para ser um excelente item no seu portfólio! 🚀

