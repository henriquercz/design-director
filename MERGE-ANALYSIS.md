# Fusão Command Code `/design` → Design Director v2

Fonte analisada: `design_skill_complete.md`, 5.106 linhas, 26 blocos. `SOURCE-STRUCTURE-INDEX.md` registra todos os 374 headings H2/H3 encontrados durante a travessia integral. A análise percorreu o arquivo inteiro e classificou princípios em **adotar**, **adaptar** ou **rejeitar como regra universal**.

## Critério

**Adotar** quando melhora roteamento, qualidade de decisão, robustez de estado, coerência ou verificação.

**Adaptar** quando a ideia é boa, mas a formulação original é rígida, redundante, específica ao Command Code, ou cria artefatos/custo desnecessário.

**Rejeitar como lei** quando transforma design em pseudo-precisão numérica, contradiz outro trecho, incentiva efeito gratuito, ou confunde ergonomia com conformidade.

## Auditoria por bloco

| Linhas fonte | Bloco | Decisão na v2 |
|---:|---|---|
| 3–413 | `SKILL.md` | **Adotar/adaptar fortemente.** Freeform routing, surface-first, prompt invariants, brief sufficiency, scope discipline, report continuity, Brand/Product, truthful completion. Bare routing foi corrigido para não fabricar UI em audit de repo vazio. |
| 414–574 | `border.md` | **Adotar.** Edges semânticos, focus, radius, input/table states, border-vs-shadow containment. Consolidado em `borders-depth.md`. |
| 575–772 | `button.md` | **Adotar/adaptar.** Hierarquia, estados, loading footprint, danger/undo, labels. Press-scale universal e loading “breathing” não viraram regras. |
| 773–938 | `checkup.md` | **Adotar conceito.** Seis vitais + evidência. `/60` removido; v2 usa status e um único score canônico `/100` em review/finish. |
| 939–1110 | `color.md` | **Adotar fortemente.** Emotional arc, semantic roles, OKLCH, palette commitment, grayscale, dark mode, domain-default trap. 60/30/10 deixou de ser lei. |
| 1111–1403 | `create.md` | **Adotar fortemente.** Read-before-ask, invariants, divergence check, build layers, edge states, realistic content. Algumas receitas visuais rígidas foram removidas. |
| 1404–1634 | `design-html.md` | **Não usar como inspiração de produto.** A fronteira é mantida; v2 prefere templates de relatório compactos em vez de carregar um grande aesthetic scaffold. |
| 1635–1849 | `deslop.md` | **Adotar diagnóstico/tratamento e designer verification.** Rejeitada a obrigação de gerar três relatórios antes de toda correção; usa relatórios existentes ou diagnóstico interno. |
| 1850–2011 | `finish.md` | **Adotar fortemente.** Real-use pass, edge states, subtraction, applied-only claims, diff/render verification. |
| 2012–2196 | `interaction.md` | **Adotar fortemente.** Full control lifecycle, keyboard/focus, recovery, overlays, mobile form zoom, RTL behavior. |
| 2197–2361 | `layout.md` | **Adotar princípios.** Task-derived composition, cards-not-default, depth planes, wrappers, rhythm. 1-4-9 universal, mass calculator e cliffhanger fixo foram removidos/convertidos em heurísticas qualitativas. |
| 2362–2569 | `motion.md` | **Adotar propósito + reduced motion.** Rejeitada a exigência de que um motion pass sempre adicione animação; timings/springs/scales viraram contexto, não lei. |
| 2570–2761 | `redesign.md` | **Adotar como modo de primeira classe.** Deve mudar spatial premise + visual system, não repaint. |
| 2762–2960 | `refine.md` | **Adotar quase inteiro como arquitetura.** `push`, `settle`, `strip`, `proof`, `activate`, `texture`, `push past limits` são excelentes moves. |
| 2961–3163 | `relayout.md` | **Adotar structural change bar.** Corrigida contradição que obrigava `color.md` e `typeset.md` apesar de dizer para não mudar identidade/tipo. |
| 3164–3404 | `report-html.md` | **Reduzir.** Relatórios continuam separados de product UI, mas HTML não é obrigatório na v2 e não deve consumir contexto sem necessidade. |
| 3405–3643 | `responsive.md` | **Adotar fortemente.** Content-driven adaptation, input modes, safe areas, containers, RTL/logical properties, real RTL test, iOS 16px form behavior, dense-data strategies. Fixed viewport gauntlet virou context-driven test set. |
| 3644–3811 | `review.md` | **Adotar experiência/evidência/priorização.** `/50` substituído pelo score canônico `/100`. |
| 3812–3936 | `setup.md` | **Adotar.** Virou `.design-director/brief.md` como design constitution/memory. |
| 3937–4079 | `shadow.md` | **Adotar.** Elevation semantics, dark mode, coherent light/depth, performance. Consolidado com borders. |
| 4080–4284 | `smell.md` | **Adotar fortemente.** 10 tells + domain stereotype + prompt drift. Score invertido `/10` removido; smell severity não deve fingir ser qualidade geral. |
| 4285–4453 | `surface.md` | **Adotar como modo de primeira classe.** Product hardening, data/state/density/operability. |
| 4454–4583 | `tokenize.md` | **Adotar como modo de primeira classe.** Consolidation after decisions, semantic names, migrate real usage, no invention disguised as cleanup. |
| 4584–4759 | `typeset.md` | **Adotar sistema e stress tests.** Reading-distance equation e hierarquia exatamente-3 foram removidas. |
| 4760–4948 | `voice.md` | **Adotar como modo de primeira classe.** Brand lane, proof/artifact-first, physical associations, imagery, section coherence. |
| 4949–5106 | `writing.md` | **Adotar recovery/action/localization.** Bans universais de em dash, exclamação e case foram removidos; voz depende de contexto. |

