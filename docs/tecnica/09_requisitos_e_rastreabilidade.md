# 9. Requisitos do Sistema e Matriz de Rastreabilidade (ISO/IEC/IEEE 29148)

Os requisitos a seguir foram extraídos formalmente a partir da análise estática e da execução do código-fonte [LIDO NO CÓDIGO] e rotulados segundo as normas de engenharia de requisitos.

---

## 9.1 Requisitos Funcionais (RF)

* **RF-01: Extração Determinística de Números de OS**
  - *Declaração*: O sistema DEVE identificar e extrair todas as sequências numéricas compostas por exatamente 6 dígitos decimais contínuos delimitados por fronteiras de palavra [LIDO NO CÓDIGO: index.html:239].
  - *Critério de Aceitação*: Números de 5 dígitos ou 7 dígitos DEVEM ser ignorados. Letras coladas diretamente aos dígitos DEVEM invalidar o casamento [VERIFICADO].

* **RF-02: Delimitação por Ponto e Vírgula**
  - *Declaração*: O sistema DEVE concatenar todos os números extraídos utilizando o caractere `;` como delimitador, sem espaço após o delimitador e sem delimitador ao final [LIDO NO CÓDIGO: index.html:242].

* **RF-03: Processamento Reativo em Tempo Real**
  - *Declaração*: O sistema DEVE executar a rotina de extração e formatação automaticamente a cada caractere inserido ou colado na área de entrada via evento `input` [LIDO NO CÓDIGO: index.html:280].

* **RF-04: Disparo Manual de Formatação**
  - *Declaração*: O sistema DEVE disponibilizar botão explícito "Formatar" que reexecuta a rotina de extração [LIDO NO CÓDIGO: index.html:221, 281].

* **RF-05: Cópia com Notificação Visual Temporária**
  - *Declaração*: O sistema DEVE copiar o texto da caixa de saída para a área de transferência do usuário, alterando o rótulo do botão para "Copiado!" com estilo verde durante 1500ms antes de retornar ao estado original [LIDO NO CÓDIGO: index.html:251-271] [VERIFICADO].

* **RF-06: Limpeza Total e Restauração de Foco**
  - *Declaração*: O sistema DEVE limpar o campo de entrada, a saída, redefinir o contador para "0 OSs" e posicionar o foco do teclado no campo de entrada ao acionar o botão "Limpar" [LIDO NO CÓDIGO: index.html:273-278] [VERIFICADO].

* **RF-07: Flexão Gramatical do Contador de OSs**
  - *Declaração*: O sistema DEVE exibir o contador de itens no cabeçalho respeitando as regras gramaticais: "0 OSs" (vazio), "1 OS" (singular) e "N OSs" (plural para N > 1) [LIDO NO CÓDIGO: index.html:244, 247] [VERIFICADO].

---

## 9.2 Requisitos Não Funcionais (RNF)

* **RNF-01: Autonomia e Execução Local (*Offline*)**
  - *Declaração*: A aplicação DEVE funcionar integralmente sem conexão com a internet, sem efetuar requisições HTTP e sem carregar recursos de terceiros [VERIFICADO: execução sem rede].

* **RNF-02: Responsividade e Layout Adaptativo**
  - *Declaração*: A interface DEVE adaptar-se a telas com largura igual ou inferior a 680 pixels, empilhando as áreas de texto verticalmente em coluna única e estendendo botões para preenchimento de largura [LIDO NO CÓDIGO: index.html:180-197] [VERIFICADO: teste `test_responsive_mobile_viewport`].

* **RNF-03: Resiliência de Acesso à Área de Transferência**
  - *Declaração*: O sistema DEVE possuir mecanismo de contingência para transferência de texto caso a API assíncrona `navigator.clipboard` seja bloqueada pelo navegador [LIDO NO CÓDIGO: index.html:255-260] [VERIFICADO].

---

## 9.3 Matriz de Rastreabilidade Bidirecional

