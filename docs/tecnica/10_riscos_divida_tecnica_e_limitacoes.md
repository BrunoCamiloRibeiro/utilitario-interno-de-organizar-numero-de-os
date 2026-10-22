# 10. Riscos, Dívida Técnica, Código Morto e Limitações Conhecidas

## 10.1 Riscos de Negócio e de Usabilidade

### 1. Quebra de Expectativa por Ausência de Ordenação e Deduplicação [ALTO]
- **Evidência**: O projeto é rotulado como `Projeto Ordenação OS` e o repositório como `utilitario-interno-de-organizar-numero-de-os` [LIDO NO CÓDIGO: AGENTS.md:1-8].
- **Risco**: Usuários esperam que a lista de saída esteja ordenada de forma crescente (ex.: `111111;555555;999999`) ou sem repetições. Como a implementação atual apenas extrai na ordem original e mantém duplicatas [LIDO NO CÓDIGO: index.html:239-242] [VERIFICADO: teste E2E], consultas em lote em sistemas legados podem ser executadas com itens repetidos ou desordenados.

### 2. Captura Indevida de Números Acessórios (Falsos Positivos) [MÉDIO]
- **Evidência**: A expressão `/\b\d{6}\b/g` captura qualquer número de 6 dígitos [LIDO NO CÓDIGO: index.html:239].
- **Risco**: Se um relatório contiver sequências de 6 dígitos que representem códigos contábeis, ramais telefônicos, matrículas de servidores de 6 dígitos ou partes de datas/documentos (ex.: `221026`), esses valores serão processados como se fossem Ordens de Serviço sem aviso ao usuário [INFERIDO].

### 3. Obsolescência por Virada de Dígitos (Ano 2026+) [MÉDIO]
- **Evidência**: O quantificador `{6}` é rígido [LIDO NO CÓDIGO: index.html:239].
- **Risco**: As OSs observadas nos arquivos SMAURB encontram-se na faixa de 730000 a 754000 [VERIFICADO: arquivos em `/home/brunocr/Documentos/SMAURB/Multas para integrar`]. Quando o município atingir a OS número `1000000` (7 dígitos), o utilitário deixará de capturar todas as novas ordens de serviço sem emitir qualquer mensagem de erro [INFERIDO].

## 10.2 Código Morto ou Funcionalmente Redundante

### Redundância Funcional do Botão "Formatar"
- **Evidência**:
  - Linha 280: `inputEl.addEventListener('input', processOrders);`
  - Linha 281: `btnFormat.addEventListener('click', processOrders);`
- **Análise**: Como o evento `input` reage imediatamente a qualquer caractere digitado ou bloco colado (`Ctrl+V`) [VERIFICADO: teste `test_extraction_on_input_event`], a saída já se encontra formatada no instante em que o usuário move o mouse. O botão `#btnFormat` é funcionalmente supérfluo para fluxos comuns, embora sirva como conforto psicológico para usuários não acostumados com interfaces reativas [INFERIDO].

## 10.3 Dívida Técnica Identificada

1. **API Obsoleta de Clipboard (`document.execCommand`)**:
   - A linha [index.html:259](file:///home/brunocr/Documentos/SMAURB/Projeto%20Ordena%C3%A7%C3%A3o%20OS/index.html#L259) invoca `document.execCommand('copy')`. Embora seja um fallback útil para ambientes antigos, a API foi descontinuada pela W3C e navegadores podem remover seu suporte em versões futuras [INFERIDO].
2. **Ausência de Sanitização e Validação Estruturada**:
   - O código não trata grandes volumes de texto (ex.: colar 50 MB de logs pode travar a thread única de UI do navegador) [INFERIDO].
3. **Falta de Suíte de Testes Nativas no Código-Fonte**:
   - O repositório original continha apenas `index.html` sem qualquer arquivo de teste automatizado [VERIFICADO: listagem inicial do repositório]. A suíte de testes E2E precisou ser instituída na pasta `docs/tests/` [VERIFICADO].
