# Relatório de Documentação e Análise Crítica (DOCS_REPORT.md)

Este relatório compila os achados da Fase 2 e atende estritamente às diretrizes de governança técnica, documentando intenções não confirmadas, anomalias de código, dívidas de projeto e perguntas para a equipe de desenvolvimento [VERIFICADO].

---

## 1. Intenções Não Confirmadas (`[INTENÇÃO NÃO CONFIRMADA]`)

Onde o porquê do comportamento não pôde ser comprovado documentalmente pelo código ou histórico git do commit `ad56c8b`, a marcação formal `[INTENÇÃO NÃO CONFIRMADA]` foi registrada:

1. **Ausência de Algoritmo de Ordenação**:
   - *Evidência*: O repositório chama-se `utilitario-interno-de-organizar-numero-de-os` e a pasta `Projeto Ordenação OS`. A função `processOrders()` em [index.html:237-249](file:///home/brunocr/Documentos/SMAURB/Projeto%20Ordena%C3%A7%C3%A3o%20OS/index.html#L237-L249) executa unicamente `rawText.match(/\b\d{6}\b/g)` e `matches.join(';')`.
   - *Intenção Não Confirmada*: Não é possível inferir se a preservação da ordem original de entrada foi intencional (para manter o alinhamento sequencial com relatórios de fiscalização físicos) ou se a ordenação numérica (`.sort()`) foi planejada e não chegou a ser implementada antes do commit inicial.
2. **Preservação de Duplicatas**:
   - *Evidência*: Se o número `739241` for citado três vezes no texto de entrada, a saída exibirá `739241;739241;739241`.
   - *Intenção Não Confirmada*: Não há registros se a repetição visa auditoria de menções repetidas ou se filtros SQL com `new Set(matches)` deveriam ter sido aplicados.
3. **Restrição Rígida a 6 Dígitos (`\d{6}`)**:
   - *Evidência*: Quantificador exato `{6}`. Números de 7 dígitos são rejeitados.
   - *Intenção Não Confirmada*: Não há especificação formal se a regra pressupõe que as OSs da SMAURB jamais ultrapassarão 999.999 durante o ciclo de vida deste utilitário ou se novos dígitos serão incorporados futuramente.

---

## 2. Bugs Prováveis, Código Morto e Contradições

1. **Redundância Funcional do Botão `#btnFormat` (Quase Código Morto)**:
   - *Evidência*: [index.html:280-281](file:///home/brunocr/Documentos/SMAURB/Projeto%20Ordena%C3%A7%C3%A3o%20OS/index.html#L280-L281) vincula a mesma função `processOrders` a dois eventos:
     - `inputEl.addEventListener('input', processOrders);`
     - `btnFormat.addEventListener('click', processOrders);`
   - *Análise*: O evento `input` é disparado sincronicamente a cada tecla digitada ou bloco colado (`Ctrl+V`). Logo, a saída já está processada no instante em que o operador poderia mover o cursor até o botão "Formatar". O botão é funcionalmente inerte na esmagadora maioria dos casos de uso, servindo primariamente como placebo de interface ou salvaguarda para navegadores que não disparem o evento `input` em preenchimento automático.
2. **Uso de API Obsoleta (`document.execCommand('copy')`)**:
   - *Evidência*: Linha de contingência em [index.html:259](file:///home/brunocr/Documentos/SMAURB/Projeto%20Ordena%C3%A7%C3%A3o%20OS/index.html#L259).
   - *Análise*: Embora funcione no Chrome 128+, a especificação oficial W3C marcou `document.execCommand` como depreciada (*deprecated*). Em versões futuras dos navegadores corporativos, essa chamada poderá disparar avisos no console ou ser removida.
3. **Contradição entre Metadados do Repositório e Implementação Real**:
   - O arquivo [AGENTS.md:8](file:///home/brunocr/Documentos/SMAURB/Projeto%20Ordena%C3%A7%C3%A3o%20OS/AGENTS.md#L8) e o nome do repositório no GitHub prometem "ordenação", mas o código não ordena. Essa contradição foi corrigida na documentação e rotulada com avisos no código.

---

## 3. Decisões sem Lastro Histórico

1. **Origem da Aplicação Monofólio**:
   - O repositório no GitHub foi criado recentemente (`created_at: 2026-10-22T11:59:45Z`) com tamanho 0 e sem histórico prévio de ramificações (*branches*) ou commits no git.
   - O arquivo inicial [index.html](file:///home/brunocr/Documentos/SMAURB/Projeto%20Ordena%C3%A7%C3%A3o%20OS/index.html) já possuía todas as regras de CSS embutidas e tratamento de fallback sem histórico incremental que justifique por que o framework de interface padrão (CSS puro) foi escolhido em detrimento de Bootstrap ou Tailwind.

---

## 4. Perguntas Objetivas para o Autor / Mantenedor

Para sanar em definitivo as intenções não confirmadas:

1. **Ordenação Numérica**:
   - Devemos adicionar uma ordenação ascendente no array (`matches.sort((a,b) => Number(a) - Number(b))`), adicionar uma opção de alternância na tela (checkbox "Ordenar números"), ou manter a ordem de leitura original do texto?
2. **Filtragem de Duplicatas**:
   - Números idênticos no mesmo relatório devem ser desduplicados automaticamente (`Array.from(new Set(matches))`) ou o sistema deve continuar exibindo todas as repetições?
3. **Previsão de Virada de Dígitos (7 dígitos)**:
   - A numeração sequencial de OS da prefeitura se aproxima de 1.000.000? Devemos atualizar a regex para aceitar `\b\d{6,7}\b`?
4. **Delimitador de Saída**:
   - A saída deve permanecer fixa em ponto e vírgula (`;`), ou seria produtivo oferecer opção para quebra de linha (`\n`) para colagem em colunas verticais do Excel?
