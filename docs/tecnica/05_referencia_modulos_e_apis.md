# 5. Referência de Módulos e Funções Internas

Todas as funções do sistema residem no escopo global do script inline em [index.html:227-284](file:///home/brunocr/Documentos/SMAURB/Projeto%20Ordena%C3%A7%C3%A3o%20OS/index.html#L227-L284).

---

## 5.1 `processOrders()`

### Assinatura
```javascript
function processOrders(): void
```
[LIDO NO CÓDIGO: index.html:237]

### Descrição
Lê o conteúdo do elemento `#inputData`, extrai números de 6 dígitos via expressão regular `/\b\d{6}\b/g` e escreve o resultado delimitado por `;` no elemento `#outputData`, atualizando o contador `#countBadge`.

### Parâmetros
*Nenhum*. A função consome o estado diretamente do nó do DOM `inputEl` (`#inputData`) [LIDO NO CÓDIGO: index.html:238].

### Retorno
*`void`* (não retorna valor) [LIDO NO CÓDIGO: index.html:237-249].

### Efeitos Colaterais no DOM
- Modifica a propriedade `outputEl.value` [LIDO NO CÓDIGO: index.html:242, 246].
- Modifica a propriedade `countBadge.textContent` com `"0 OSs"`, `"1 OS"` ou `"${total} OSs"` [LIDO NO CÓDIGO: index.html:244, 247].

### Tratamento de Exceções
Não lança exceções conhecidas em circunstâncias normais. Se `inputEl.value` for vazio, `rawText.match(...)` retorna `null`, acionando o ramo `else` seguro [LIDO NO CÓDIGO: index.html:245-248].

---

## 5.2 `copyToClipboard()`

### Assinatura
```javascript
async function copyToClipboard(): Promise<void>
```
[LIDO NO CÓDIGO: index.html:251]

### Descrição
Transfere o conteúdo atual do elemento `#outputData` para a área de transferência do sistema operacional. Alterna a interface visual para exibir confirmação temporária durante 1.500 milissegundos.

### Parâmetros
*Nenhum*. Consome o valor de `outputEl.value` [LIDO NO CÓDIGO: index.html:252].

### Retorno
*`Promise<void>`* [LIDO NO CÓDIGO: index.html:251].

### Fluxo de Erros e Fallback
- Se `outputEl.value` for falsy (vazio), executa `return;` antecipado e encerra sem efeito visual [LIDO NO CÓDIGO: index.html:253].
- Se `navigator.clipboard.writeText` lançar erro (ou for rejeitado por restrição de permissão), o bloco `catch` intercepta o erro silenciosamente, invoca `outputEl.select()` e tenta `document.execCommand('copy')` [LIDO NO CÓDIGO: index.html:257-260].

### Efeitos Colaterais
- Acessa o subsistema de clipboard do sistema operacional [LIDO NO CÓDIGO: index.html:256, 259].
- Limpa qualquer temporizador anterior via `clearTimeout(copyTimeout)` [LIDO NO CÓDIGO: index.html:262].
- Altera `btnCopy.textContent` para `'Copiado!'` e adiciona classe CSS `.copied` [LIDO NO CÓDIGO: index.html:264-265].
- Agenda temporizador (`setTimeout`) de 1500ms para reverter o texto para `'Copiar'` e remover a classe `.copied` [LIDO NO CÓDIGO: index.html:267-270].

---

## 5.3 `clearFields()`

### Assinatura
```javascript
function clearFields(): void
```
[LIDO NO CÓDIGO: index.html:273]

### Descrição
Restaura os campos de formulário e contadores visuais aos seus valores padrão iniciais e devolve o foco do cursor para o campo de entrada.

### Parâmetros
*Nenhum*.

### Retorno
*`void`*.

### Efeitos Colaterais no DOM
- Define `inputEl.value = ''` [LIDO NO CÓDIGO: index.html:274].
- Define `outputEl.value = ''` [LIDO NO CÓDIGO: index.html:275].
- Define `countBadge.textContent = '0 OSs'` [LIDO NO CÓDIGO: index.html:276].
- Invoca `inputEl.focus()` [LIDO NO CÓDIGO: index.html:277] [VERIFICADO: teste `test_clear_button`].

---

## 5.4 Referências de Elementos e Estado Global

```javascript
// Referências de nós no DOM (index.html:228-233)
const inputEl    = document.getElementById('inputData');   // HTMLTextAreaElement
const outputEl   = document.getElementById('outputData');  // HTMLTextAreaElement (readonly)
const btnFormat  = document.getElementById('btnFormat');   // HTMLButtonElement
const btnCopy    = document.getElementById('btnCopy');     // HTMLButtonElement
const btnClear   = document.getElementById('btnClear');    // HTMLButtonElement
const countBadge = document.getElementById('countBadge');  // HTMLSpanElement

// Estado mutable (index.html:235)
let copyTimeout = null; // ID retornado por setTimeout ou null
```
[LIDO NO CÓDIGO: index.html:228-235]
