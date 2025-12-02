# Como Publicar o App na Nova Interface do Google Cloud

## 🔍 Você está na página errada!

Você está em **"Visão geral de OAuth"** (OAuth Overview), que mostra apenas métricas e estatísticas. O botão de publicar está em outra página.

## ✅ Solução: Acessar a Página Correta

### Método 1: Pelo Menu Lateral (Mais Fácil)

Na barra lateral esquerda, você vê:
- Visão geral ← (você está aqui)
- Branding
- **Público-alvo** ← CLIQUE AQUI!
- Clientes
- Acesso a dados
- Central de verificação
- Configurações

**Clique em "Público-alvo" (Audience)**

### Método 2: Pelo Menu Principal

1. No topo da página, clique no menu **"☰"** (três linhas horizontais)
2. Procure por **"APIs e Serviços"** ou **"APIs & Services"**
3. Clique em **"Tela de consentimento OAuth"** ou **"OAuth consent screen"**

### Método 3: Link Direto

Acesse diretamente:
**https://console.cloud.google.com/apis/credentials/consent**

**Certifique-se de que o projeto "Upload Drive App" está selecionado no topo!**

---

## 🎯 O que você verá na página correta:

Na página **"Tela de consentimento OAuth"** ou **"Público-alvo"**, você verá:

1. **Status do app**: "Em teste" ou "Em produção"
2. **Informações do app**: Nome, email, etc.
3. **Botão grande no topo**: **"PUBLICAR APP"** ou **"PUBLISH APP"** ← ESTE É O BOTÃO!

---

## 📋 Passo a Passo Detalhado:

### Passo 1: Clique em "Público-alvo"

No menu lateral esquerdo, clique em **"Público-alvo"** (Audience)

### Passo 2: Verificar Status

Na página que abrir, você verá:
- Status: **"Em teste"** (Testing)
- Tipo de usuário: **"Externo"** (External)

### Passo 3: Encontrar o Botão Publicar

1. **Role a página para cima** (o botão pode estar no topo)
2. Procure por um botão grande com texto:
   - **"PUBLICAR APP"** (em português)
   - **"PUBLISH APP"** (em inglês)
   - Ou **"ALTERAR PARA PRODUÇÃO"**

### Passo 4: Se não encontrar o botão

**Possíveis causas:**

1. **Você já está em produção**
   - Verifique o status: se diz "Em produção", já está publicado!
   
2. **Falta configurar algo**
   - Verifique se todas as informações estão preenchidas:
     - Nome do app
     - Email de suporte
     - Escopos configurados
   
3. **Você não tem permissão**
   - Precisa ser "Proprietário" ou "Editor" do projeto

### Passo 5: Publicar

1. Clique no botão **"PUBLICAR APP"**
2. Uma janela de confirmação aparecerá
3. Leia os avisos
4. Clique em **"CONFIRMAR"** ou **"CONFIRM"**

---

## 🔧 Se ainda não encontrar:

### Opção A: Verificar se já está publicado

1. Na página "Público-alvo", veja o status
2. Se diz **"Em produção"** → Já está publicado! ✅
3. Se diz **"Em teste"** → Precisa publicar

### Opção B: Tentar pela aba "Branding"

1. No menu lateral, clique em **"Branding"**
2. Configure o nome e logo do app
3. Clique em **"SALVAR"**
4. Depois volte para **"Público-alvo"** e procure o botão

### Opção C: Verificar permissões

1. No topo da página, ao lado do nome do projeto
2. Verifique se você tem permissão de **"Proprietário"** ou **"Editor"**
3. Se for apenas "Visualizador", não poderá publicar

---

## 📸 Onde está o botão (Visual):

```
Página: Público-alvo (Audience)
│
├── [Topo da página]
│   └── [BOTÃO: PUBLICAR APP] ← AQUI!
│
├── Status: Em teste
│
├── Tipo de usuário: Externo
│
└── [Resto das configurações...]
```

---

## ✅ Checklist:

- [ ] Cliquei em "Público-alvo" no menu lateral
- [ ] Estou na página correta (não é "Visão geral")
- [ ] Vejo o status "Em teste"
- [ ] Procurei o botão no topo da página
- [ ] Rolei a página para cima e para baixo
- [ ] Verifiquei minhas permissões no projeto

---

## 💡 Dica Importante:

**A nova interface do Google Cloud mudou!**

- Antes: "APIs e Serviços" → "Tela de consentimento OAuth"
- Agora: "Google Auth Platform" → "Público-alvo" (Audience)

O botão de publicar está na página **"Público-alvo"**, não na "Visão geral"!

---

## 🆘 Se nada funcionar:

Me diga:
1. O que aparece quando você clica em "Público-alvo"?
2. Qual é o status que você vê? ("Em teste" ou "Em produção"?)
3. Você vê algum botão na página? Qual o texto dele?

Com essas informações, posso te ajudar de forma mais específica!

