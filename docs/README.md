# Central de Documentação do Projeto: Formatador de OS

Bem-vindo à documentação oficial do **Formatador de OS** (Projeto Ordenação OS / SMAURB).
Toda a documentação deste projeto foi construída a partir de **evidência bruta verificada** em execução real, sem suposições não comprovadas [VERIFICADO].

---

## 🧭 Mapa de Navegação da Documentação

### 📘 Documentação do Usuário (`docs/usuario/`)
*Escrita para servidores, fiscais e operadores que não conhecem programação, baseada no framework Diátaxis e na norma ISO/IEC/IEEE 26514:*

1. [**Tutorial de Primeiros Passos**](usuario/01_primeiros_passos.md): Do zero ao primeiro resultado formatado em 3 passos com telas capturadas.
2. [**Guias por Tarefa ("Como Fazer")**](usuario/02_guias_por_tarefa.md):
   - Extrair e formatar OSs de textos e relatórios.
   - Copiar resultado para a área de transferência.
   - Limpar dados e reiniciar formulário.
   - Auditar números repetidos.
3. [**Referência da Interface**](usuario/03_referencia_interface.md): Dicionário de elementos de tela, campos, botões, atalhos de teclado e visualização móvel.
4. [**Explicações Conceituais**](usuario/04_explicacoes_conceituais.md): Motivos para os 6 dígitos, uso do ponto e vírgula, preservação de ordem e privacidade local.
5. [**Solução de Problemas (Troubleshooting)**](usuario/05_solucao_de_problemas.md): Guia de diagnósticos e soluções para comportamentos inesperados.
6. [**Instalação e Perguntas Frequentes (FAQ)**](usuario/06_instalacao_e_faq.md): Como executar no Windows, Linux e macOS, requisitos e FAQ.

---

### ⚙️ Documentação Técnica de Engenharia (`docs/tecnica/`)
*Escrita para engenheiros de software, mantenedores e auditores técnicos, baseada no arc42 e modelo C4:*

1. [**01. Visão Geral e Escopo**](tecnica/01_visao_geral_e_escopo.md): Objetivos, restrições e confronto direto de hipóteses vs evidência no código.
2. [**02. Arquitetura e Componentes (C4)**](tecnica/02_arquitetura_c4_e_componentes.md): Diagramas C4 Níveis 1, 2 e 3 (Mermaid), grafo de dependências e fronteiras.
3. [**03. Visão de Execução e Fluxos**](tecnica/03_visao_execucao_fluxos.md): Diagramas de sequência passo a passo de inicialização, parsing, cópia e reset.
4. [**04. Modelo de Dados e Protocolos**](tecnica/04_modelo_dados_e_protocolos.md): Especificação formal da regex `\b\d{6}\b`, matriz de validação e Clipboard API.
5. [**05. Referência de Módulos e APIs**](tecnica/05_referencia_modulos_e_apis.md): Assinaturas completas, parâmetros, retornos e efeitos colaterais de cada função JS.
6. [**06. Build, Configuração e Ambiente**](tecnica/06_ambiente_build_e_dependencias.md): Volumetria (cloc/tokei), ausência de build e dependências de teste.
7. [**07. Estratégia de Testes e Cobertura**](tecnica/07_estrategia_testes_e_cobertura.md): Suíte de testes E2E reais via Selenium e Chrome Headless.
8. [**08. Decisões de Arquitetura (ADRs)**](tecnica/08_decisoes_arquitetura_adrs.md): Registros formais em padrão MADR (ADR-001 a ADR-004).
9. [**09. Requisitos e Rastreabilidade**](tecnica/09_requisitos_e_rastreabilidade.md): Requisitos ISO/IEC/IEEE 29148 e matriz bidirecional (Requisito ↔ Código ↔ Teste ↔ Manual).
10. [**10. Riscos, Dívida Técnica e Limitações**](tecnica/10_riscos_divida_tecnica_e_limitacoes.md): Análise crítica de riscos, código morto e dívida técnica.
11. [**11. Glossário**](tecnica/11_glossario.md): Dicionário formal de termos de software e de negócio.

---

### 📊 Auditoria, Qualidade e Governança
* [**Lacunas de Informação (`docs/LACUNAS.md`)**](LACUNAS.md): Registro explícito do que não está evidenciado no código e necessita confirmação do autor.
* [**Métricas de Cobertura (`docs/COBERTURA.md`)**](COBERTURA.md): Percentual de funcionalidades documentadas, testadas e exemplos verificados.
* [**Revisão Crítica e Teste a Frio (`docs/REVISAO.md`)**](REVISAO.md): Perguntas objetivas para o autor e roteiro de teste cego para novos colaboradores.
* [**Script de CI e Verificação (`docs/scripts/ci_check.py`)**](scripts/ci_check.py): Verificador de integridade de links, sintaxe markdown e executor de testes E2E.
