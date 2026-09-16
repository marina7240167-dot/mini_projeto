# VesteBem

Loja de roupas fictícia desenvolvida com Flask, Jinja2 e Bootstrap para o mini-projeto.

## Tecnologias

- Flask para as rotas;
- Jinja2 com herança de templates, `for` e `if`;
- Bootstrap com navbar, grid e cards.

## Páginas

- `/` — início e produtos em destaque;
- `/catalogo` — todos os produtos;
- `/ofertas` — produtos em promoção;
- `/sobre` — apresentação da loja.

## Como executar

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe app.py
```

Abra `http://127.0.0.1:5000` no navegador. Produtos, preços e disponibilidade são fictícios.
