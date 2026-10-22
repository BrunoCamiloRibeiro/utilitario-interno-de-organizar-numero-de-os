# 4. Modelo de Dados, Formatos e Protocolos

## 4.1 Modelo de Dados de Entrada
O sistema aceita como entrada qualquer sequência de caracteres textuais codificada em UTF-8 recebida através de um elemento `HTMLTextAreaElement` (`id="inputData"`) [LIDO NO CÓDIGO: index.html:211].

- **Tipo**: `String` primitiva do JavaScript.
- **Estrutura**: Texto arbitrário não estruturado, contendo quebras de linha, tabulações, caracteres alfanuméricos e sinais de pontuação.
- **Tamanho Máximo**: Limitado exclusivamente pela memória do navegador e limites práticos de renderização de strings no DOM (aproximadamente 512 MB a 1 GB em navegadores V8 de 64 bits) [INFERIDO: restrição do motor V8].

## 4.2 Especificação Formal da Expressão Regular de Extração
A regra de extração central do sistema é definida em [index.html:239](file:///home/brunocr/Documentos/SMAURB/Projeto%20Ordena%C3%A7%C3%A3o%20OS/index.html#L239):
```javascript
const matches = rawText.match(/\b\d{6}\b/g);
```

### Análise Léxica dos Tokens da Expressão Regular:
1. `\b` (Word Boundary): Casamento de largura zero (zero-width assertion) que ocorre onde um caractere de palavra (`\w` = `[a-zA-Z0-9_]`) é precedido ou seguido por um caractere que não seja de palavra, ou no início/fim da string [LIDO NO CÓDIGO].
2. `\d{6}` (Digit Quantifier): Exatamente seis caracteres pertencentes à classe `[0-9]` [LIDO NO CÓDIGO].
3. `\b` (Word Boundary): Segunda asserção de largura zero para delimitar o final do número [LIDO NO CÓDIGO].
4. Flag `/g` (Global Match): Não interrompe no primeiro casamento; percorre todo o texto retornando todas as ocorrências encontradas em um array [LIDO NO CÓDIGO].

### Matriz de Validação de Fronteiras (Testada em Execução Real)

| Exemplo de Entrada | Casamento Observado | Motivo do Casamento / Rejeição | Status |
| :--- | :--- | :--- | :--- |
| `739241` | `['739241']` | Exatamente 6 dígitos isolados por espaços ou início/fim de linha | [VERIFICADO] |
| `OS 739241, 739710.` | `['739241', '739710']` | Espaços e vírgulas são caracteres `\W`, ativando `\b` | [VERIFICADO] |
| `(739241)` | `['739241']` | Parênteses `()` são `\W`, ativando `\b` | [VERIFICADO] |
| `12345` | `null` | Apenas 5 dígitos (menor que o quantificador `{6}`) | [VERIFICADO] |
| `1234567` | `null` | 7 dígitos consecutivos violam a asserção `\b` nos 6 primeiros | [VERIFICADO] |
| `ABC123456` | `null` | Letra `C` adjacente é `\w`, invalidando a asserção `\b` à esquerda | [VERIFICADO] |
| `123456DEF` | `null` | Letra `D` adjacente é `\w`, invalidando a asserção `\b` à direita | [VERIFICADO] |
| `123456_789012` | `null` | Sublinhado `_` é considerado caractere `\w` na especificação ECMAScript, suprimindo o `\b` | [VERIFICADO] |
| `739241-739710` | `['739241', '739710']` | Hífen `-` é `\W`, portanto ambos os lados são reconhecidos como OSs válidas | [VERIFICADO] |

## 4.3 Modelo de Dados de Saída
O dado de saída gerado por `processOrders()` em [index.html:242](file:///home/brunocr/Documentos/SMAURB/Projeto%20Ordena%C3%A7%C3%A3o%20OS/index.html#L242) segue o padrão de lista delimitada (*Delimiter-Separated Values*):

- **Delimitador**: Ponto e vírgula literal (`;`).
- **Ordem dos Elementos**: Estritamente a ordem de varredura sequencial do texto original (ordem de aparição, sem ordenação alfanumérica ou numérica) [VERIFICADO: teste `test_non_sorting_and_non_deduplication`].
- **Unicidade de Elementos**: Permite duplicatas. Se o mesmo número aparecer 3 vezes no texto original, aparecerá 3 vezes na saída [VERIFICADO: teste `test_non_sorting_and_non_deduplication`].
- **Terminação**: Sem delimitador no final da string (`join(';')` não insere ponto e vírgula após o último elemento) [LIDO NO CÓDIGO: index.html:242].
- **Exemplo de Saída**: `739241;739710;739813` [VERIFICADO].

## 4.4 Protocolos e APIs de Navegador Utilizadas

### 1. W3C Asynchronous Clipboard API (`navigator.clipboard.writeText`)
- Chamada primária em [index.html:256](file:///home/brunocr/Documentos/SMAURB/Projeto%20Ordena%C3%A7%C3%A3o%20OS/index.html#L256).
- Retorna uma `Promise<void>` [LIDO NO CÓDIGO].
- **Requisito de Contexto Seguro**: Em navegadores modernos, `navigator.clipboard` exige contexto seguro (`https://` ou `localhost` / `file://`) e foco ativo da janela/documento [INFERIDO: especificação W3C Clipboard].

### 2. Document Object Model Level 2 ExecCommand Fallback (`document.execCommand`)
- Fallback em [index.html:258-259](file:///home/brunocr/Documentos/SMAURB/Projeto%20Ordena%C3%A7%C3%A3o%20OS/index.html#L258-L259).
- Acionado se a Promise for rejeitada ou se a API `navigator.clipboard` não estiver disponível.
- Executa `outputEl.select()` seguido de `document.execCommand('copy')` para garantir compatibilidade com ambientes corporativos restritos ou navegadores legados [LIDO NO CÓDIGO: index.html:258-259].
