"""VesteBem: loja de roupas fictícia feita com Flask, Jinja2 e Bootstrap."""
from flask import Flask, render_template

app = Flask(__name__)

# Lista de dicionários: os cards do catálogo são criados automaticamente no template.
produtos = [
    {"id": 1, "nome": "Camiseta Essencial", "categoria": "Camisetas", "preco": 5990, "preco_anterior": None, "disponivel": True, "destaque": True, "cor": "Areia", "icone": "👕"},
    {"id": 2, "nome": "Calça Jeans Reta", "categoria": "Calças", "preco": 14990, "preco_anterior": 18990, "disponivel": True, "destaque": True, "cor": "Azul índigo", "icone": "👖"},
    {"id": 3, "nome": "Vestido Midi Solar", "categoria": "Vestidos", "preco": 17990, "preco_anterior": None, "disponivel": True, "destaque": True, "cor": "Amarelo", "icone": "👗"},
    {"id": 4, "nome": "Jaqueta Bomber", "categoria": "Casacos", "preco": 21990, "preco_anterior": 27990, "disponivel": True, "destaque": False, "cor": "Preto", "icone": "🧥"},
    {"id": 5, "nome": "Saia Plissada", "categoria": "Saias", "preco": 11990, "preco_anterior": None, "disponivel": True, "destaque": False, "cor": "Off-white", "icone": "👗"},
    {"id": 6, "nome": "Moletom Conforto", "categoria": "Casacos", "preco": 13990, "preco_anterior": 16990, "disponivel": False, "destaque": False, "cor": "Cinza", "icone": "🧥"},
]


@app.template_filter("moeda")
def moeda(centavos):
    inteiro, decimal = divmod(centavos, 100)
    return f"R$ {inteiro:,}".replace(",", ".") + f",{decimal:02d}"


def em_oferta(produto):
    return produto["disponivel"] and produto["preco_anterior"] is not None


@app.context_processor
def utilitarios_template():
    return {"em_oferta": em_oferta}


@app.route("/")
def inicio():
    destaques = [produto for produto in produtos if produto["destaque"]]
    return render_template("inicio.html", produtos=destaques)


@app.route("/catalogo")
def catalogo():
    return render_template("catalogo.html", produtos=produtos)


@app.route("/ofertas")
def ofertas():
    return render_template("ofertas.html", produtos=[produto for produto in produtos if em_oferta(produto)])


@app.route("/sobre")
def sobre():
    return render_template("sobre.html")


@app.errorhandler(404)
def pagina_nao_encontrada(erro):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(debug=True)
