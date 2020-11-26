from bs4 import BeautifulSoup as bs
from re import *
import jinja2  as j2


# Função que preenche o template html de um report com o conteúdo extraído do ficheiro xml respetivo (Portfolio.xml)

def report_template(info):
	
	t = j2.Template("""
<html>
   <head>
    	<meta charset=UTF-8"/>
    	<title>{{theme}}</title>
    	<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bootswatch/4.5.3/yeti/bootstrap.min.css">
    	<style>
			body{
            	text-align:justify;
            	margin-right:100px;
            	margin-left:100px;
        	}     
        </style>
    </head>

    <body style="font-family:Times New Roman">
    	<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bootswatch/4.5.3/yeti/bootstrap.min.css">
        <style>
            body{
                text-align:justify;
                margin-right:100px;
                margin-left:100px;
            }    
        </style>

    	<br>
    	
        <h1 align="center"><b>{{theme}}</b></h1>
        <hr align="center" width="70%">
        <h3 align="center">{{affiliation}}</h3>
        <br>
        <center><img src="https://facs2017.di.uminho.pt/sites/default/files/logo_UMEENG_sem_nome.jpg" with=110 height=80></center>
        <br>
        <h3 align="center">{{subject}}</h3>
        <br>
        <h4 align="center">{{date}}</h4>
        <hr/>

        <style>
			div.a {
  			text-indent: 25px;
			}	
      	</style>

      	<style>
    		.heading { color: #E24700; }
  		</style>

        <ul><h4><b>Autores</b></h4><ul>
            {% for el in team  %}
            <li>{{el['name']}} : {{el['number']}}</li>
            {% endfor %}
        </ul></ul>
        <hr/>
        <br>

        <ol><h2>Índice</h2><ol>
        	{% for section in body  %}
	        <li><a class="heading" href="#{{section['title']}}">{{section['title']}}</a></li>
	        {% endfor %}
	    </ol></ol>

		<ol>
	       	{% for section in body  %}
	        <h2 id="{{section['title']}}"> {{section['title']}}</h2>
		    <div class="a"><p>{{section['text']}}</p></div>
	       	{% endfor %}
	    </ol>

	    <br>

	    {% if image  %}
	    <center><img src={{image}} with=550 height=500></center>
	    {% endif %}

	    <br>
	    <br>

		<ol><h2>Referências Bibliográficas</h2><ol>
		   	<p>{% for bibitem in bibliography  %}
			<li> {{bibitem['author']}} . {{bibitem['description']}} 
		    </li></p>
		    {% endfor %}
		</ol></ol>
		
    </body>
</html>

""")
	return (t.render(info))

# Função que preenche o template html do index com o conteúdo extraído do ficheiro xml respetivo (Portfolio.xml)