## Melhorias arquiteturais sobre a fonte

### 1. Diagnóstico interno ≠ relatório obrigatório
A fonte tem uma ótima separação entre diagnóstico e tratamento, mas em `deslop` exige todos os relatórios. A v2 mantém a separação lógica sem gerar arquivos desnecessários. Relatórios persistentes existem quando o usuário pede `checkup`, `smell` ou `review` explicitamente.

### 2. Um score canônico
A fonte usa `/60` em checkup, `/50` em review e `/10` invertido em smell. A v2 evita esse vocabulário fragmentado:
- checkup = statuses;
- smell = severity/evidence;
- review/finish = score `/100`.

### 3. Calibration layer
Números úteis deixam de ser leis. A v2 explicitamente diferencia:
- standards/accessibility floors;
- ergonomic targets;
- visual heuristics;
- project-specific tokens.

### 4. Empty-repo behavior corrigido
A fonte manda qualquer modo criar `index.html` em projeto vazio. Isso é útil para criação, mas ruim para um audit explícito. A v2 cria somente quando a intenção realmente é criar.

### 5. Motion can choose stillness
A fonte possui ótimos princípios de motion, mas alguns trechos fazem a ausência de animação parecer falha. Na v2, remover motion pode ser a conclusão correta.

### 6. Relayout não puxa recolor/typeset por obrigação
A composição continua separada da identidade visual quando o escopo exige isso.

### 7. Compact context
Regras globais como "não gere relatórios" e truthful completion aparecem uma vez no core, em vez de serem repetidas em cada arquivo. Isso economiza contexto e reduz conflito interno.

## Regras deliberadamente NÃO importadas como universais

- 60/30/10 obrigatório;
- tipografia com exatamente três níveis;
- reading-distance equation;
- toda spacing como múltiplo 1/4/9;
- composition-mass score;
- cliffhanger de 40–80px em toda seção;
- spring tension/damping fixos;
- 3-beat entrance universal;
- random stagger jitter;
- press scale 0.97–0.98 obrigatório;
- width-breathing loading button;
- seis viewports fixos em todo projeto;
- slider custom de motion obrigatório;
- 44×44 descrito como requisito WCAG AA;
- proibição universal de em dash/exclamação;
- "um único primary button" interpretado literalmente para telas complexas;
- três relatórios obrigatórios antes de deslop.

Essas ideias foram preservadas apenas quando o princípio por trás delas é útil e contextual.
