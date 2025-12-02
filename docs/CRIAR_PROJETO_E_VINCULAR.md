# Guia Completo: Criar Novo Projeto e Vincular ao Aplicativo

## 📋 O que você precisa fazer:

1. ✅ Criar um novo projeto no Google Cloud Console
2. ✅ Ativar a API do Google Drive
3. ✅ Criar credenciais OAuth 2.0
4. ✅ Baixar o arquivo `credentials.json`
5. ✅ Configurar a Tela de Consentimento OAuth
6. ✅ Tornar o app público

---

## 🚀 PASSO 1: Criar Novo Projeto

### 1.1 Acessar Google Cloud Console

1. Acesse: **https://console.cloud.google.com**
2. Faça login com sua conta Google

### 1.2 Criar o Projeto

1. No topo da página, ao lado do logo do Google Cloud, você verá um **seletor de projetos**
2. Clique nele e depois clique em **"NOVO PROJETO"** ou **"CREATE PROJECT"**

### 1.3 Configurar o Projeto

1. **Nome do projeto**: Digite um nome (ex: "Upload Drive App" ou "Meu Upload Drive")
2. **ID do projeto**: Será gerado automaticamente (você pode alterar se quiser)
3. **Organização**: Deixe como está (ou selecione se tiver)
4. Clique em **"CRIAR"** ou **"CREATE"**

### 1.4 Aguardar Criação

- Aguarde alguns segundos para o projeto ser criado
- Uma notificação aparecerá quando estiver pronto
- O projeto será selecionado automaticamente

---

## 🔌 PASSO 2: Ativar API do Google Drive

### 2.1 Acessar Biblioteca de APIs

1. No menu lateral esquerdo, clique em **"APIs e Serviços"**
2. Clique em **"Biblioteca"** ou **"Library"**

### 2.2 Buscar e Ativar Google Drive API

1. Na barra de busca, digite: **"Google Drive API"**
2. Clique no resultado **"Google Drive API"**
3. Clique no botão **"ATIVAR"** ou **"ENABLE"**
4. Aguarde alguns segundos para ativação

**✅ Pronto!** A API do Google Drive está ativada.

---

## 🔑 PASSO 3: Criar Credenciais OAuth 2.0

### 3.1 Acessar Credenciais

1. No menu lateral, vá em **"APIs e Serviços"** → **"Credenciais"** ou **"Credentials"**
2. Você verá uma página com suas credenciais (provavelmente vazia)

### 3.2 Configurar Tela de Consentimento (Primeira Vez)

**IMPORTANTE:** Antes de criar credenciais, você precisa configurar a Tela de Consentimento OAuth.

1. Clique em **"CONFIGURAR TELA DE CONSENTIMENTO"** ou **"CONFIGURE CONSENT SCREEN"**
2. Selecione **"Externo"** (para permitir qualquer conta Google)
3. Clique em **"CRIAR"** ou **"CREATE"**

### 3.3 Preencher Informações do App

Na página de configuração, preencha:

1. **Nome do app**: Digite um nome (ex: "Upload Drive")
2. **Email de suporte do usuário**: Seu email
3. **Logo do app** (opcional): Pode pular por enquanto
4. Clique em **"SALVAR E CONTINUAR"** ou **"SAVE AND CONTINUE"**

### 3.4 Configurar Escopos

1. Na seção **"Escopos"**, clique em **"ADICIONAR OU REMOVER ESCOPOS"**
2. Procure por: **"../auth/drive.file"**
3. Marque a caixa ao lado
4. Clique em **"ATUALIZAR"** ou **"UPDATE"**
5. Clique em **"SALVAR E CONTINUAR"**

### 3.5 Adicionar Usuários de Teste (Opcional)

1. Se quiser manter em modo de teste, adicione seu email na seção "Usuários de teste"
2. Ou pule esta etapa se quiser tornar público depois
3. Clique em **"SALVAR E CONTINUAR"**

### 3.6 Revisar e Voltar para Credenciais

1. Revise as informações
2. Clique em **"VOLTAR AO PAINEL"** ou **"BACK TO DASHBOARD"**
3. Agora volte para **"APIs e Serviços"** → **"Credenciais"**

### 3.7 Criar Credenciais OAuth

1. Na página de Credenciais, clique em **"+ CRIAR CREDENCIAIS"** ou **"+ CREATE CREDENTIALS"**
2. Selecione **"ID do cliente OAuth"** ou **"OAuth client ID"**

**Se pedir para configurar a tela de consentimento primeiro:**
- Siga os passos 3.2 a 3.6 acima
- Depois volte aqui

### 3.8 Configurar Tipo de Aplicativo

1. **Tipo de aplicativo**: Selecione **"Aplicativo de desktop"** ou **"Desktop app"**
2. **Nome**: Digite um nome (ex: "Upload Drive Desktop")
3. Clique em **"CRIAR"** ou **"CREATE"**

### 3.9 Baixar Credenciais

1. Uma janela aparecerá com suas credenciais
2. **IMPORTANTE:** Clique em **"BAIXAR JSON"** ou **"DOWNLOAD JSON"**
3. O arquivo será baixado com um nome como `client_secret_xxxxx.json`

### 3.10 Renomear e Colocar no Projeto

