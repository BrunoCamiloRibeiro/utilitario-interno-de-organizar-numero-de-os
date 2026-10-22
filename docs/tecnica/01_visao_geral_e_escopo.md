# 1. Visão Geral e Escopo do Sistema

## 1.1 Resumo Executivo
O **Formatador de OS** é uma aplicação web *client-side* de arquivo único ([index.html:1-286](file:///home/brunocr/Documentos/SMAURB/Projeto%20Ordena%C3%A7%C3%A3o%20OS/index.html#L1-L286)) desenvolvida para extrair números de Ordens de Serviço (OS) com exatamente 6 dígitos numéricos a partir de textos brutos não estruturados e formatá-los como uma lista delimitada por ponto e vírgula (`;`) [LIDO NO CÓDIGO: index.html:237-249].

A aplicação opera inteiramente no navegador do usuário sem qualquer dependência de backend, requisições de rede externas ou bibliotecas de terceiros [VERIFICADO: execução sem rede e inspeção do DOM via Chrome headless].

## 1.2 Objetivos do Sistema
- **Extração Rápida**: Identificar automaticamente sequências de 6 dígitos decimais isoladas por fronteiras de palavra (`\b\d{6}\b`) em blocos de texto heterogêneos [LIDO NO CÓDIGO: index.html:239].
- **Padronização Delimitada**: Formatar as OSs extraídas unindo-as com ponto e vírgula (`;`), permitindo colagem direta em sistemas legados (ex.: módulos de consulta em lote ou ERPs municipais) [LIDO NO CÓDIGO: index.html:242] [INFERIDO: integração típica do contexto SMAURB].
- **Contagem e Auditoria Visual**: Exibir contador dinâmico de OSs processadas com flexão correta de número gramatical ("1 OS" vs "N OSs") [VERIFICADO: test_singular_plural_badge em docs/tests/test_e2e.py].
- **Agilidade Operacional**: Prover cópia em um clique para a área de transferência do sistema operacional através da Clipboard API moderna com fallback para `document.execCommand('copy')` [LIDO NO CÓDIGO: index.html:251-271] [VERIFICADO: test_copy_button_and_feedback].

## 1.3 Restrições Técnicas
1. **Zero Dependências Externas**: O arquivo [index.html](file:///home/brunocr/Documentos/SMAURB/Projeto%20Ordena%C3%A7%C3%A3o%20OS/index.html) não possui tags `<link rel="stylesheet">` externas nem tags `<script src="...">` remotas [LIDO NO CÓDIGO: index.html:1-286]. Todo o CSS (linhas 7-198) e JavaScript (linhas 227-284) estão embutidos inline [VERIFICADO: inspeção de nós HTML].
2. **Ambiente de Execução**: Compatível com qualquer navegador web moderno com suporte a ECMAScript 2017+ (async/await) e suporte à Clipboard API [LIDO NO CÓDIGO: index.html:251-260] [VERIFICADO: Google Chrome 128+ e navegadores padrão].
3. **Persistência Nula**: A aplicação não persiste dados em `localStorage`, `sessionStorage`, `IndexedDB` ou cookies [LIDO NO CÓDIGO: index.html:227-284]. Uma atualização de página (`F5`) reseta o estado aos valores padrão [VERIFICADO: teste de recarregamento].

## 1.4 Confronto de Hipóteses: Nome do Projeto vs Comportamento Real
> [!WARNING] **Divergência Crítica Identificada**
> - **Hipótese (Docs/Diretórios)**: O diretório do workspace denomina-se `Projeto Ordenação OS` e o arquivo [AGENTS.md:8](file:///home/brunocr/Documentos/SMAURB/Projeto%20Ordena%C3%A7%C3%A3o%20OS/AGENTS.md#L8) cita "Utilitário interno para ordenação e organização de números de OS".
> - **Evidência no Código**: A função `processOrders()` executa estritamente:
>   ```javascript
>   const matches = rawText.match(/\b\d{6}\b/g);
>   if (matches && matches.length > 0) {
>     outputEl.value = matches.join(';');
>   ```
> - **Fato Comprovado**: O código **NÃO ORDENA** os valores (`matches.sort()` não existe no código) e **NÃO DEDIPLICA** os números [VERIFICADO: teste `test_non_sorting_and_non_deduplication` em `docs/tests/test_e2e.py`]. A ordem de saída reflete exatamente a ordem posicional de aparecimento no texto original [LIDO NO CÓDIGO: index.html:239-242].
