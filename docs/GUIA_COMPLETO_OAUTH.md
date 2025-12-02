# Guia Completo: Como Tornar o App OAuth Público no Google Cloud Console

## 🔍 Passo 1: Acessar o Google Cloud Console

1. Acesse: **https://console.cloud.google.com**
2. Faça login com a mesma conta Google que você usou para criar o projeto

## 🔍 Passo 2: Selecionar o Projeto Correto

1. No topo da página, você verá um **seletor de projetos** (ao lado do logo do Google Cloud)
2. Clique nele e selecione o projeto onde você criou as credenciais OAuth
3. **Se não encontrar o projeto:**
   - Clique em "NOVO PROJETO" para criar um novo
   - Ou procure na lista de projetos recentes

## 🔍 Passo 3: Encontrar a Tela de Consentimento OAuth

### Método 1: Pelo Menu Lateral (Mais Fácil)

1. No menu lateral esquerdo, procure por **"APIs e Serviços"**
2. Clique em **"APIs e Serviços"**
3. No submenu que aparece, clique em **"Tela de consentimento OAuth"**

### Método 2: Pela Busca

1. No topo da página, há uma **barra de busca** (lupa)
2. Digite: **"Tela de consentimento OAuth"** ou **"OAuth consent screen"**
3. Clique no resultado que aparecer

### Método 3: Link Direto

1. Acesse diretamente: **https://console.cloud.google.com/apis/credentials/consent**
2. Certifique-se de que o projeto correto está selecionado no topo

## 📋 Passo 4: Verificar o Status Atual

Na página da "Tela de consentimento OAuth", você verá:

- **Status**: "Em teste" ou "Em produção"
- **Tipo de usuário**: "Externo" ou "Interno"
- Informações do app (nome, email, etc.)

## 🚀 Passo 5: Tornar o App Público

### Se o Status estiver como "Em teste":

1. No topo da página, você verá um botão grande **"PUBLICAR APP"** ou **"PUBLISH APP"**
2. Clique neste botão
3. Uma janela de confirmação aparecerá com avisos
4. Leia os avisos e clique em **"CONFIRMAR"** ou **"CONFIRM"**

### Se o botão não aparecer:

1. Verifique se você está na aba correta (geralmente "Editar app")
2. Role a página para cima - o botão pode estar no topo
3. Verifique se você tem permissões de "Proprietário" ou "Editor" no projeto

## ⚙️ Passo 6: Configurar Informações Básicas (se necessário)

Se ainda não configurou, preencha:

1. **Tipo de usuário**: Selecione "Externo" (para permitir qualquer conta Google)
2. **Nome do app**: Dê um nome (ex: "Upload Drive")
3. **Email de suporte do usuário**: Seu email
4. **Logo** (opcional): Pode adicionar um logo
5. Clique em **"SALVAR E CONTINUAR"** em cada etapa

## 📝 Passo 7: Configurar Escopos (Scopes)

1. Na seção **"Escopos"**, verifique se está configurado:
   - `https://www.googleapis.com/auth/drive.file`
2. Se não estiver, clique em **"ADICIONAR OU REMOVER ESCOPOS"**
3. Procure e adicione o escopo acima
4. Clique em **"SALVAR E CONTINUAR"**

## 👥 Passo 8: Adicionar Usuários de Teste (Alternativa)

**Se preferir manter em modo de teste mas adicionar mais usuários:**

1. Na seção **"Usuários de teste"**
2. Clique em **"+ ADICIONAR USUÁRIOS"**
3. Digite os emails (um por linha ou separados por vírgula)
4. Clique em **"ADICIONAR"**
5. **Limite**: Máximo de 100 usuários de teste

## ✅ Passo 9: Verificar Publicação

Após publicar:

1. O status mudará de **"Em teste"** para **"Em produção"**
2. Aguarde **5-10 minutos** para as mudanças serem propagadas
3. Você verá um aviso verde confirmando a publicação

## 🔧 Solução de Problemas

### "Não encontro o projeto"

**Solução:**
- Verifique se está logado com a conta correta
- Procure na lista de projetos recentes
- Ou crie um novo projeto e configure as credenciais novamente

### "Não vejo o botão PUBLICAR APP"

**Possíveis causas:**
1. **Você não tem permissão**: Peça ao proprietário do projeto para dar permissão de "Editor"
2. **App já está público**: Verifique o status na página
3. **Tipo de usuário incorreto**: Se for "Interno", só funciona para contas da organização

**Solução:**
- Verifique suas permissões no projeto
- Certifique-se de que o tipo de usuário é "Externo"

### "Não encontro a opção 'Tela de consentimento OAuth'"

**Solução:**
- Use a busca no topo: digite "OAuth consent screen"
- Ou acesse diretamente: https://console.cloud.google.com/apis/credentials/consent
- Certifique-se de que a API do Google Drive está ativada

### "O app precisa de verificação"

**Quando acontece:**
- Para escopos sensíveis (como acesso completo ao Drive)
- Para apps com muitos usuários

**Solução:**
- O escopo `drive.file` geralmente **não precisa** de verificação
- Se pedir verificação, você receberá um email do Google com instruções
- Pode levar alguns dias para aprovação

## 📸 Onde Está Cada Coisa (Visual)

```
Google Cloud Console
├── Menu Lateral Esquerdo
│   └── APIs e Serviços
│       ├── Dashboard
│       ├── Biblioteca
│       ├── Credenciais ← (Aqui você criou o credentials.json)
│       └── Tela de consentimento OAuth ← (AQUI ESTÁ!)
│
└── Topo da Página
    ├── Seletor de Projetos ← (Certifique-se do projeto correto)
    └── Barra de Busca ← (Use para encontrar "OAuth consent screen")
```

## 🎯 Resumo Rápido

1. **Acesse**: https://console.cloud.google.com
2. **Selecione** o projeto correto
3. **Menu**: APIs e Serviços → Tela de consentimento OAuth
4. **Clique**: "PUBLICAR APP" (botão no topo)
5. **Confirme** a publicação
6. **Aguarde** 5-10 minutos

## 💡 Dica Extra

Se ainda tiver dificuldade, você pode:
- Tirar um print da tela do Google Cloud Console e me mostrar
- Ou me dizer exatamente o que você vê quando acessa o console
- Assim posso te guiar passo a passo de forma mais específica

