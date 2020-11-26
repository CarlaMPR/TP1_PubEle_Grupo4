# TP1_PubEle_Grupo4
TP1_PubEle_Grupo4

<b>Grupo 4:</b>
<p>Carla Rodrigues, A84710</p>
<p>Cláudia Palma, A85401</p>
<p>Eduarda Ribeiro, A8541</p>

<b>A construção deste trabalho assenta nas seguintes fases:</b>

  1.	Em primeiro lugar criamos um ficheiro XML, denominado <b>Portfolio.xml</b> que contém vários Relatórios.
 
  2.	Criamos dois templates HTML (um para o Relatório, denomiando <b>report_template</b>, e outro para o Portfolio, denominado <b>index_template</b>) que, foram adicionados ao         ficheiro <b>portfolio_to_html.py</b>.

  3.	Também no ficheiro <b>portfolio_to_html.py</b>, criamos um conjunto de funções em Python que permitem preencher os dois templates HTML criados (report_template e                   index_template) com informação do ficheiro <b>Portfolio.xml</b>. Foi também necessária a criação do ficheiro <b>report.dtd</b> que é chamado numa das funções python do             ficheiro portfolio_to_html.py.

  4.	Para testar, corremos o ficheiro <b>portfolio_to_html.py</b> no terminal da seguinte forma: <b>python3 portfolio_to_html.py</b>.

  5.	Neste caso, foram gerados 4 ficheiros HTML (<b>report1.html</b>, <b>report2.html</b>, <b>report3.html</b>, <b>report4.html</b>) correspondentes aos 4 relatórios que se             encontravam no nosso ficheiro <b>Portfolio.xml</b>.

  6.	Para além dos 4 ficheiros mencionados no ponto anterior, é gerado um outro ficheiro HTML denominado <b>index.html</b>, correspondente ao index_template (template do               Portfolio). Nesse ficheiro, index.html, encontra-se:
        - a identificação do grupo de trabalho;
        - a identificação dos docentes;
        - um índice dos vários Relatórios criados dentro do ficheiro Portfolio.xml: três deles a título de exemplo, com base em relatórios de outra cadeira do nosso curso e outro           correspondente a um breve relatório do trabalho em questão, onde é explicado com maior detalhe a elaboração de cada um dos ficheiros aqui mencionados, nomeadamente as             funções Python criadas;
        - um índice temático de hashtags;
        - todos os ficheiros criados neste trabalho, nomeadamente o código python criado. 
