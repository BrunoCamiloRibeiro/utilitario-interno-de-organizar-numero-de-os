# Guias por Tarefa ("Como Fazer")

Estes guias no estilo *How-To* oferecem instruções orientadas a objetivos diretos para o trabalho diário dos servidores e fiscais.

---

## Tarefa 1: Como Extrair e Formatar Números de OS de um Texto ou Relatório

### Pré-requisitos
- O arquivo `index.html` aberto no navegador de sua preferência [VERIFICADO].
- O texto bruto contendo as Ordens de Serviço (copiado de um e-mail, PDF, planilha ou relatório do Posturas/ACTO) [INFERIDO: fontes habituais].

### Passos de Execução
1. Clique com o botão esquerdo do mouse na área de texto **Entrada** [VERIFICADO].
2. Pressione as teclas `Ctrl + V` (ou clique com o botão direito e escolha *Colar*) para inserir o texto [VERIFICADO].
3. *(Opcional)*: Se a formatação automática não ocorrer de imediato por alguma restrição do navegador, clique no botão azul **Formatar** [LIDO NO CÓDIGO: index.html:281] [VERIFICADO: teste `test_format_button_click`].

### Resultado Esperado
- A área de texto **Saída** exibe todas as sequências numéricas de 6 dígitos encontradas separadas por `;` [VERIFICADO].
- Exemplo verificado em teste:
  - Entrada: `Fiscalização na OS 740588 e na OS 739241 concluída com sucesso.`
  - Saída: `740588;739241` [VERIFICADO].
- O selo no canto superior direito indica a quantidade total encontrada (ex.: `2 OSs`) [VERIFICADO].

### Erros Comuns
- **O número tem 5 ou 7 dígitos**: O sistema ignora silenciosamente números fora do padrão de 6 dígitos. Exemplo: `73924` (5 dígitos) ou `2026102` (7 dígitos) não aparecem na saída [VERIFICADO: teste `test_regex_boundary_and_length_rules`].
- **Letras coladas aos números**: Códigos como `OS739241` (sem espaço entre 'OS' e o número) não serão reconhecidos porque a letra impede o reconhecimento de fronteira de palavra [VERIFICADO]. Corrija adicionando um espaço: `OS 739241`.

---

## Tarefa 2: Como Copiar a Lista Formatada para Colar em Outro Sistema

### Pré-requisitos
- Ter gerado ao menos um resultado válido na caixa **Saída** [VERIFICADO].

### Passos de Execução
1. Localize o botão **Copiar** ao lado do botão Formatar [VERIFICADO].
2. Clique no botão **Copiar** [VERIFICADO].
3. Observe o rótulo do botão mudar para **Copiado!** com um fundo verde suave [VERIFICADO].
4. Abra o programa de destino (como o Excel, bloco de notas ou formulário de consulta) e pressione `Ctrl + V` [VERIFICADO].

### Resultado Esperado
O texto delimitado exatamente como exibido na caixa de saída é colado no destino [VERIFICADO]. Após 1,5 segundo, o botão voltará automaticamente a exibir o texto original **Copiar** [VERIFICADO].

### Erros Comuns
- **Clicar em Copiar com a saída vazia**: Se não houver números na caixa de saída, o botão não reage e não altera para "Copiado!" para evitar que você sobrescreva acidentalmente sua área de transferência com nada [LIDO NO CÓDIGO: index.html:253] [VERIFICADO].

---

## Tarefa 3: Como Limpar a Tela para um Novo Lote

### Pré-requisitos
- Aplicação aberta contendo dados anteriores [VERIFICADO].

### Passos de Execução
1. Clique no botão **Limpar** (localizado à direita da barra de ações) [VERIFICADO].

### Resultado Esperado
- O campo de Entrada fica em branco [VERIFICADO].
- O campo de Saída fica em branco [VERIFICADO].
- O selo de contagem retorna para `0 OSs` [VERIFICADO].
- O cursor de digitação volta automaticamente para o campo de Entrada, permitindo novo `Ctrl + V` imediatamente sem precisar clicar [VERIFICADO: teste `test_clear_button`].

---

## Tarefa 4: Como Garantir que Números Repetidos Sejam Auditados

### Pré-requisitos
- Conhecimento da regra de negócio: o sistema **não elimina duplicatas** e **não reorganiza a ordem dos dados** [VERIFICADO: teste `test_non_sorting_and_non_deduplication`].

### Passos de Execução
1. Insira o texto de entrada. Exemplo real testado:
   ```text
   Relatório de manhã: 739241
   Relatório de tarde: 739241
   Revisão final: 739710
   ```
2. Observe a saída gerada:
   ```text
   739241;739241;739710
   ```
3. O contador indicará `3 OSs` [VERIFICADO].

### Recomendação de Uso
Se você necessita de valores únicos para uma cláusula SQL do tipo `IN (...)`, esteja ciente de que se o mesmo número for citado duas vezes no texto original, ele constará duas vezes na saída. Para remover repetições, use o recurso "Remover Duplicadas" do Excel após colar [INFERIDO: recomendação operacional].
