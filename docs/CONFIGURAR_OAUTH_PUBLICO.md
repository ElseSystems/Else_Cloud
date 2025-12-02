# Como Configurar OAuth para Qualquer Email Usar

## Problema Atual
O erro "403: access_denied" ocorre porque seu aplicativo OAuth está em **modo de teste** e só permite emails de testadores aprovados.

## ⚠️ IMPORTANTE: Leia o Guia Completo

**Para instruções detalhadas com imagens e soluções de problemas, veja:** `GUIA_COMPLETO_OAUTH.md`

## Solução: Tornar o App Público

### Passo 1: Acessar Google Cloud Console

1. Acesse: https://console.cloud.google.com
2. **Selecione seu projeto** no seletor no topo da página
3. Se não encontrar o projeto, procure na lista ou crie um novo

### Passo 2: Encontrar a Tela de Consentimento OAuth

**Três formas de encontrar:**

**Método 1 (Mais fácil):**
1. No menu lateral esquerdo, clique em **"APIs e Serviços"**
2. No submenu, clique em **"Tela de consentimento OAuth"**

**Método 2 (Busca):**
1. Use a barra de busca no topo
2. Digite: **"Tela de consentimento OAuth"** ou **"OAuth consent screen"**

**Método 3 (Link direto):**
1. Acesse: https://console.cloud.google.com/apis/credentials/consent
2. Certifique-se de que o projeto correto está selecionado

### Passo 3: Verificar Status

1. Na página da "Tela de consentimento OAuth"
2. Você verá que o status está como **"Em teste"**

### Passo 4: Publicar o App

1. Clique no botão **"PUBLICAR APP"** (no topo da página)
2. Uma janela de confirmação aparecerá
3. Leia os avisos e clique em **"CONFIRMAR"**

### Passo 5: Configurar Informações do App (se necessário)

Certifique-se de que as seguintes informações estão preenchidas:

- **Nome do app**: Nome que aparecerá para os usuários
- **Email de suporte do usuário**: Seu email
- **Logo do app** (opcional): Pode adicionar um logo
- **Domínio autorizado** (opcional): Se tiver um domínio

### Passo 6: Adicionar Escopos (Scopes)

Na seção **"Escopos"**, certifique-se de que está configurado:
- `https://www.googleapis.com/auth/drive.file` (já deve estar)

### Passo 7: Adicionar Usuários de Teste (Alternativa - se não quiser tornar público)

Se preferir manter em modo de teste mas adicionar mais usuários:

1. Na seção **"Usuários de teste"**
2. Clique em **"+ ADICIONAR USUÁRIOS"**
3. Adicione os emails que devem ter acesso
4. Clique em **"ADICIONAR"**

### Passo 8: Salvar e Aguardar

1. Clique em **"SALVAR E CONTINUAR"** em cada etapa
2. Aguarde alguns minutos para as mudanças serem propagadas

## ⚠️ Importante

### Se Tornar Público:
- ✅ Qualquer pessoa com conta Google poderá usar
- ✅ Não precisa adicionar emails manualmente
- ⚠️ Você precisará passar pela verificação do Google se usar escopos sensíveis
- ⚠️ Pode levar alguns dias para ser aprovado se precisar de verificação

### Se Manter em Modo de Teste:
- ✅ Mais controle sobre quem acessa
- ✅ Não precisa de verificação do Google
- ❌ Precisa adicionar cada email manualmente
- ❌ Limitado a 100 usuários de teste

## Verificação do Google (se necessário)

Se você tornar o app público e usar escopos sensíveis, o Google pode solicitar verificação:

1. Você receberá um email do Google
2. Precisará preencher um formulário de verificação
3. Pode levar alguns dias para aprovação

Para o escopo `drive.file` (acesso apenas a arquivos criados pelo app), geralmente não é necessário verificação.

## 🔧 Problemas Comuns

### "Não encontro o projeto"
- Verifique se está logado com a conta correta
- Procure na lista de projetos recentes
- Ou crie um novo projeto

### "Não vejo o botão PUBLICAR APP"
- Verifique se tem permissão de "Editor" ou "Proprietário"
- Certifique-se de que o tipo de usuário é "Externo"
- O botão está no topo da página da "Tela de consentimento OAuth"

### "Não encontro a opção 'Tela de consentimento OAuth'"
- Use a busca: digite "OAuth consent screen"
- Ou acesse: https://console.cloud.google.com/apis/credentials/consent
- Certifique-se de que a API do Google Drive está ativada

**Para mais detalhes e soluções, veja:** `GUIA_COMPLETO_OAUTH.md`

## Testando Após Configuração

1. Aguarde 5-10 minutos após publicar
2. Feche completamente o programa
3. Remova o arquivo `token.pickle` (se existir)
4. Execute o programa novamente
5. Tente conectar com qualquer conta Google

## Resumo Rápido

**Para permitir QUALQUER email:**
1. Acesse: https://console.cloud.google.com
2. Selecione o projeto correto
3. Menu: APIs e Serviços → Tela de consentimento OAuth
4. Clique em **"PUBLICAR APP"** (botão no topo)
5. Confirme
6. Aguarde alguns minutos
7. Teste novamente

**Para adicionar emails específicos (modo teste):**
1. Google Cloud Console → APIs e Serviços → Tela de consentimento OAuth
2. Seção "Usuários de teste" → "+ ADICIONAR USUÁRIOS"
3. Adicione os emails
4. Salve

