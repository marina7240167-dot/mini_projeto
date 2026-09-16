import unittest

from app import app, moeda, produtos


class VesteBemTests(unittest.TestCase):
    def setUp(self):
        app.config["TESTING"] = True
        self.client = app.test_client()

    def test_paginas_principais(self):
        for rota in ["/", "/catalogo", "/ofertas", "/sobre"]:
            resposta = self.client.get(rota)
            self.assertEqual(resposta.status_code, 200)
            self.assertIn("VesteBem", resposta.get_data(as_text=True))

    def test_catalogo_usa_lista_de_produtos(self):
        pagina = self.client.get("/catalogo").get_data(as_text=True)
        for produto in produtos:
            self.assertIn(produto["nome"], pagina)

    def test_moeda(self):
        self.assertEqual(moeda(5990), "R$ 59,90")

    def test_404(self):
        self.assertEqual(self.client.get("/nao-existe").status_code, 404)


if __name__ == "__main__":
    unittest.main()
