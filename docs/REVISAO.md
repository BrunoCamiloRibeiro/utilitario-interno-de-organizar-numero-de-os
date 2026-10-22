# Revisão com o Mantenedor e Roteiro de Teste a Frio (docs/REVISAO.md)

Este documento atende à Fase 4e, fornecendo um conjunto de perguntas objetivas para validação com o autor/mantenedor e um roteiro de teste cego (*cold test protocol*) a ser executado por um novo colaborador sem consulta ao código-fonte [INFERIDO: instrumento de governança e validação].

---

## 1. Perguntas Objetivas para o Autor / Mantenedor do Projeto

As perguntas a seguir visam sanar as decisões inferidas e lacunas registradas em `docs/LACUNAS.md`:

1. **Ordenação Numérica**:
   - *Constatação*: O repositório e diretório chamam-se "Projeto Ordenação OS" / "organizar-numero-de-os", porém o código em [index.html:242](file:///home/brunocr/Documentos/SMAURB/Projeto%20Ordena%C3%A7%C3%A3o%20OS/index.html#L242) apenas junta os casamentos na ordem sequencial de texto.
   - *Pergunta*: Devemos implementar uma ordenação numérica (crescente ou decrescente), oferecer um botão de alternância (*checkbox* "Ordenar valores") ou o comportamento atual de preservação da ordem do relatório é o definitivo?
2. **Deduplicação de Valores**:
   - *Constatação*: Se uma OS aparece repetida no texto de entrada, ela permanece repetida na saída.
   - *Pergunta*: A eliminação de duplicatas é um requisito desejado para evitar repetições em consultas SQL/ERP, ou os operadores necessitam ver todas as ocorrências citadas?
3. **Escalaridade dos Dígitos (6 vs 7 algarismos)**:
   - *Constatação*: A expressão regular fixa `{6}` rejeita números de 7 dígitos.
   - *Pergunta*: Há previsão de quando a SMAURB alcançará a OS número 1.000.000? Devemos flexibilizar a expressão regular para `\b\d{6,7}\b`?
4. **Delimitadores Alternativos**:
   - *Constatação*: O delimitador é rigidamente o ponto e vírgula (`;`).
   - *Pergunta*: Seria útil adicionar um seletor para permitir que o usuário escolha entre ponto e vírgula (`;`), vírgula (`,`) ou quebra de linha (`\n`) para colar em colunas do Excel?
5. **Utilidade do Botão "Formatar"**:
   - *Constatação*: A extração é reativa em tempo real através do evento `input`, tornando o botão `#btnFormat` redundante na maioria das interações.
   - *Pergunta*: O botão "Formatar" deve ser preservado para fins de usabilidade e segurança psicológica do usuário, ou deve ser simplificado?

---

## 2. Roteiro de Teste a Frio (Para Nova Pessoa no Projeto)

**Público-Alvo**: Servidor municipal ou estagiário sem acesso ao código-fonte ou conhecimentos de programação.
**Objetivo**: Validar a clareza e suficiência da documentação contida na pasta `docs/usuario/`.

### Protocolo de Teste
*Instrução ao testador: Siga exclusivamente as instruções de `docs/usuario/` sem abrir o editor de código nem inspecionar o HTML.*

#### Teste 1: Abertura e Reconhecimento
- **Ação**: Navegue até a pasta do projeto e abra o arquivo `index.html` com duplo clique.
- **Critério de Sucesso**: A página abre no navegador exibindo duas caixas de texto ("Entrada" e "Saída"), três botões ("Formatar", "Copiar", "Limpar") e um selo com o texto `"0 OSs"`.
- **Registro do Testador**: [ ] Aprovado  [ ] Reprovado (Descrever ocorrência)

#### Teste 2: Extração de Lote Misto
- **Ação**: Copie o seguinte bloco de texto e cole dentro da caixa "Entrada":
  ```text
  Auto de fiscalização nº 739241 lavrado pela equipe A.
  Complementar nº 739710 realizado pela equipe B.
  Ignorar valor de teste 12345 e ano 2026.
  ```
- **Critério de Sucesso**:
  - A caixa "Saída" deve exibir automaticamente: `739241;739710`
  - O selo no canto superior direito deve exibir: `2 OSs`
  - Os números 12345 e 2026 NÃO devem aparecer na saída.
- **Registro do Testador**: [ ] Aprovado  [ ] Reprovado (Descrever ocorrência)

#### Teste 3: Operação de Cópia
- **Ação**: Clique no botão "Copiar". Abra o Bloco de Notas ou um documento em branco e pressione `Ctrl + V`.
- **Critério de Sucesso**:
  - O botão na tela muda brevemente para "Copiado!" em fundo verde claro e volta para "Copiar" após cerca de 1 a 2 segundos.
  - O texto colado no Bloco de Notas deve ser exatamente `739241;739710`.
- **Registro do Testador**: [ ] Aprovado  [ ] Reprovado (Descrever ocorrência)

#### Teste 4: Limpeza do Formulário
- **Ação**: Clique no botão "Limpar".
- **Critério de Sucesso**:
  - A caixa de entrada e a de saída ficam vazias.
  - O contador exibe `"0 OSs"`.
  - O cursor de digitação volta a piscar na caixa "Entrada".
- **Registro do Testador**: [ ] Aprovado  [ ] Reprovado (Descrever ocorrência)