def index_template(info):
	
	t2 = j2.Template("""
<html>
   <head>
    	<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    	<title>Portfolio</title>
    	<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bootswatch/4.5.3/yeti/bootstrap.min.css">

    </head>
    
 	<body>
 		<style>
			body{
            	text-align:justify;
            	margin-right:100px;
            	margin-left:100px;
        	}     
        </style>

        <style>
	      	#header{
	          background-color:#DCDCDC;
	          color:black;
	          text-align:center;
	          padding:7px;
	      	}
	    </style>
        
        <br>

	    <h1 align="center"><b>Portfolio</b></h1>
	    <hr align="center" width="50%">
	    <h3 align="center">Universidade do Minho</h3>
	    <br>
	    <center><img src="https://facs2017.di.uminho.pt/sites/default/files/logo_UMEENG_sem_nome.jpg" with=110 height=80></center>
	    <br>
	    <h3 align="center">Mestrado Integrado em Engenharia Biomédica</h3>
	    <hr align="center" width="80%">

		<br>

		<div id="header">
    		<h2><b>Grupo 4</b></h2>
		</div>

		<style>
		  .heading { color: #E24700; }
		</style>

		<br>

		<ul>
		   <li><b> Nome: </b>Carla Maria Pinto Rodrigues<br><br><b> E-mail: </b><a class="heading" href="mailto:a84710@alunos.uminho.pt">a84710@alunos.uminho.pt</a><br><br><b> Número de aluno: </b>84710<br><br></li>
		   <li><b> Nome: </b>Cláudia Patrícia Ribeiro Palma<br><br><b> E-mail: </b><a class="heading" href="mailto:a85401@alunos.uminho.pt">a85401@alunos.uminho.pt</a><br><br><b> Número de aluno: </b>85401<br><br></li>
		   <li><b> Nome: </b>Eduarda Maria Lopes Ribeiro<br><br><b> E-mail: </b><a class="heading" href="mailto:a85412@alunos.uminho.pt">a85412@alunos.uminho.pt</a><br><br><b> Número de aluno: </b>85412<br><br></li>
		</ul>
		
		<div id="header">
    		<h2><b>Docentes</b></h2>
		</div>

		<br>

		<ul>
		   <p>José João Antunes Guimarães Dias Almeida</p>
		   <p>Pedro Rafael Paiva Moura</p>
		</ul>

    	<div id="header">
    		<h2><b>Índice</b></h2>
    	</div>

    	<br>

    	<ul>
    		{% for t in theme %}
	    	<p><a class="heading" href="report{{theme.index(t)+1}}.html" title="Ir para {{t}}" target="_blank">{{t}}</a></p>
	    	{% endfor %}
    	</ul>

    	<div id="header">
    		<h2><b>Índice Temático</b></h2>
    	</div>

    	<br>

		<ul>
			{% for t in hashtag %}
			<p><a class="heading" href="report{{hashtag.index(t)+1}}.html" title="Ir para {{t}}" target="_blank">{{t}}</a></p>
			{% endfor %}
    	</ul>

    	<br>

    	<div id="header">
    		<h2><b>Ficheiros</b></h2>
    	</div>

    	<br>

    	<ul>
			<p><a class="heading" href="Portfolio.xml">Portfolio XML</a></p>
 			<p><a class="heading" href="portfolio_to_html.py">Conversor XML para HTML em Python</a></p>
			<p><a class="heading" href="report.dtd">Portfolio DTD</a></p>
		</ul>

    	<br>


   	</body>
   	
</html>
""")
	return (t2.render(info))


def dtd(): # Função que extrai as tags do ficheiro report.dtd para uma lista
	
	with open("report.dtd") as f:
		content = f.read()
	l=[]
	for tag in findall('<!ELEMENT +(\w+)', content):
		l.append(tag)
	return l


def extract_report(): # Cria uma lista, em que cada elemento da lista é um report do Portfolio.xml

	with open("Portfolio.xml") as f:
		reports=f.read()

	Bs_reports = bs(reports, "xml")
	b_report = Bs_reports.find_all('report')

	return b_report


def extract_list(xml,tag): # Recebe uma tag "pai" do xml, e cria uma lista com o conteudo da tag "filha" 

	info = []

	for miolo in findall(rf'<{tag}>((?:.|\n)*?)</{tag}>',xml):
		info.append(miolo)

	return info


def extract_dict(l,report): # Recebe uma lista com as tags e o report/excerto report, e devolve dicionário com {tag:conteudo correspondente}

	info = {}
	for elem in l:
		v=search(rf"<{elem}>((?:.|\n)*?)</{elem}>",report)
		if v:
			info[elem]=v[1]

	return info


def extract_theme(report): # extrai o conteudo da tag theme
	
	lt= bs(report,"xml")
	for el in lt.find_all("theme"):
		return el.text


def extract_hashtags(report): # extrai o conteudo da tag hastag
	
	bs_hashtags = bs(report, "xml") 
	for el in bs_hashtags.find_all("hashtag"):
		return el.text


def main():
	
	lista_reports= extract_report()

	lista=dtd()

	i=1

	t={'theme':[],'hashtag':[]}

	for report in lista_reports:
		report=str(report)

		dic = extract_dict(lista,report)
		aux = extract_list(dic['team'],'element')
		dic['team'] = [extract_dict(['name','number'],el) for el in aux]

		aux1= extract_list(dic['body'],'section')
		dic['body'] = [extract_dict(['title','text','image'],el) for el in aux1]

		aux2= extract_list(dic['bibliography'],'bibitem')
		dic['bibliography'] = [extract_dict(['description','author'],el) for el in aux2]

		t['theme'].append(extract_theme(report))
		t['hashtag'].append(extract_hashtags(report))

		with open(f'report{i}.html', 'w') as f:
			f.write(report_template(dic))
			i+=1

		with open(f'index.html','w') as ind:
			ind.write(index_template(t))
main()