| Requisito | Código-Fonte (Arquivo:Linhas) | Caso de Teste E2E (docs/tests/test_e2e.py) | Seção do Manual do Usuário |
| :--- | :--- | :--- | :--- |
| **RF-01** (Extração 6 dígitos) | [index.html:239](file:///home/brunocr/Documentos/SMAURB/Projeto%20Ordena%C3%A7%C3%A3o%20OS/index.html#L239) | `test_regex_boundary_and_length_rules` | [docs/usuario/02_guias_por_tarefa.md#tarefa-1](file:///home/brunocr/Documentos/SMAURB/Projeto%20Ordena%C3%A7%C3%A3o%20OS/docs/usuario/02_guias_por_tarefa.md) |
| **RF-02** (Delimitação `;`) | [index.html:242](file:///home/brunocr/Documentos/SMAURB/Projeto%20Ordena%C3%A7%C3%A3o%20OS/index.html#L242) | `test_extraction_on_input_event` | [docs/usuario/02_guias_por_tarefa.md#tarefa-1](file:///home/brunocr/Documentos/SMAURB/Projeto%20Ordena%C3%A7%C3%A3o%20OS/docs/usuario/02_guias_por_tarefa.md) |
| **RF-03** (Tempo Real `input`) | [index.html:280](file:///home/brunocr/Documentos/SMAURB/Projeto%20Ordena%C3%A7%C3%A3o%20OS/index.html#L280) | `test_extraction_on_input_event` | [docs/usuario/01_primeiros_passos.md](file:///home/brunocr/Documentos/SMAURB/Projeto%20Ordena%C3%A7%C3%A3o%20OS/docs/usuario/01_primeiros_passos.md) |
| **RF-04** (Botão Formatar) | [index.html:281](file:///home/brunocr/Documentos/SMAURB/Projeto%20Ordena%C3%A7%C3%A3o%20OS/index.html#L281) | `test_format_button_click` | [docs/usuario/03_referencia_interface.md](file:///home/brunocr/Documentos/SMAURB/Projeto%20Ordena%C3%A7%C3%A3o%20OS/docs/usuario/03_referencia_interface.md) |
| **RF-05** (Cópia e Feedback) | [index.html:251-271](file:///home/brunocr/Documentos/SMAURB/Projeto%20Ordena%C3%A7%C3%A3o%20OS/index.html#L251-L271) | `test_copy_button_and_feedback` | [docs/usuario/02_guias_por_tarefa.md#tarefa-2](file:///home/brunocr/Documentos/SMAURB/Projeto%20Ordena%C3%A7%C3%A3o%20OS/docs/usuario/02_guias_por_tarefa.md) |
| **RF-06** (Botão Limpar e Foco) | [index.html:273-278](file:///home/brunocr/Documentos/SMAURB/Projeto%20Ordena%C3%A7%C3%A3o%20OS/index.html#L273-L278) | `test_clear_button` | [docs/usuario/02_guias_por_tarefa.md#tarefa-3](file:///home/brunocr/Documentos/SMAURB/Projeto%20Ordena%C3%A7%C3%A3o%20OS/docs/usuario/02_guias_por_tarefa.md) |
| **RF-07** (Badge Singular/Plural) | [index.html:244, 247](file:///home/brunocr/Documentos/SMAURB/Projeto%20Ordena%C3%A7%C3%A3o%20OS/index.html#L244) | `test_singular_plural_badge` | [docs/usuario/03_referencia_interface.md](file:///home/brunocr/Documentos/SMAURB/Projeto%20Ordena%C3%A7%C3%A3o%20OS/docs/usuario/03_referencia_interface.md) |
| **RNF-01** (Execução Offline) | [index.html:1-286](file:///home/brunocr/Documentos/SMAURB/Projeto%20Ordena%C3%A7%C3%A3o%20OS/index.html#L1-L286) | Inspeção de conexões / headless | [docs/usuario/06_instalacao_e_faq.md](file:///home/brunocr/Documentos/SMAURB/Projeto%20Ordena%C3%A7%C3%A3o%20OS/docs/usuario/06_instalacao_e_faq.md) |
| **RNF-02** (Responsividade Móvel) | [index.html:180-197](file:///home/brunocr/Documentos/SMAURB/Projeto%20Ordena%C3%A7%C3%A3o%20OS/index.html#L180-L197) | `test_responsive_mobile_viewport` | [docs/usuario/03_referencia_interface.md](file:///home/brunocr/Documentos/SMAURB/Projeto%20Ordena%C3%A7%C3%A3o%20OS/docs/usuario/03_referencia_interface.md) |
| **RNF-03** (Fallback de Clipboard) | [index.html:257-260](file:///home/brunocr/Documentos/SMAURB/Projeto%20Ordena%C3%A7%C3%A3o%20OS/index.html#L257-L260) | `test_copy_button_and_feedback` | [docs/usuario/05_solucao_de_problemas.md](file:///home/brunocr/Documentos/SMAURB/Projeto%20Ordena%C3%A7%C3%A3o%20OS/docs/usuario/05_solucao_de_problemas.md) |
