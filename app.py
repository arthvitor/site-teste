from flask import Flask

app = Flask(__name__)

menu = '''
<a href="/">Pagina Inicial</a> | <a href="/sobre">Sobre</a> | <a href="/contato">Contato</a> | <a href="/teste">Teste</a>
<br>
'''

@app.route("/")
def index():
   return menu + "Meu nome é Vitor. Muito prazer"

@app.route("/sobre")
def sobre():
   return menu + "Aqui vai o conteúdo da página Sobre"

@app.route("/contato")
def contato():
   return menu + "Aqui vai o conteúdo da página Contato"

@app.route("/teste")
def ultimas_promocoes():
  scraper = ChannelScraper()
  contador = 0
  resultado = []
  for message in scraper.messages("promocoeseachadinhos"):
    contador += 1
    texto = message.text.strip().splitlines()[0]
    resultado.append(f"{message.created_at} {texto}")
    if contador == 10:
      return menu + resultado
   
