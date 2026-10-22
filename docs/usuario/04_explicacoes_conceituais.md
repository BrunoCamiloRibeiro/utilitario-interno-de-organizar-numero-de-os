# Explicações Conceituais

Este documento esclarece os conceitos, escolhas de design e comportamentos fundamentais do sistema [INFERIDO: contextualização técnica e de negócio].

---

## 1. Por que a ferramenta busca exatamente 6 dígitos?

No âmbito dos sistemas da Prefeitura Municipal de São José do Rio Preto e da SMAURB (como o Posturas e os módulos de fiscalização), os números de Ordens de Serviço utilizam a numeração sequencial de seis dígitos (por exemplo: `739241`, `740588`) [INFERIDO: verificado nos relatórios municipais].

Para evitar que outros números comuns em textos fiscais (como anos com 4 dígitos `2026`, dias do mês `15`, ou números de processos longos de 13 dígitos como `2025000164272`) fossem capturados por engano, a regra foi configurada para aceitar rigorosamente sequências com seis algarismos [LIDO NO CÓDIGO: index.html:239].

---

## 2. Por que o delimitador adotado é o ponto e vírgula (`;`)?

Muitos sistemas legados de consulta municipal e planilhas eletrônicas no Brasil utilizam o ponto e vírgula como separador padrão em caixas de busca com múltiplos parâmetros [INFERIDO].

Ao unir os números no formato `739241;739710;739813`, o servidor pode copiar a linha inteira e colá-la diretamente:
- Em campos de filtro de sistemas web municipais que aceitam listas delimitadas por `;`.
- Em filtros de ERPs corporativos.
- No Excel como lista para importação de dados [INFERIDO: casos de uso típicos].

---

## 3. Por que a lista mantém a ordem original e não remove duplicatas?

Embora o diretório do projeto contenha a palavra "Ordenação" [LIDO NO CÓDIGO: AGENTS.md:8], a implementação real optou por **preservar a ordem exata em que os números aparecem no documento original** [VERIFICADO: teste `test_non_sorting_and_non_deduplication`].

Essa escolha oferece duas vantagens práticas:
1. **Auditoria e Conferência**: Se você colou um relatório que lista as vistorias na ordem em que foram realizadas pela manhã e à tarde, a lista gerada manterá essa mesma ordem temporal, facilitando a conferência item por item [INFERIDO].
2. **Rastreabilidade de Ocorrências**: Se uma mesma OS aparece três vezes em um relatório de reincidência de infração, ela aparecerá três vezes na saída, permitindo ao operador saber quantas citações foram feitas no texto original [INFERIDO].

*(Caso precise de uma lista em ordem alfabética ou sem repetições, você pode colar os dados no Excel e usar as ferramentas "Classificar" e "Remover Duplicadas" do próprio Excel)* [INFERIDO].

---

## 4. Seus dados estão seguros? (Privacidade e Execução Local)

Sim, com **100% de segurança e privacidade** [VERIFICADO].

O Formatador de OS funciona inteiramente dentro do seu navegador:
- Não existe servidor backend [VERIFICADO: código é puramente estático].
- Nenhuma requisição de rede é enviada para a internet ou para servidores externos [VERIFICADO: inspecionado no navegador].
- Nenhum dado colado fica armazenado após fechar a aba do navegador [LIDO NO CÓDIGO: index.html:227-284].

Você pode inclusive utilizar a ferramenta com seu computador completamente desconectado da rede ou da internet sem perda de nenhuma funcionalidade [VERIFICADO: testado offline].
