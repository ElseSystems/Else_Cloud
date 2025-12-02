# Como Usar o Executável em Outra Máquina

## ✅ Executável Criado com Sucesso!

O arquivo executável foi criado em: **`dist/UploadDrive.exe`**

## 📦 O que você precisa para usar em outra máquina:

⚠️ **IMPORTANTE:** Por padrão, o executável **NÃO** inclui o arquivo `credentials.json` para proteger suas credenciais e permitir que cada usuário use suas próprias credenciais.

### Você precisará:

1. **`dist/UploadDrive-v2.exe`** - O executável principal
2. **`credentials.json`** - Você precisa criar seu próprio arquivo seguindo as instruções em [CRIAR_PROJETO_E_VINCULAR.md](CRIAR_PROJETO_E_VINCULAR.md)

## 🚀 Passos para usar em outra máquina:

1. **Criar seu próprio credentials.json:**
   - Siga as instruções em [CRIAR_PROJETO_E_VINCULAR.md](CRIAR_PROJETO_E_VINCULAR.md)
   - Crie um projeto no Google Cloud Console
   - Baixe o arquivo de credenciais OAuth
   - Renomeie para `credentials.json`

2. **Copiar os arquivos:**
   - Copie `UploadDrive-v2.exe` da pasta `dist/`
   - Copie seu `credentials.json` criado
   - Coloque ambos na mesma pasta

3. **Execute o programa:**
   - Clique duas vezes em `UploadDrive-v2.exe`
   - O programa abrirá normalmente

4. **Primeira execução:**
   - Clique em "Conectar Conta"
   - O navegador abrirá para autorização
   - Após autorizar, você poderá usar normalmente

## ⚠️ Importante:

- **Não precisa instalar Python** na outra máquina - o executável é standalone
- **Não precisa instalar dependências** - tudo está incluído no .exe
- O arquivo `token.pickle` será criado automaticamente após a primeira conexão
- O arquivo `links.txt` será criado após fazer uploads

## 📋 Checklist para distribuição:

- [ ] Copiar `UploadDrive.exe` para a outra máquina
- [ ] Copiar `credentials.json` (se necessário)
- [ ] Colocar ambos na mesma pasta
- [ ] Executar e testar conexão
- [ ] Verificar se o app OAuth está público (para permitir qualquer email)

## 🔧 Solução de Problemas:

**Erro ao executar:**
- Certifique-se de que o Windows não está bloqueando o arquivo
- Clique com botão direito → Propriedades → Desbloquear (se aparecer)

**Erro "credentials.json não encontrado":**
- Você precisa criar seu próprio `credentials.json` seguindo [CRIAR_PROJETO_E_VINCULAR.md](CRIAR_PROJETO_E_VINCULAR.md)
- Coloque o arquivo `credentials.json` na mesma pasta do executável

**Erro 403 ao conectar:**
- Veja o arquivo `CONFIGURAR_OAUTH_PUBLICO.md` para tornar o app público

## 📁 Estrutura na outra máquina:

```
Pasta de Destino/
├── UploadDrive-v2.exe
├── credentials.json (OBRIGATÓRIO - você precisa criar o seu)
├── token.pickle (criado automaticamente após primeira conexão)
└── link{nome_da_pasta}.txt (criado após uploads)
```

## 💡 Dica:

Se você quiser distribuir o programa para outras pessoas, certifique-se de:
1. Tornar o app OAuth público no Google Cloud Console
2. Incluir o arquivo `credentials.json` junto com o executável
3. Fornecer instruções básicas de uso

