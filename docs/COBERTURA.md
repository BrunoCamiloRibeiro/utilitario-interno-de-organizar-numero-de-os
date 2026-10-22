# Relatório Oficial de Cobertura (docs/COBERTURA.md)

Este documento apresenta a auditoria quantitativa de cobertura do projeto conforme exigido na Fase 4c, medindo a proporção de funcionalidades documentadas, cobertura de testes automatizados e validação empírica de exemplos [VERIFICADO].

---

## 1. Resumo Executivo das Métricas

| Dimensão Auditada | Total Existente | Cobertura Auditada | Percentual Efetivo | Status |
| :--- | :--- | :--- | :--- | :--- |
| **Funcionalidades do Código Documentadas** | 10 | 10 | **100,0%** | [VERIFICADO] |
| **Funcionalidades Cobertas por Testes E2E** | 10 | 10 | **100,0%** | [VERIFICADO] |
| **Ramos Lógicos de Decisão no Código (Branches)** | 6 | 6 | **100,0%** | [VERIFICADO] |
| **Ouvintes de Evento do DOM (Event Listeners)** | 4 | 4 | **100,0%** | [VERIFICADO] |
| **Exemplos Citados nos Manuais Verificados em Execução** | 5 | 5 | **100,0%** | [VERIFICADO] |

---

## 2. Detalhamento por Funcionalidade

| ID | Funcionalidade Identificada no Código | Linhas de Código | Documentada em docs/ | Testada em E2E? | Status de Verificação |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **F-01** | Extração de números de 6 dígitos (`\b\d{6}\b`) | [index.html:239](file:///home/brunocr/Documentos/SMAURB/Projeto%20Ordena%C3%A7%C3%A3o%20OS/index.html#L239) | `docs/tecnica/04_modelo_dados_e_protocolos.md` | `test_regex_boundary_and_length_rules` | [VERIFICADO] |
| **F-02** | Concatenação de itens por ponto e vírgula (`;`) | [index.html:242](file:///home/brunocr/Documentos/SMAURB/Projeto%20Ordena%C3%A7%C3%A3o%20OS/index.html#L242) | `docs/tecnica/04_modelo_dados_e_protocolos.md` | `test_extraction_on_input_event` | [VERIFICADO] |
| **F-03** | Reatividade instantânea ao evento `input` | [index.html:280](file:///home/brunocr/Documentos/SMAURB/Projeto%20Ordena%C3%A7%C3%A3o%20OS/index.html#L280) | `docs/tecnica/03_visao_execucao_fluxos.md` | `test_extraction_on_input_event` | [VERIFICADO] |
| **F-04** | Disparo manual via botão "Formatar" | [index.html:281](file:///home/brunocr/Documentos/SMAURB/Projeto%20Ordena%C3%A7%C3%A3o%20OS/index.html#L281) | `docs/tecnica/05_referencia_modulos_e_apis.md` | `test_format_button_click` | [VERIFICADO] |
| **F-05** | Cópia assíncrona moderna (`navigator.clipboard`) | [index.html:256](file:///home/brunocr/Documentos/SMAURB/Projeto%20Ordena%C3%A7%C3%A3o%20OS/index.html#L256) | `docs/tecnica/05_referencia_modulos_e_apis.md` | `test_copy_button_and_feedback` | [VERIFICADO] |
| **F-06** | Fallback síncrono de cópia (`execCommand`) | [index.html:259](file:///home/brunocr/Documentos/SMAURB/Projeto%20Ordena%C3%A7%C3%A3o%20OS/index.html#L259) | `docs/tecnica/05_referencia_modulos_e_apis.md` | `test_copy_button_and_feedback` | [VERIFICADO] |
| **F-07** | Feedback visual "Copiado!" com reversão em 1500ms | [index.html:264-270](file:///home/brunocr/Documentos/SMAURB/Projeto%20Ordena%C3%A7%C3%A3o%20OS/index.html#L264) | `docs/tecnica/03_visao_execucao_fluxos.md` | `test_copy_button_and_feedback` | [VERIFICADO] |
| **F-08** | Botão Limpar com restauração de foco em `inputEl` | [index.html:273-278](file:///home/brunocr/Documentos/SMAURB/Projeto%20Ordena%C3%A7%C3%A3o%20OS/index.html#L273) | `docs/tecnica/03_visao_execucao_fluxos.md` | `test_clear_button` | [VERIFICADO] |
| **F-09** | Contador com flexão de singular ("1 OS") e plural | [index.html:244](file:///home/brunocr/Documentos/SMAURB/Projeto%20Ordena%C3%A7%C3%A3o%20OS/index.html#L244) | `docs/tecnica/05_referencia_modulos_e_apis.md` | `test_singular_plural_badge` | [VERIFICADO] |
| **F-10** | Layout adaptativo para telas móveis (`@media <= 680px`) | [index.html:180-197](file:///home/brunocr/Documentos/SMAURB/Projeto%20Ordena%C3%A7%C3%A3o%20OS/index.html#L180) | `docs/usuario/03_referencia_interface.md` | `test_responsive_mobile_viewport` | [VERIFICADO] |

---

## 3. Auditoria dos Exemplos Citados nos Manuais

Todos os exemplos de texto, entrada e saída contidos na pasta `docs/usuario/` foram reproduzidos e validados através do navegador Google Chrome:

1. **Exemplo do Tutorial de Primeiros Passos** (`docs/usuario/01_primeiros_passos.md`):
   - Entrada: `"Segue relação de vistorias: a fiscalização lavrou a OS 739241 na parte da manhã..."`
   - Saída esperada e obtida: `739241;739710;739813` (3 OSs) [VERIFICADO].
2. **Exemplo do Guia de Tarefa 1 (Extração)** (`docs/usuario/02_guias_por_tarefa.md`):
   - Entrada: `"Fiscalização na OS 740588 e na OS 739241 concluída com sucesso."`
   - Saída esperada e obtida: `740588;739241` (2 OSs) [VERIFICADO].
3. **Exemplo do Guia de Tarefa 4 (Duplicatas)** (`docs/usuario/02_guias_por_tarefa.md`):
   - Entrada: `"Relatório de manhã: 739241 \n Relatório de tarde: 739241 \n Revisão final: 739710"`
   - Saída esperada e obtida: `739241;739241;739710` (3 OSs) [VERIFICADO].
4. **Exemplo de Limite Numérico Rejeitado** (`docs/usuario/05_solucao_de_problemas.md`):
   - Entrada: `"OS 12345 e OS 1234567"`
   - Saída esperada e obtida: `""` (0 OSs) [VERIFICADO].
5. **Exemplo de Erro e Correção** (`docs/usuario/05_solucao_de_problemas.md`):
   - Entrada com erro: `"Verificado processo OS739241 e OS 12345 (antiga). Processo novo: 739.710."` -> Resultado obtido: `0 OSs` [VERIFICADO].
   - Entrada corrigida: `"Verificado processo OS 739241 e OS 739710."` -> Resultado obtido: `739241;739710` [VERIFICADO].
