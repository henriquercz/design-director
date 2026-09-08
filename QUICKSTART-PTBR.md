# Design Director v4.1 — Quickstart PT-BR

## O principal: continua fácil de usar

Você não precisa saber `relayout`, `deslop`, `motion`, contratos de componentes, posture axes nem nenhum detalhe interno.

Isto já funciona:

```text
$design-director
Não gostei dessa seção. Redesenhe para ficar mais profissional, específica para o produto e melhor resolvida. Preserve o que já funciona.
```

A v4.1 entende o pedido abstrato, lê o projeto e decide sozinha o que precisa inspecionar e quais tratamentos aplicar.

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

Com Revenue-Centric Design (licença upstream separada):

```bash
./scripts/install.sh --global --agents codex,claude-code --react --revenue
```

## 3. O que a v4.1 melhora internamente

Além de tudo da v4, sem mudar seu prompt a skill agora também pode:

- inferir internamente **variância visual, intensidade de motion e densidade de informação** sem pedir sliders numéricos;
- preservar SEO, analytics, rotas/anchors, formulários, consentimento/legal e acessibilidade em redesigns de produção;
- separar um **design system oficial** de uma estética inspirada e verificar APIs/pacotes atuais antes de inventar dependências;
- detectar melhor slop de landing pages: eyebrows repetidos, numeração decorativa, fake status/version/weather, fake screenshots e precisão inventada;
- diferenciar imagem de atmosfera de **prova real do produto**;
- fazer copy self-audit de CTA, terminologia, referents e claims;
- verificar dependências e evitar render churn em interações de pointer/scroll de alta frequência;
- usar `dvh`/`svh` quando resolvem browser chrome mobile, sem transformar isso em regra universal;
- manter tudo calibrado: não bane Inter, serif, em dash, Lucide, gradientes, dark/light, múltiplos accents ou qualquer estética só porque um modelo costuma abusar dela.

## 4. Codex

```text
$design-director
Essa landing está genérica e amadora. Entenda o projeto, escolha sozinho os tratamentos necessários e deixe profissional sem quebrar as funcionalidades. Valide desktop e mobile.
```

## 5. Claude Code

```text
/design-director
Não gostei dessa parte do dashboard. Redesenhe para ficar mais profissional e melhor de operar. Preserve os fluxos e decida sozinho o que precisa mudar.
```

Use nomes de modos apenas quando quiser limitar o escopo:

```text
$design-director review esta landing. Não edite.
$design-director relayout apenas a hero. Preserve cores e tipografia.
$design-director responsive corrija somente mobile/tablet.
```

## 6. Usar sem instalar

Abra [`PROMPT-INSTALL.md`](PROMPT-INSTALL.md), copie o bootstrap e cole no agente/LLM antes do pedido.

Ou:

```bash
npx skills use henriquercz/design-director@design-director --agent codex
npx skills use henriquercz/design-director@design-director --agent claude-code
```

## 7. Claude na web — Skill nativa

```bash
python scripts/build-web-bundles.py --claude
```

Será criado:

```text
dist/claude/design-director-claude-web.zip
```

No Claude:
1. ative **Code execution**;
2. vá em **Customize → Skills**;
3. **+ → Create skill → Upload a skill**;
4. envie o ZIP;
5. ative Design Director.

## 8. ChatGPT na web — GPT ou Projeto

```bash
python scripts/build-web-bundles.py --chatgpt
```

Arquivos:

```text
dist/chatgpt/INSTRUCTIONS.md
dist/chatgpt/design-director-knowledge.md
```

### GPT personalizado
1. **GPTs → Criar**;
2. cole `INSTRUCTIONS.md` em **Instruções**;
3. envie `design-director-knowledge.md` em **Conhecimento**;
4. habilite as ferramentas desejadas;
5. teste e salve.

### Projeto
1. crie um **Projeto**;
2. cole `INSTRUCTIONS.md` nas instruções do projeto;
3. adicione `design-director-knowledge.md` como arquivo/fonte;
4. faça o trabalho de design dentro do projeto.

Para detalhes completos, veja [`README.md`](README.md), [`INSTALL.md`](INSTALL.md), [`V4-RESEARCH-AUDIT.md`](V4-RESEARCH-AUDIT.md) e [`TASTE-SKILL-AUDIT.md`](TASTE-SKILL-AUDIT.md).
