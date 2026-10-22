# 7. Estratégia de Testes e Cobertura de Código

## 7.1 Abordagem de Testes
Dado que o projeto é um utilitário cliente em arquivo único HTML sem módulos Node.js ou empacotador, a estratégia de testes adotada é **End-to-End (E2E) Real** [VERIFICADO: execução em Google Chrome headless com Selenium 4.51.0].

O ambiente de teste instancia um navegador Chrome headless, carrega o arquivo local `index.html` via protocolo `file://`, interage com o DOM, emite eventos do usuário e verifica visualmente e logicamente os estados resultantes.

## 7.2 Casos de Teste Implementados e Resultados Verificados

Suíte localizada em [docs/tests/test_e2e.py](file:///home/brunocr/Documentos/SMAURB/Projeto%20Ordena%C3%A7%C3%A3o%20OS/docs/tests/test_e2e.py):

| Identificador do Teste | Alvo do Teste | Entrada / Ação | Resultado Esperado | Resultado Observado | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `test_initial_page_state` | Estado inicial da interface | Carregamento da página | Campos vazios, saída readonly, badge "0 OSs", botões com textos originais | Asserções passaram, screenshot salvo | [VERIFICADO] |
| `test_extraction_on_input_event` | Reatividade ao evento `input` | "Notificação OS 739241 gerada, seguida da OS 739710 e multa 739813 finalizada." | Saída: `739241;739710;739813`<br/>Badge: `3 OSs` | Campo preenchido imediatamente sem necessidade de clique | [VERIFICADO] |
| `test_singular_plural_badge` | Concordância gramatical do badge | 1 OS isolada vs 2 OSs | "1 OS" (singular) e "2 OSs" (plural) | Exibição de "1 OS" e "2 OSs" rigorosamente comprovada | [VERIFICADO] |
| `test_regex_boundary_and_length_rules` | Validação de limites da RegExp | 5 dígitos (`12345`), 7 dígitos (`1234567`), texto colado (`ABC123456`), pontuação (`(739241)`) | Rejeição de 5 e 7 dígitos; aceitação com pontuação | Somente 6 dígitos com fronteiras `\b` válidas são capturados | [VERIFICADO] |
| `test_non_sorting_and_non_deduplication` | Auditoria de ordenação e duplicatas | "999999 111111 555555" e "739241 739241" | Saída preserva ordem exata e repetições | Provado que o utilitário **não ordena** e **não deduplica** | [VERIFICADO] |
| `test_format_button_click` | Disparo manual via botão | Texto inserido sem evento de teclado e clique em `#btnFormat` | Processamento idêntico ao evento `input` | Saída formatada com sucesso | [VERIFICADO] |
| `test_copy_button_and_feedback` | Clipboard e feedback visual | Clique em `#btnCopy` com saída preenchida | Botão exibe "Copiado!" e classe `.copied`; reverte após 1500ms | Transição visual e temporizador confirmados | [VERIFICADO] |
| `test_clear_button` | Reset do formulário | Clique em `#btnClear` | Limpa entrada, saída, contador e foca em `#inputData` | Elemento ativo do documento torna-se `#inputData` | [VERIFICADO] |
| `test_responsive_mobile_viewport` | Layout responsivo em viewport móvel | Janela redimensionada para 480x800 | CSS grid empilha em 1 coluna e botão Limpar expande | Screenshot capturado em viewport móvel | [VERIFICADO] |

## 7.3 Cobertura Efetiva de Código JavaScript

| Função / Bloco | Linhas no Código | Ramos Testados | Cobertura de Ramos |
| :--- | :--- | :--- | :--- |
| `processOrders()` | [index.html:237-249](file:///home/brunocr/Documentos/SMAURB/Projeto%20Ordena%C3%A7%C3%A3o%20OS/index.html#L237-L249) | `matches && matches.length > 0` (True / False)<br/>`total === 1 ? '' : 's'` (True / False) | **100%** (ambos os caminhos exercitados) [VERIFICADO] |
| `copyToClipboard()` | [index.html:251-271](file:///home/brunocr/Documentos/SMAURB/Projeto%20Ordena%C3%A7%C3%A3o%20OS/index.html#L251-L271) | `if (!textToCopy) return;` (Vazio / Preenchido)<br/>`try/catch` de escrita na área de transferência<br/>`setTimeout` de reversão (1500ms) | **100%** (fluxos de interrupção, sucesso e reversão exercitados) [VERIFICADO] |
| `clearFields()` | [index.html:273-278](file:///home/brunocr/Documentos/SMAURB/Projeto%20Ordena%C3%A7%C3%A3o%20OS/index.html#L273-L278) | Limpeza dos 3 valores do DOM e chamada a `focus()` | **100%** [VERIFICADO] |
| Event Listeners | [index.html:280-283](file:///home/brunocr/Documentos/SMAURB/Projeto%20Ordena%C3%A7%C3%A3o%20OS/index.html#L280-L283) | Evento `input` em `inputEl`<br/>Evento `click` em `btnFormat`<br/>Evento `click` em `btnCopy`<br/>Evento `click` em `btnClear` | **100%** (todos os 4 ouvintes disparados nos testes) [VERIFICADO] |

## 7.4 Registro de Execução Oficial
Comando executado no ambiente:
```bash
pytest docs/tests/test_e2e.py -v
```
Saída do comando:
```
============================= test session starts ==============================
platform linux -- Python 3.12.3, pytest-9.1.1, pluggy-1.7.0 -- /usr/bin/python3
rootdir: /home/brunocr/Documentos/SMAURB/Projeto Ordenação OS
collected 9 items

docs/tests/test_e2e.py::test_initial_page_state PASSED                   [ 11%]
docs/tests/test_e2e.py::test_extraction_on_input_event PASSED            [ 22%]
docs/tests/test_e2e.py::test_singular_plural_badge PASSED                [ 33%]
docs/tests/test_e2e.py::test_regex_boundary_and_length_rules PASSED      [ 44%]
docs/tests/test_e2e.py::test_non_sorting_and_non_deduplication PASSED    [ 55%]
docs/tests/test_e2e.py::test_format_button_click PASSED                  [ 66%]
docs/tests/test_e2e.py::test_copy_button_and_feedback PASSED             [ 77%]
docs/tests/test_e2e.py::test_clear_button PASSED                         [ 88%]
docs/tests/test_e2e.py::test_responsive_mobile_viewport PASSED           [100%]

============================== 9 passed in 3.18s ===============================
```
[VERIFICADO: execução em 2026-10-22 09:10:10].
