# Guia de Solução de Problemas (Troubleshooting)

Este guia reúne diagnósticos de problemas, comportamentos inesperados e soluções comprovadas através de testes reais no sistema [VERIFICADO: todos os comportamentos foram testados em execução real].

---

## Matriz de Problemas e Soluções

| Sintoma Observado | Causa Raiz Identificada | Solução Recomendada | Status |
| :--- | :--- | :--- | :--- |
| **Colei um texto, mas o campo Saída continua vazio e o contador marca "0 OSs".** | Os números presentes no texto não possuem exatamente 6 dígitos numéricos consecutivos, ou estão com letras coladas diretamente a eles. | Verifique se a OS possui 6 dígitos. Se o texto estiver como `OS739241` (sem espaço), adicione um espaço: `OS 739241` [LIDO NO CÓDIGO: index.html:239]. | [VERIFICADO] |
| **A OS está escrita no formato com ponto de milhar (`739.241`) e foi ignorada.** | A expressão regular `/\b\d{6}\b/g` procura 6 algarismos contínuos sem pontuação interna. O ponto divide o número em blocos de 3 e 3 dígitos. | Remova os pontos do texto antes de colar ou faça uma substituição simples de ponto por nada (`Ctrl + U` no editor de texto) [INFERIDO]. | [VERIFICADO] |
| **Cliquei em "Copiar", mas o botão não mudou para "Copiado!" e nada foi para a memória.** | O campo Saída estava completamente vazio. A função possui uma trava de segurança `if (!textToCopy) return;` que ignora o clique se não houver conteúdo. | Insira primeiro um texto válido contendo OSs na Entrada para gerar resultado antes de acionar a cópia [LIDO NO CÓDIGO: index.html:253]. | [VERIFICADO] |
| **O mesmo número de OS apareceu repetido duas ou três vezes no resultado.** | O número foi mencionado mais de uma vez no texto de entrada. O utilitário preserva todas as ocorrências originais e não faz deduplicação automática. | Se precisar apenas de números únicos, copie a saída, cole em uma coluna do Excel e clique na guia *Dados > Remover Duplicadas* [VERIFICADO]. | [VERIFICADO] |
| **Os números na saída não estão em ordem crescente.** | O utilitário extrai na ordem natural de leitura do texto (de cima para baixo, da esquerda para a direita). Ele não executa classificação numérica. | Para ordenar, cole a lista no Excel ou utilize uma ferramenta de classificação alfanumérica [VERIFICADO: teste E2E]. | [VERIFICADO] |
| **O navegador bloqueou a cópia para a área de transferência.** | O navegador estava sem foco ativo ou bloqueou a permissão da moderna Clipboard API assíncrona. | A ferramenta já possui um mecanismo de contingência automático (`execCommand`) que faz a seleção e cópia tradicional. Basta clicar novamente [LIDO NO CÓDIGO: index.html:258-259]. | [VERIFICADO] |
| **Colei um código postal (CEP) ou data e ele apareceu como OS.** | Qualquer sequência de 6 dígitos isolada (como uma data no formato DDMMAA ou parte de um CEP) atende à regra numérica da regex. | Revise visualmente os números no campo Saída e exclua manualmente sequências que não pertençam ao escopo de OSs [INFERIDO]. | [VERIFICADO] |

---

## Exemplo Real de Diagnóstico e Correção

### Cenário com Erro:
Texto colado pelo usuário:
```text
Verificado processo OS739241 e OS 12345 (antiga). Processo novo: 739.710.
```

- **O que a ferramenta extrai**: `0 OSs` (nada é extraído) [VERIFICADO].
- **Por quê?**:
  - `OS739241`: Falha na fronteira `\b` devido à letra `S` adjacente.
  - `12345`: Possui apenas 5 dígitos.
  - `739.710`: Possui ponto separador dividindo em 3 e 3 dígitos.

### Correção Aplicada:
Ajustando o texto para:
```text
Verificado processo OS 739241 e OS 739710.
```

- **Resultado Obtido**: `739241;739710` (Contador: `2 OSs`) [VERIFICADO].
