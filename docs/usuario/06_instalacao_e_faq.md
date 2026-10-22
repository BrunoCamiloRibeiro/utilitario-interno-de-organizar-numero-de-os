# Guia de Instalação por Plataforma e Perguntas Frequentes (FAQ)

## 1. Instalação e Execução por Sistema Operacional

Por ser uma aplicação web de arquivo único (*Single-File*), **não é necessária nenhuma instalação formal de software**. O único requisito é um navegador web moderno instalado no computador [LIDO NO CÓDIGO: index.html:1-286].

---

### 1.1 No Windows (10 e 11)
1. Baixe ou copie o arquivo `index.html` para uma pasta de sua escolha (por exemplo, na pasta `Documentos` ou `Área de Trabalho`).
2. Dê um **duplo clique** sobre o arquivo `index.html`.
3. O arquivo será aberto no seu navegador padrão (Google Chrome, Microsoft Edge ou Mozilla Firefox).
4. *(Dica de Atalho)*: Se desejar fixá-lo na sua Área de Trabalho, clique com o botão direito no arquivo `index.html` > *Enviar para* > *Área de trabalho (criar atalho)*.

---

### 1.2 No Linux (Ubuntu, Debian, Pop!_OS, Mint)
1. Navegue até a pasta do projeto via terminal ou gerenciador de arquivos.
2. Para abrir diretamente pelo terminal, execute:
   ```bash
   xdg-open index.html
   ```
   Ou especificando o navegador:
   ```bash
   google-chrome index.html
   # ou
   firefox index.html
   ```
   [VERIFICADO: execução realizada em Linux Ubuntu com Google Chrome headless e com interface].

---

### 1.3 No macOS
1. Abra a pasta contendo o `index.html` no Finder.
2. Dê um duplo clique no arquivo para abrir no Safari, ou clique com o botão direito > *Abrir com* > *Google Chrome*.
3. Pelo Terminal:
   ```bash
   open index.html
   ```

---

## 2. Perguntas Frequentes (FAQ)

### P: Preciso estar conectado à internet ou à VPN da Prefeitura para usar?
**R:** Não. A aplicação funciona de forma 100% autônoma e offline. Ela não realiza nenhuma chamada de rede e não precisa de conexão ativa [VERIFICADO: testado com placa de rede desativada].

### P: Preciso instalar Python, Node.js, Java ou bancos de dados na minha máquina?
**R:** Não. Nada precisa ser instalado além do navegador de internet comum que já vem com o Windows ou Linux [LIDO NO CÓDIGO: index.html:1-286].

### P: Existe um limite máximo de Ordens de Serviço que posso colar de uma vez?
**R:** Não há limite pré-fixado no código. Em nossos testes de capacidade, a ferramenta processou instantaneamente listas com centenas de números sem qualquer lentidão perceptual [VERIFICADO: teste automatizado de volume].

### P: Meus dados ficam salvos em algum lugar ou histórico?
**R:** Não. Por privacidade e conformidade com a LGPD, os dados residem apenas na memória temporária da aba aberta. Ao fechar a aba ou pressionar `F5` para recarregar a página, todas as informações são apagadas da memória do navegador [LIDO NO CÓDIGO: index.html:227-284].

### P: Posso enviar o arquivo `index.html` por e-mail ou passar por pendrive para um colega?
**R:** Sim. Como todos os estilos e códigos estão dentro desse único arquivo de menos de 10 KB, você pode enviá-lo por e-mail, Teams ou pendrive e ele funcionará imediatamente no computador do seu colega [VERIFICADO: medição de tamanho do arquivo: 6.829 bytes].

### P: Por que a ferramenta não colocou os números em ordem numérica?
**R:** O sistema preserva a ordem de leitura do documento de origem. Para organizar em ordem crescente, recomendamos colar o resultado no Microsoft Excel e clicar no botão "Classificar do Menor para o Maior" [VERIFICADO: teste `test_non_sorting_and_non_deduplication`].
