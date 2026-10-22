<div align="center">

# 📑 Formatador de OS (SMAURB)

**Utilitário interno, leve e 100% autônomo para extração, contagem e padronização de Ordens de Serviço municipais.**

[![Testes E2E](https://img.shields.io/badge/Testes%20E2E-9%20Passando-brightgreen?style=flat-square&logo=pytest)](docs/tests/test_e2e.py)
[![Dependências](https://img.shields.io/badge/Dependências-0%20(Zero)-blue?style=flat-square)](index.html)
[![Offline First](https://img.shields.io/badge/Modo-100%25%20Offline-orange?style=flat-square)](index.html)
[![Linguagem](https://img.shields.io/badge/Stack-Vanilla%20HTML5%20%7C%20CSS3%20%7C%20ES2017-yellow?style=flat-square)](index.html)
[![Documentação](https://img.shields.io/badge/Docs-MkDocs%20Material-indigo?style=flat-square)](docs/README.md)

<br/>

<img src="docs/assets/screenshot_initial.png" alt="Interface Principal do Formatador de OS" width="850px" style="border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.1);"/>

</div>

---

## 📖 Sobre o Projeto

O **Formatador de OS** é uma aplicação web de arquivo único (*Single-Page Utility* / Monofólio) projetada para agilizar o fluxo de trabalho de auditores, servidores e fiscais da **SMAURB** (Secretaria Municipal de Meio Ambiente e Urbanismo).

Frequentemente, números de Ordens de Serviço chegam aos operadores dispersos em relatórios de vistorias, despachos administrativos em PDF ou mensagens de e-mail. Este utilitário processa instantaneamente qualquer bloco de texto não estruturado, localiza todas as OSs válidas com padrão de **6 dígitos numéricos** e as formata como uma lista delimitada por ponto e vírgula (`;`), pronta para colagem direta em consultas em lote de sistemas legados ou planilhas do Microsoft Excel.

---

## ✨ Principais Funcionalidades

- ⚡ **Processamento Reativo em Tempo Real**: Extrai e formata automaticamente enquanto você digita ou cola (`Ctrl + V`), sem necessidade obrigatória de cliques.
- 🎯 **Filtro Determinístico via Regex**: Utiliza a expressão regular `/\b\d{6}\b/g` com asserções de fronteira de palavra, capturando apenas OSs de 6 dígitos decimais e ignorando números de processos longos, anos ou datas.
- 🔢 **Contador Dinâmico com Concordância**: Exibe no cabeçalho o quantitativo exato de itens encontrados, aplicando flexão gramatical automática (`0 OSs`, `1 OS`, `N OSs`).
- 📋 **Cópia Rápida com Feedback Visual**: Botão de cópia integrado à Clipboard API moderna (com fallback síncrono para ambientes restritos) que fornece confirmação visual instantânea (*"Copiado!"* em verde por 1,5s).
- 🧹 **Reset em 1 Clique com Foco Automático**: O botão *Limpar* esvazia ambos os campos, restaura o contador e posiciona o cursor de volta na caixa de entrada para o próximo lote.
- 🔒 **Privacidade Total & 100% Offline**: Sem requisições de rede, sem servidores backend, sem armazenamento persistente (cookies ou LocalStorage). Seus dados nunca saem da sua estação de trabalho.
- 📱 **Layout Responsivo**: Interface limpa baseada em CSS Grid e Flexbox, adaptando-se confortavelmente a monitores widescreen ou telas móveis estreitas (`max-width: 680px`).

---

## 🚀 Demonstração Prática

### Entrada (Texto Bruto / Relatório Fiscal):
```text
Segue relação de vistorias realizadas pela manhã:
Fiscalização lavrou a OS 739241 no setor Norte.
À tarde, foram vistoriadas as OS 739710 e também a OS 739813 (auto de infração).
Desconsiderar código auxiliar 12345 e ano 2026.
```

### Saída Gerada Automaticamente:
```text
739241;739710;739813
```
*Contador exibido: **3 OSs** | Pronto para copiar com 1 clique.*

<div align="center">
  <img src="docs/assets/screenshot_filled.png" alt="Demonstração com Dados Preenchidos" width="750px"/>
</div>

---

## 🛠️ Como Utilizar

Por se tratar de uma aplicação de arquivo único sem etapas de compilação (*zero build step*), **não é necessário instalar Node.js, Python ou bancos de dados** para usar a ferramenta.

### 🖥️ No Windows
1. Baixe ou clone este repositório.
2. Dê um **duplo clique** sobre o arquivo [`index.html`](index.html).
3. O aplicativo abrirá imediatamente no seu navegador padrão (Google Chrome, Microsoft Edge ou Firefox).
4. *(Opcional)*: Crie um atalho do arquivo `index.html` na sua Área de Trabalho para acesso rápido.

### 🐧 No Linux
Abra pelo terminal ou gerenciador de arquivos:
```bash
xdg-open index.html
# ou
google-chrome index.html
```

### 🍎 No macOS
```bash
open index.html
```

---

## 🔍 Regras de Extração e Validação

A ferramenta segue regras estritas de casamento para evitar falsos positivos em textos fiscais:

| Padrão no Texto | Casamento / Saída | Justificativa Técnica |
| :--- | :---: | :--- |
| `OS 739241` | `739241` | Sequência exata de 6 dígitos delimitada por espaço. |
| `(739241), [739710].` | `739241;739710` | Sinais de pontuação comuns ativam fronteira de palavra `\b`. |
| `OS 12345` | *(Ignorado)* | Apenas 5 dígitos (abaixo do padrão de OS). |
| `Processo 20261022` | *(Ignorado)* | 8 dígitos (acima do padrão de OS). |
| `OS739241` | *(Ignorado)* | Letra colada ao dígito sem espaço suprime a fronteira `\b`. |
| `739241 739241` | `739241;739241` | Preserva duplicatas (não deduplica automaticamente). |
| `999999 111111` | `999999;111111` | Preserva a ordem original do documento (não ordena). |

---

## 📂 Estrutura do Repositório

```text
utilitario-interno-de-organizar-numero-de-os/
├── index.html                   # Aplicação web pura (HTML5 + CSS3 + JavaScript)
├── README.md                    # Esta documentação inicial do GitHub
├── DOCS_MAP.md                  # Mapa de arquitetura, pontos de entrada e criticidade de risco
├── DOCS_REPORT.md               # Relatório de governança, intenções não confirmadas e perguntas
├── VERIFICATION.md              # Evidência bruta de testes, AST invariante e linters
├── mkdocs.yml                   # Configuração do site de documentação MkDocs Material
└── docs/                        # Central de documentação aprofundada
    ├── README.md                # Índice de navegação da documentação técnica
    ├── LACUNAS.md               # Catálogo formal de dúvidas e decisões pendentes
    ├── COBERTURA.md             # Matriz de 100% de cobertura de código e testes
    ├── REVISAO.md               # Roteiro de testes a frio para novos colaboradores
    ├── assets/                  # Capturas de tela reais do utilitário
    ├── scripts/
    │   └── ci_check.py          # Script de CI para links, pytest e build estrito
    ├── tests/
    │   └── test_e2e.py          # Suíte de testes automatizados E2E via Selenium Chrome
    ├── tecnica/                 # 11 seções de arquitetura baseadas em arc42 e C4
    └── usuario/                 # 6 guias baseados no framework Diátaxis e ISO 26514
```

---

## 🧪 Suíte de Testes Automatizados & CI

Para desenvolvedores e auditores técnicos que desejam validar o repositório ou estender funcionalidades:

### 1. Pré-requisitos de Desenvolvimento
- Python 3.12+
- Google Chrome instalado

### 2. Instalação das Ferramentas de Teste
```bash
pip install selenium webdriver-manager pytest mkdocs mkdocs-material pydocstyle mypy
```

### 3. Execução dos Testes End-to-End (Selenium Headless)
```bash
pytest docs/tests/test_e2e.py -v
```

### 4. Execução do Pipeline Completo de CI (Links + Testes + MkDocs Estrito)
```bash
python3 docs/scripts/ci_check.py
```

### 5. Visualização Local da Documentação Interativa
```bash
mkdocs serve
```
Acesse `http://127.0.0.1:8000` no seu navegador para navegar pela documentação completa com diagramas interativos Mermaid.

---

## 📚 Documentação Adicional

Para detalhes arquiteturais, requisitos e guias de usuário avançados, consulte:

- 📘 [**Manual do Usuário**](docs/usuario/01_primeiros_passos.md): Passo a passo para novos servidores e guias de resolução de problemas.
- ⚙️ [**Documentação Técnica (arc42/C4)**](docs/tecnica/01_visao_geral_e_escopo.md): Especificação de dados, diagramas de sequência e decisões arquiteturais (ADRs).
- 🗺️ [**Mapa do Sistema**](DOCS_MAP.md): Grafo de chamadas e matriz de risco dos símbolos.
- 🔍 [**Relatório de Verificação**](VERIFICATION.md): Provas de invariância de AST, relatórios de cobertura e validação empírica.

---

## 📄 Licença & Uso Interno

Desenvolvido para uso interno no âmbito da **SMAURB** (Secretaria Municipal de Meio Ambiente e Urbanismo).  
Autor: **Bruno Camilo Ribeiro**
