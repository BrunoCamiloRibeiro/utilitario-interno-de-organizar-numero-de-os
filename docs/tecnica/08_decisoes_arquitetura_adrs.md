# 8. Registros de Decisões de Arquitetura (ADRs - MADR)

Estes registros foram reconstruídos com base na evidência do código-fonte e histórico de criação do repositório [INFERIDO: reconstrução analítica baseada no código index.html].

---

## ADR-001: Adoção de Arquitetura *Single-File Client-Side* (Monofólio HTML/CSS/JS)

* **Status**: Aceito e Implementado [LIDO NO CÓDIGO: index.html:1-286].
* **Decisores**: Engenharia de Software / SMAURB [INFERIDO].
* **Data**: 2026-10-22 [LIDO NO HISTÓRICO: timestamp de criação do arquivo].

### Contexto
Servidores municipais e operadores de campo da SMAURB precisam processar relatórios de campo e números de processos em diferentes computadores corporativos que frequentemente possuem restrições de permissão para instalação de executáveis, bloqueios de firewall ou ausência de runtimes (Node.js/Python) instalados [INFERIDO: contexto operacional da SMAURB].

### Decisão
Empacotar toda a aplicação (estrutura semântica HTML, estilização visual CSS e lógica JavaScript) em um único arquivo [index.html](file:///home/brunocr/Documentos/SMAURB/Projeto%20Ordena%C3%A7%C3%A3o%20OS/index.html), sem dependências de CDN ou empacotadores (*bundlers*).

### Consequências
* **Positivas**:
  - Portabilidade instantânea: funciona abrindo diretamente no navegador (`file://`) [VERIFICADO].
  - Manutenção zero de infraestrutura e custo de servidor nulo [INFERIDO].
  - Isolamento de segurança: não transmite dados para servidores externos [VERIFICADO].
* **Negativas**:
  - Mistura de preocupações de apresentação e lógica em um único arquivo de 286 linhas [LIDO NO CÓDIGO].
  - Falta de modularização para reuso de componentes caso o sistema cresça [INFERIDO].

---

## ADR-002: Extração Determinística de OS via Regex `\b\d{6}\b` com Delimitação por `;`

* **Status**: Aceito e Implementado [LIDO NO CÓDIGO: index.html:239-242].
* **Data**: 2026-10-22.

### Contexto
As Ordens de Serviço municipais da prefeitura utilizam um padrão fixo de 6 dígitos decimais (por exemplo: 739241, 739710, 740588). Esses números chegam aos operadores misturados em corpos de texto de e-mails, despachos administrativos ou relatórios em PDF [INFERIDO: dados observados na pasta SMAURB].

### Decisão
Utilizar a expressão regular `/\b\d{6}\b/g` para localizar todas as sequências de 6 dígitos numéricos isoladas por fronteiras de palavra e uni-las com o caractere ponto e vírgula (`;`).

### Consequências
* **Positivas**:
  - Alta performance: execução em tempo real durante a digitação/colagem via evento `input` [VERIFICADO].
  - Imunidade a ruídos textuais (pontuação comum como parênteses, vírgulas e pontos não quebram a extração) [VERIFICADO].
* **Negativas**:
  - Quaisquer números de 6 dígitos que não sejam OSs (como códigos de CEP truncados ou ramais de 6 dígitos) serão capturados indistintamente [INFERIDO].

---

## ADR-003: Estratégia de Cópia com Fallback Híbrido (`navigator.clipboard` + `execCommand`)

* **Status**: Aceito e Implementado [LIDO NO CÓDIGO: index.html:251-260].
* **Data**: 2026-10-22.

### Contexto
A API `navigator.clipboard.writeText` é a especificação moderna da W3C, porém exige contextos seguros (`HTTPS`) ou permissões explícitas. Quando o arquivo é executado via protocolo de arquivo local (`file://`) em certas políticas restritivas do Chromium ou navegadores corporativos legados, a Promise pode ser rejeitada [INFERIDO: especificações W3C].

### Decisão
Implementar um padrão `try/catch`:
```javascript
try {
  await navigator.clipboard.writeText(textToCopy);
} catch {
  outputEl.select();
  document.execCommand('copy');
}
```
[LIDO NO CÓDIGO: index.html:255-260].

### Consequências
* **Positivas**:
  - Resiliência máxima em qualquer versão de navegador [VERIFICADO: teste E2E executou com sucesso].
* **Negativas**:
  - `document.execCommand` é uma API obsoleta (*deprecated*) no padrão Web atual, embora mantida para compatibilidade [LIDO NA ESPECIFICAÇÃO W3C].

---

## ADR-004: Não Ordenação e Não Deduplicação dos Elementos Extraídos

* **Status**: Ativo no Código [LIDO NO CÓDIGO: index.html:237-249].
* **Data**: 2026-10-22.

### Contexto
O projeto foi denominado em pastas e metadados como "Projeto Ordenação OS". No entanto, os operadores podem precisar auditar as ocorrências exatamente na ordem em que aparecem no relatório de origem, ou correlacionar com planilhas de trabalho linha por linha [INFERIDO: hipótese de design].

### Decisão
O código atual mantém a ordem natural de casamento da regex (`rawText.match(...)`) e une os elementos diretamente (`matches.join(';')`), sem chamar `.sort()` e sem aplicar `new Set(matches)`.

### Consequências
* **Positivas**:
  - Preserva a rastreabilidade posicional com o texto original [VERIFICADO].
* **Negativas / Riscos**:
  - Divergência conceitual com o nome do repositório ("organizar número de os" / "Ordenação OS") [LIDO NO CÓDIGO vs DOCS].
  - Requer confirmação formal com o autor/mantenedor sobre se a ordenação ascendente/descendente e a remoção de duplicatas são funcionalidades pendentes [INFERIDO: registrado em `docs/REVISAO.md`].
