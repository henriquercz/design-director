# Design Director v3 — Quickstart PT-BR

## 1. Instalação mais fácil: `npx skills`

### Codex + Claude Code global

```bash
npx skills add henriquercz/design-director \
  --skill design-director \
  -g \
  -a codex \
  -a claude-code \
  -y
```

### Só neste projeto

```bash
npx skills add henriquercz/design-director \
  --skill design-director \
  -a codex \
  -a claude-code \
  -y
```

## 2. Instalação completa com companions

```bash
git clone https://github.com/henriquercz/design-director.git
cd design-director
chmod +x scripts/*.sh
./scripts/install.sh --global --agents codex,claude-code --react
./scripts/doctor.sh
python scripts/validate.py
```

Com o especialista Revenue-Centric Design (licença upstream separada):

```bash
./scripts/install.sh --global --agents codex,claude-code --react --revenue
```

## 3. Como usar

### Codex

```text
$design-director
Essa página está genérica e amadora. Analise o projeto, encontre as causas reais, escolha sozinho os tratamentos necessários, preserve a funcionalidade e valide desktop + mobile no final.
```

### Claude Code

```text
/design-director
Melhore esse dashboard como produto real. Preserve os fluxos existentes, corrija composição, estados, responsividade e acessibilidade conforme necessário e verifique o resultado.
```

Você **não precisa** dizer `relayout`, `deslop`, `typeset` etc. A skill roteia automaticamente. Use o nome do modo apenas quando quiser restringir o escopo.

## 4. Usar sem instalar

Abra [`PROMPT-INSTALL.md`](PROMPT-INSTALL.md), copie o bootstrap e cole no agente/LLM antes do seu pedido.

Ou, com o Skills CLI:

```bash
npx skills use henriquercz/design-director@design-director --agent codex
npx skills use henriquercz/design-director@design-director --agent claude-code
```

## 5. Claude na web — Skill nativa

Gere o ZIP:

```bash
python scripts/build-web-bundles.py --claude
```

Será criado:

```text
dist/claude/design-director-claude-web.zip
```

No Claude:

1. Ative **Code execution**.
2. Vá em **Customize → Skills**.
3. Clique em **+ → Create skill → Upload a skill**.
4. Envie `design-director-claude-web.zip`.
5. Ative a skill.

Depois basta pedir normalmente; o Claude pode identificar quando usar a skill.

## 6. ChatGPT na web — GPT personalizado

Gere o pacote:

```bash
python scripts/build-web-bundles.py --chatgpt
```

Arquivos:

```text
dist/chatgpt/INSTRUCTIONS.md
dist/chatgpt/design-director-knowledge.md
```

No ChatGPT:

1. Abra **GPTs → Criar**.
2. Cole `INSTRUCTIONS.md` em **Instruções**.
3. Envie `design-director-knowledge.md` em **Conhecimento**.
4. Habilite as ferramentas que quiser.
5. Teste na Prévia e salve.

A criação/edição de GPTs personalizados exige um plano elegível pago.

## 7. ChatGPT na web — Projeto

Se preferir um workspace em vez de um GPT:

1. Crie um **Projeto**.
2. Em **Configurações do projeto**, cole `INSTRUCTIONS.md` nas instruções.
3. Adicione `design-director-knowledge.md` aos arquivos/fontes do projeto.
4. Faça o trabalho de design dentro daquele projeto.

## 8. Exemplos de controle explícito

```text
$design-director review esta landing page. Não edite arquivos.
$design-director relayout esta hero. Preserve cor e tipografia.
$design-director responsive corrija apenas tablet e mobile.
$design-director finish faça somente o passe final antes de ship.
```

Para detalhes completos, veja [`README.md`](README.md) e [`INSTALL.md`](INSTALL.md).
