# Home credit risk default

Para o projeto final do bootcamp do LAMIA (Laboratório de Aprendizado de Máquina e Imagens Aplicados à Indústria - https://www.lamia.sh.utfpr.edu.br/) foi feito um modelo para estimar o risco de emprestimo de credito de acordo com as características pessoais e financeiras dos clientes, o conjunto de dados disponibilizados apresenta dados de diversas fontes, desde dados da empresa que propôs o desafio, até pontuações externas e históricos de solicitação de crédito (https://www.kaggle.com/competitions/home-credit-default-risk/data).

A modelagem dos dados foi feita em cima dos dados disponibilizados pela empresa que propos o desafio, a tabela de treino para algoritmos ja contava com 122 colunas, porem não foi alcançado um resultado aceitavel com apenas estas features, por esse motivo, primeiramente foi realizado uma analise exploratoria dos dados para encontrar algumas possiveis novas variaveis que acrescentassem valor ao modelo criando assim mais 11 novas features. O projeto seguiu as etapas do modelo CRISP-DM, inicialmente na etapa de entendimento do contexto foram realizadas pesquisas conceituais sobre este segmento, com o objetivo de entender onde poderia ser aplicadas esta solução.

Na segunda etapa o objetivo foi de entender o conjunto de dados para tomar a melhor escolha de como tratar/utilizar os dados nesta solução, o conjunto contava com mais de 2GB de dados, foi necessário algumas traduções e pesquisas para entender exatamente cada aspecto das variáveis, por fim foi decidido utilizar a base de dados que a empresa disponibilizou com acréscimo das variáveis explicativas desenvolvidas no inicio do projeto.

E assim com os dados alinhados, o projeto se desenvolveu passando pelas etapas de preparação dos dados, analise do conjunto final(insights) e em seguida a modelagem, os dados foram testados de diversas formas, somente com variaveis categoricas, somente com numericas, normalizadas, padronizadas, excluindo nulls, utilizando sem excluir nenhuma linha, removendo outliers, deixando os dados como estão, e por fim o tipo de tratamento que se saiu melhor foi o que não excluia nenhuma linha da tabela, substituia os dados atraves de alguma metrica como moda, media, mediana, e não removia os outliers. A quantidade de features tambem foi filtrada, neste caso foi utilizado o algoritmo RFE para selecionar as variaveis que seriam utilizadas no dataset final.

Por fim analisando os resultados dos modelos lado a lado com os resultados de pontuação obtidos na competição do kaggle foi selecionado o modelo LGBMClassifier para trabalhar neste projeto. foi alcançado a marca de 0.71164 de score na competição (Competição de 2019), o primeiro lugar em 0.80570 então considerei um ótimo resultado, a principal diferença foi que os primeiros lugares utilizaram uma engenharia de dados mais pesada em toda a base de dados.

# Informações e recomendações:

Caso queira visualizar a dashboard no aplicativo power bi ( recomendado ), este arquivo sera necessario.

- Dados para a dashboard Power Bi: https://drive.google.com/file/d/16OETHvRAzzcok9oTi1Q38l65jvGQqtSB/view?usp=sharing
- O arquivo "Dashboard - HomeCredit.pdf" contem a ilustração da dashboard criada, porem acaba não sendo interativa.

Para rodar o codigo completo sera necessario criar uma pasta fora desta estrutura chamada datasets e colocar estes dois arquivos nela
  
  - Dados da base de treino ( Abt_bureau ): https://drive.google.com/file/d/15N0azotB9V1DlbUeVBE6pEn68soB_hbP/view?usp=sharing
  
  - Dados da base de teste ( Abt_bureau_test ): https://drive.google.com/file/d/10zwNtu07pjNjDYCkxzK1QrLm30JJ5pz1/view?usp=sharing
  
  
