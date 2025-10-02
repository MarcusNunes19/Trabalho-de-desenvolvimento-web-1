import json
import os

# -------------------------
# Funções utilitárias
# -------------------------

def ler_json(arquivo):
    """Lê um arquivo JSON e retorna os dados"""
    with open(arquivo, 'r', encoding='utf-8') as f:
        return json.load(f)

def salvar_html(template_path, saida_path, conteudo):
    """Substitui o placeholder {{CONTEUDO}} no HTML e salva"""
    with open(template_path, 'r', encoding='utf-8') as f:
        html = f.read()

    html = html.replace("{{CONTEUDO}}", conteudo)

    with open(saida_path, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f"✅ Página gerada: {saida_path}")

# -------------------------
# Geradores de HTML
# -------------------------

def gerar_cardapio_comida(dados):
    """Gera HTML para comidas/bebidas/sobremesas"""
    html = ""
    for cat in dados['categorias']:
        html += f'<div class="cardapio-category">\n'
        html += f'  <h2>{cat["nome"]}'
        if "observacao" in cat:
            html += f' ({cat["observacao"]})'
        html += '</h2>\n'
        html += '  <div class="cardapio-grid">\n'

        for item in cat['itens']:
            html += f'''
    <div class="cardapio-opcoes">
        <div class="cardapio-opcoes-content">
            <h3>{item["nome"]}</h3>
            <div class="cardapio-opcoes-image">
                <img src="{item["imagem"]}" alt="{item["nome"]}">
            </div>
            <p class="cardapio-opcoes-description">{item["descricao"]}</p>
            <p class="cardapio-opcoes-ingredients">{item["ingredientes"]}</p>
            <p class="cardapio-opcoes-price">{item["preco"]}</p>
        </div>
    </div>
            '''
        html += '  </div>\n</div>\n'
    return html


def gerar_cardapio_tipicos(dados):
    """Gera HTML para comidas típicas"""
    html = '<div class="tipicos">\n'
    for item in dados['itens']:
        html += f'''
    <div class="tipico-item">
        <h3>{item["nome"]}</h3>
        <img src="{item["imagem"]}" alt="{item["nome"]}">
        <p>{item["descricao"]}</p>
        <p><b>Ingredientes:</b> {item["ingredientes"]}</p>
        <p><b>Preço:</b> {item["preco"]}</p>
    </div>
        '''
    html += '</div>\n'
    return html


def gerar_jogos(dados):
    """Gera HTML para jogos de tabuleiro"""
    html = '<div class="jogos">\n'
    for jogo in dados['jogos']:
        html += f'''
    <div class="jogo-item">
        <h3>{jogo["nome"]}</h3>
        <img src="{jogo["imagem"]}" alt="{jogo["nome"]}">
        <p>{jogo["descricao"]}</p>
        <p><b>Estilo:</b> {jogo["estilo"]}</p>
        <p><b>Jogadores:</b> {jogo["jogadores"]}</p>
    </div>
        '''
    html += '</div>\n'
    return html

# -------------------------
# Main
# -------------------------

def main():
    pasta_json = "json"

    # Comida
    dados_comida = ler_json(os.path.join(pasta_json, "cardapio_comida.json"))
    html_comida = gerar_cardapio_comida(dados_comida)
    salvar_html("cardapio-comida.html", "cardapio-comida.html", html_comida)

    # Típicos
    dados_tipicos = ler_json(os.path.join(pasta_json, "cardapio_típicos.json"))
    html_tipicos = gerar_cardapio_tipicos(dados_tipicos)
    salvar_html("cardapio-tipicas.html", "cardapio-tipicas.html", html_tipicos)

    # Jogos
    dados_jogos = ler_json(os.path.join(pasta_json, "tabuleiros.json"))
    html_jogos = gerar_jogos(dados_jogos)
    salvar_html("catálogo-jogos.html", "catálogo-jogos.html", html_jogos)


if __name__ == "__main__":
    main()