1. Renomeie o arquivo baixado para: **`credentials.json`**
2. Coloque este arquivo na mesma pasta onde está o `upload_drive.py`
3. **Certifique-se de que o nome está exatamente:** `credentials.json` (sem espaços, tudo minúsculo)

---

## 🌐 PASSO 4: Tornar o App Público

### ⚠️ IMPORTANTE: Nova Interface do Google Cloud

A interface mudou! Agora você precisa acessar de forma diferente.

### 4.1 Acessar Tela de Consentimento

**Método 1 (Nova Interface):**
1. No menu lateral esquerdo, procure por **"Google Auth Platform"**
2. Clique em **"Público-alvo"** ou **"Audience"**
3. Você verá o status como **"Em teste"**

**Método 2 (Interface Antiga):**
1. Vá em **"APIs e Serviços"** → **"Tela de consentimento OAuth"**
2. Você verá o status como **"Em teste"**

**Método 3 (Link Direto):**
1. Acesse: https://console.cloud.google.com/apis/credentials/consent
2. Certifique-se de que o projeto correto está selecionado

### 4.2 Publicar o App

1. **Role a página para cima** (o botão pode estar no topo)
2. Procure pelo botão **"PUBLICAR APP"** ou **"PUBLISH APP"**
3. Se não encontrar, verifique:
   - Se já está publicado (status: "Em produção")
   - Se tem permissão de "Proprietário" ou "Editor"
4. Clique no botão **"PUBLICAR APP"**
5. Uma janela de confirmação aparecerá
6. Leia os avisos e clique em **"CONFIRMAR"** ou **"CONFIRM"**

**📋 Veja o guia detalhado:** `COMO_PUBLICAR_NA_NOVA_INTERFACE.md`

### 4.3 Aguardar Propagação

- Aguarde **5-10 minutos** para as mudanças serem aplicadas
- O status mudará para **"Em produção"**

---

## ✅ PASSO 5: Verificar Vinculação

### 5.1 Verificar Arquivo credentials.json

1. Abra a pasta do seu projeto
2. Verifique se existe o arquivo `credentials.json`
3. Abra o arquivo (é um JSON) e verifique se contém:
   - `client_id`
   - `client_secret`
   - `project_id`

### 5.2 Testar o Aplicativo

1. Execute o programa: `python upload_drive.py`
2. Clique em **"Conectar Conta"**
3. O navegador deve abrir para autorização
4. Após autorizar, você deve conseguir conectar

---

## 📝 Resumo do que você precisa:

### Arquivos Necessários:

1. ✅ `credentials.json` - Arquivo de credenciais OAuth (você acabou de criar)
2. ✅ `upload_drive.py` - Seu programa Python (já existe)

### Configurações no Google Cloud:

1. ✅ Projeto criado
2. ✅ API do Google Drive ativada
3. ✅ Credenciais OAuth 2.0 criadas (tipo: Desktop App)
4. ✅ Tela de Consentimento configurada
5. ✅ App publicado (status: Em produção)

---

## 🔧 Solução de Problemas

### "Não consigo criar credenciais"

**Causa:** Tela de Consentimento não configurada

**Solução:**
1. Vá em "APIs e Serviços" → "Tela de consentimento OAuth"
2. Configure seguindo os passos 3.2 a 3.6
3. Depois tente criar as credenciais novamente

### "O arquivo credentials.json não funciona"

**Verificações:**
1. O nome está exatamente `credentials.json`? (sem espaços, tudo minúsculo)
2. O arquivo está na mesma pasta do `upload_drive.py`?
3. O arquivo não está corrompido? (abra e veja se é um JSON válido)

### "Erro 403 ao conectar"

**Causa:** App não está público ou email não está na lista de testadores

**Solução:**
1. Vá em "Tela de consentimento OAuth"
2. Clique em "PUBLICAR APP"
3. Ou adicione seu email em "Usuários de teste"

### "Não encontro a opção 'Aplicativo de desktop'"

**Solução:**
- Procure por "Desktop app" ou "Desktop application"
- Ou selecione "Other" e depois escolha "Desktop"

---

## 🎯 Checklist Final

Antes de usar o aplicativo, verifique:

- [ ] Projeto criado no Google Cloud Console
- [ ] API do Google Drive ativada
- [ ] Tela de Consentimento OAuth configurada
- [ ] Credenciais OAuth 2.0 criadas (tipo Desktop)
- [ ] Arquivo `credentials.json` baixado e renomeado
- [ ] Arquivo `credentials.json` na mesma pasta do `upload_drive.py`
- [ ] App publicado (status: Em produção)
- [ ] Testou conectar no aplicativo

---

## 💡 Dica Importante

**Mantenha o arquivo `credentials.json` seguro!**
- Não compartilhe publicamente
- Não faça commit no GitHub sem proteção
- Este arquivo dá acesso à sua conta Google

**Para distribuir o executável:**
- O `credentials.json` pode ser incluído no executável (já configurado)
- Ou distribua junto com o executável

---

## 📞 Próximos Passos

Após seguir todos os passos:

1. ✅ Execute o programa: `python upload_drive.py`
2. ✅ Teste conectar com sua conta Google
3. ✅ Teste fazer upload de arquivos
4. ✅ Se tudo funcionar, você pode criar o executável: `python build_executavel.py`

**Pronto!** Seu aplicativo está vinculado ao projeto Google Cloud e pronto para uso! 🚀

