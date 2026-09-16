from flask import Flask, render_template

app = Flask(__name__)

products = [
    {"name": "Camisa Aurora", "category": "Camisas", "price": "R$ 89,90", "description": "Algodao leve com corte confortavel para todos os dias.", "badge": "Mais vendida", "color": "#d86f52"},
    {"name": "Calca Horizonte", "category": "Calcas", "price": "R$ 159,90", "description": "Jeans azul profundo com cintura media e caimento reto.", "badge": "Novo", "color": "#426b76"},
    {"name": "Vestido Brisa", "category": "Vestidos", "price": "R$ 129,90", "description": "Viscose estampada para deixar os dias mais leves.", "badge": "Destaque", "color": "#e0a458"},
    {"name": "Moletom Norte", "category": "Casacos", "price": "R$ 189,90", "description": "Moletom macio, amplo e pronto para acompanhar o frio.", "badge": "Ultimas unidades", "color": "#66735f"},
]


@app.route("/")
def home():
    return render_template("home.html", featured_products=products[:3])


@app.route("/catalogo")
def catalogo():
    categories = ["Todos", "Camisas", "Calcas", "Vestidos", "Casacos"]
    return render_template("catalogo.html", products=products, categories=categories)


@app.route("/sobre")
def sobre():
    values = [
        {"title": "Escolhas conscientes", "text": "Priorizamos pecas versateis e materiais que duram mais."},
        {"title": "Estilo real", "text": "Roupas para a rotina, sem complicar o que deve ser simples."},
        {"title": "Feito perto", "text": "Trabalhamos com pequenos fornecedores e producao local."},
    ]
    return render_template("sobre.html", values=values)


if __name__ == "__main__":
    app.run(debug=True)
