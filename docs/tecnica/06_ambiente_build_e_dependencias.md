# 6. Build, Configuração, Dependências e Ambiente de Desenvolvimento

## 6.1 Etapa de Build (Compilação e Empacotamento)
O projeto **não requer etapa de compilação ou build** [VERIFICADO: execução direta de `index.html` em navegador sem etapas intermediárias].
- Não há `webpack`, `vite`, `esbuild`, `babel` ou compiladores TypeScript [LIDO NO CÓDIGO: ausência de package.json ou configs de build].
- O arquivo [index.html](file:///home/brunocr/Documentos/SMAURB/Projeto%20Ordena%C3%A7%C3%A3o%20OS/index.html) é servido ou aberto diretamente no navegador (`file://` ou qualquer servidor HTTP estático) [VERIFICADO: teste E2E].

## 6.2 Dependências de Produção
- **Bibliotecas Externas**: **0** [LIDO NO CÓDIGO: index.html:1-286].
- **Fontes Remotas**: Nenhuma. O CSS utiliza fontes nativas do sistema operacional via pilha *system-ui*: `-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif` [LIDO NO CÓDIGO: index.html:15].
- **Ícones**: Nenhum pacote externo (FontAwesome, Material Icons, etc.) é carregado [LIDO NO CÓDIGO: index.html:1-286].

## 6.3 Dependências de Teste e Documentação (Ambiente de Engenharia)
Para execução da suíte de testes de regressão automatizada e geração da documentação estática:

| Pacote / Ferramenta | Versão Instalada / Detectada | Finalidade | Comando de Verificação |
| :--- | :--- | :--- | :--- |
| **Python** | 3.12.3 | Execução de testes e scripts auxiliares | `python3 --version` [VERIFICADO] |
| **Google Chrome** | 128+ | Navegador headless para testes E2E | `google-chrome --version` [VERIFICADO] |
| **Selenium** | 4.51.0 | Automação e controle do navegador nos testes | `pip show selenium` [VERIFICADO] |
| **Pytest** | 9.1.1 | Framework de asserção e execução de testes | `pytest --version` [VERIFICADO] |
| **MkDocs** | 1.6.1 | Gerador de site de documentação estática | `mkdocs --version` [VERIFICADO] |
| **MkDocs Material**| 9.7.7 | Tema responsivo para MkDocs | `pip show mkdocs-material` [VERIFICADO] |

## 6.4 Volumetria do Código (Medição Estilo cloc/tokei)
Medição realizada sobre [index.html](file:///home/brunocr/Documentos/SMAURB/Projeto%20Ordena%C3%A7%C3%A3o%20OS/index.html) via script Python:

| Linguagem / Seção | Linhas Físicas | Linhas em Branco | Linhas de Comentário | Linhas de Código Efetivo | Percentual do Total |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **HTML** | 40 | 6 | 0 | 34 | 14,0% |
| **CSS** (inline) | 190 | 18 | 0 | 172 | 66,4% |
| **JavaScript** (inline) | 56 | 9 | 0 | 47 | 19,6% |
| **TOTAL** | **286** | **33** | **0** | **253** | **100,0%** |

*(Medição executada pelo interpretador Python 3.12 diretamente sobre o arquivo físico do projeto)* [VERIFICADO].

## 6.5 Requisitos de Ambiente para Execução
- **Sistemas Operacionais Homologados**: Linux (Ubuntu 22.04 / 24.04), Windows 10/11, macOS 12+ [INFERIDO: aplicação web padrão].
- **Navegadores Homologados**: Google Chrome, Mozilla Firefox, Microsoft Edge, Safari [INFERIDO: compatibilidade padrão com HTML5].
- **Como Executar em Modo Desenvolvimento / Local**:
  1. Opção A (Direto no arquivo): Abrir `index.html` com duplo clique no gerenciador de arquivos ou executar `google-chrome index.html`.
  2. Opção B (Servidor Local Python): Executar `python3 -m http.server 8000` na raiz e acessar `http://localhost:8000/`.
