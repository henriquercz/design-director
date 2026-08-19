# Design Director v3 — Guia rápido

## Instalação

```bash
unzip design-director-skillset-v3.zip
cd design-director-skillset-v3
chmod +x scripts/*.sh
./scripts/install.sh --global --agents codex,claude-code --react
./scripts/doctor.sh
python scripts/validate.py
```

## Uso normal

### Codex

```text
$design-director
Quero que esta interface fique com qualidade de produto profissional.
Analise o que existe, escolha sozinho os tratamentos necessários,
preserve a funcionalidade e valide o resultado no final.
```

### Claude Code

```text
/design-director
Quero que esta interface fique com qualidade de produto profissional.
Analise o que existe, escolha sozinho os tratamentos necessários,
preserve a funcionalidade e valide o resultado no final.
```

Você não precisa dizer `audit`, `relayout`, `deslop` etc. O roteador escolhe.

## Quando nomear um modo

Use quando quiser restringir o trabalho:

```text
$design-director review esta página. Não edite nada.
```

```text
$design-director responsive. Corrija somente mobile e tablet; desktop está aprovado.
```

```text
$design-director relayout somente o hero. Preserve tipografia, cores e conteúdo.
```

## Comportamento importante da v3

- `checkup`, `smell` e `review` explicitamente nomeados = relatório, sem correção no mesmo comando.
- pedido livre como "melhore isso" = diagnóstico interno + correção, sem criar três relatórios desnecessários.
- `redesign` = transformação completa do mundo visual.
- `refine` = muda caráter com `push`, `settle`, `strip`, `proof`, `activate` ou `texture`.
- `voice` = identidade/art direction de Brand.
- `surface` = robustez de app/dashboard/produto.
- `tokenize` = consolidação depois que as decisões estão boas.
- `finish` = uso real, estados, remoção de ruído, verificação e score.

## Prompt diário recomendado

```text
$design-director
Trabalhe como diretor de design deste projeto.
Leia o projeto antes de perguntar qualquer coisa.
Preserve as funcionalidades existentes e os requisitos do produto.
Identifique o tipo de surface e se o registro é Brand ou Product.
Extraia os invariantes do prompt e impeça drift de templates anteriores.
Diagnostique os problemas reais e escolha a menor sequência de tratamentos útil.
Use as skills especialistas apenas quando acrescentarem valor.
Implemente em arquivos reais, teste estados e dados extremos.
Valide a interface renderizada em contextos relevantes.
Faça no máximo um repair pass amplo e um repair pass final focado.
Só declare ship-ready se os quality gates realmente passarem.
```


## Camada de outcome (v3)

Para SaaS/startup você continua chamando apenas a skill principal. Ela pode classificar o problema como Acquire, Activate, Retain, Expand, Monetize ou Differentiate e então escolher o tratamento visual/UX correto.

Exemplo:

```text
$design-director Nossa landing está bonita mas converte mal. Descubra se o problema é mensagem, prova, composição ou fricção e melhore sem dark patterns.
```

Especialista opcional de Revenue-Centric Design:

```bash
./scripts/install.sh --global --agents codex,claude-code --revenue
```

Ele é instalado separadamente e mantém a licença/restrições próprias do repositório upstream.
