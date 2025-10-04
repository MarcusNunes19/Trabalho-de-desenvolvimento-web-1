import json
import os
import sys

def carregar_dados(arquivo_json):
    """Carrega dados do arquivo JSON com tratamento de erros"""
    try:
        with open(arquivo_json, 'r', encoding='utf-8') as f:
            dados = json.load(f)
            print(f"Dados carregados: {len(dados.get('categorias', []))} categorias encontradas")
            return dados
    except FileNotFoundError:
        print(f"Erro: Arquivo '{arquivo_json}' não encontrado.")
        return None
    except json.JSONDecodeError as e:
        print(f"Erro: JSON inválido no arquivo '{arquivo_json}': {e}")
        return None
    except Exception as e:
        print(f"Erro inesperado ao carregar '{arquivo_json}': {e}")
        return None

def detectar_tipo_dados(dados):
    """Detecta se os dados são de cardápio ou jogos"""
    if not dados or 'categorias' not in dados:
        return 'desconhecido'
    
    primeira_categoria = dados['categorias'][0] if dados['categorias'] else {}
    
    # Verifica se é catálogo de jogos
    if 'jogos' in primeira_categoria:
        return 'jogos'
    # Verifica se é cardápio de comida
    elif 'itens' in primeira_categoria:
        return 'cardapio'
    else:
        return 'desconhecido'

def gerar_html_categoria_cardapio(categoria):
    """Gera HTML para uma categoria do cardápio"""
    nome_categoria = categoria["nome"]
    itens = categoria["itens"]
    
    html = f'<div class="cardapio-category">\n<h2>{nome_categoria}</h2>\n'
    
    # Adiciona observação se existir
    if 'observacao' in categoria:
        html += f'<p class="category-obs">{categoria["observacao"]}</p>\n'
    
    html += '<div class="cardapio-grid">\n'
    
    for item in itens:
        html += f"""
        <div class="cardapio-opcoes">
            <div class="cardapio-opcoes-content">
                <h3>{item['nome']}</h3>
                <div class="cardapio-opcoes-image">
                    <img src="{item['imagem']}" alt="{item['nome']}" loading="lazy">
                </div>
                <p class="cardapio-opcoes-description">{item['descricao']}</p>
                <p class="cardapio-opcoes-ingredients">{item['ingredientes']}</p>
                <p class="cardapio-opcoes-price">{item['preco']}</p>
            </div>
        </div>
        """
    
    html += "</div>\n</div>\n"
    return html

def gerar_html_categoria_jogos(categoria):
    """Gera HTML para uma categoria de jogos"""
    nome_categoria = categoria["nome"]
    jogos = categoria["jogos"]
    
    html = f'<div class="jogos-category">\n<h2>{nome_categoria}</h2>\n'
    html += '<div class="jogos-grid">\n'
    
    for jogo in jogos:
        html += f"""
        <div class="jogo-item">
            <div class="jogo-image">
                <img src="{jogo['imagem']}" alt="{jogo['nome']}" loading="lazy">
            </div>
            <div class="jogo-content">
                <h3>{jogo['nome']}</h3>
                <div class="jogo-info">
                    <span class="jogo-tipo">{jogo['tipo']}</span>
                    <span class="jogo-jogadores">Jogadores: {jogo['jogadores']}</span>
                    <span class="jogo-tempo">Tempo: {jogo['tempo']}</span>
                </div>
                <p class="jogo-descricao">{jogo['descricao']}</p>
                <p class="jogo-detalhes">{jogo['detalhes']}</p>
            </div>
        </div>
        """
    
    html += "</div>\n</div>\n"
    return html

def obter_arquivo_entrada():
    """Obtém o arquivo/diretório de entrada do usuário com validação"""
    while True:
        # Verifica se foi passado por linha de comando
        if len(sys.argv) > 1:
            entrada = sys.argv[1]
            print(f"Arquivo/diretório informado: {entrada}")
        else:
            # Prompt interativo
            entrada = input("\nDigite o caminho do arquivo JSON (ex: json/cardapio_comida.json): ").strip()
        
        # Verifica se é um arquivo JSON
        if os.path.isfile(entrada) and entrada.endswith('.json'):
            if os.path.exists(entrada):
                return entrada
            else:
                print("Arquivo não encontrado.")
        
        # Verifica se é um diretório
        elif os.path.isdir(entrada):
            arquivos_json = [f for f in os.listdir(entrada) if f.endswith('.json')]
            if arquivos_json:
                print("\nArquivos JSON encontrados no diretório:")
                for i, arquivo in enumerate(arquivos_json, 1):
                    print(f"   {i}. {arquivo}")
                
                try:
                    escolha = int(input(f"\nEscolha o número do arquivo (1-{len(arquivos_json)}): ")) - 1
                    if 0 <= escolha < len(arquivos_json):
                        caminho_completo = os.path.join(entrada, arquivos_json[escolha])
                        return caminho_completo
                    else:
                        print("Número fora do intervalo válido.")
                except ValueError:
                    print("Por favor, digite um número válido.")
            else:
                print("Nenhum arquivo JSON encontrado no diretório.")
        else:
            print("Entrada inválida. Digite um arquivo JSON ou diretório existente.")

def determinar_arquivo_saida(arquivo_entrada, tipo_dados):
    """Determina o nome do arquivo de saída baseado no arquivo de entrada e tipo de dados"""
    nome_arquivo = os.path.basename(arquivo_entrada).lower()
    
    if tipo_dados == 'jogos':
        return 'catalogo-jogos.html', 'Catálogo de Jogos - Pará e Paraná Bar'
    elif tipo_dados == 'cardapio':
        # CORREÇÃO: Agora procura por "tipica" ou "típica" no nome do arquivo
        if 'tipica' in nome_arquivo or 'típica' in nome_arquivo:
            return 'cardapio-tipicas.html', 'Cardápio Típicas - Pará e Paraná Bar'
        else:
            return 'cardapio-comida.html', 'Cardápio - Pará e Paraná Bar'
    else:
        # Para arquivos genéricos, pergunta ao usuário
        nome_saida = input("Digite o nome do arquivo de saída (ex: cardapio.html): ").strip()
        if not nome_saida.endswith('.html'):
            nome_saida += '.html'
        titulo = input("Digite o título da página: ").strip()
        return nome_saida, titulo

def selecionar_template(tipo_dados, arquivo_entrada):
    """Seleciona o template apropriado baseado no tipo de dados"""
    nome_arquivo = os.path.basename(arquivo_entrada).lower()
    
    if tipo_dados == 'jogos':
        return os.path.join('Exemplos', 'jogos.html')
    elif tipo_dados == 'cardapio':
        # CORREÇÃO: Usa comida_tipica.html para cardápios típicos
        if 'tipica' in nome_arquivo or 'típica' in nome_arquivo:
            return os.path.join('Exemplos', 'comida_tipica.html')
        else:
            return os.path.join('Exemplos', 'comida.html')
    else:
        return os.path.join('Exemplos', 'comida.html')

def gerar_conteudo(dados, tipo_dados):
    """Gera o conteúdo HTML baseado no tipo de dados"""
    print(f"\nGerando conteúdo para {tipo_dados}...")
    
    conteudo = ""
    for categoria in dados.get("categorias", []):
        if tipo_dados == 'jogos':
            conteudo += gerar_html_categoria_jogos(categoria)
        else:  # cardapio
            conteudo += gerar_html_categoria_cardapio(categoria)
    
    return conteudo

def obter_marcador_template(tipo_dados):
    """Retorna o marcador correto para substituição no template"""
    if tipo_dados == 'jogos':
        return '{{JOGOS_CONTENT}}'
    else:  # cardapio
        return '{{MENU_CONTENT}}'

def main():
    """Função principal"""
    print("=" * 50)
    print("    GERADOR DE CARDÁPIOS E JOGOS - PARÁ E PARANÁ BAR")
    print("=" * 50)
    
    # Obter arquivo de entrada
    arquivo_entrada = obter_arquivo_entrada()
    
    # Carregar dados
    dados = carregar_dados(arquivo_entrada)
    if dados is None:
        print("Não foi possível carregar os dados. Encerrando.")
        return
    
    # Detectar tipo de dados
    tipo_dados = detectar_tipo_dados(dados)
    print(f"Tipo de dados detectado: {tipo_dados}")
    
    if tipo_dados == 'desconhecido':
        print("Não foi possível determinar o tipo de dados. Verifique a estrutura do JSON.")
        return
    
    # Determinar arquivo de saída
    arquivo_saida, titulo_pagina = determinar_arquivo_saida(arquivo_entrada, tipo_dados)
    
    # Selecionar template
    template_file = selecionar_template(tipo_dados, arquivo_entrada)
    
    if not os.path.exists(template_file):
        print(f"Template não encontrado: {template_file}")
        return
    
    # Carregar template
    try:
        with open(template_file, "r", encoding="utf-8") as f:
            template = f.read()
    except Exception as e:
        print(f"Erro ao carregar template: {e}")
        return
    
    # Gerar conteúdo
    conteudo = gerar_conteudo(dados, tipo_dados)
    
    # Obter marcador correto
    marcador = obter_marcador_template(tipo_dados)
    
    # Substituir no template
    html_final = template.replace(marcador, conteudo)
    
    # Salvar arquivo NA PASTA RAIZ (Trabalho-de-desenvolvimento-web-1)
    try:
        with open(arquivo_saida, "w", encoding="utf-8") as f:
            f.write(html_final)
        
        print(f"\nPágina gerada com sucesso: {arquivo_saida}")
        print(f"Local: Pasta raiz (Trabalho-de-desenvolvimento-web-1)")
        print(f"Estatísticas:")
        print(f"   - Categorias: {len(dados.get('categorias', []))}")
        
        if tipo_dados == 'jogos':
            total_itens = sum(len(cat['jogos']) for cat in dados.get('categorias', []))
            print(f"   - Jogos totais: {total_itens}")
        else:
            total_itens = sum(len(cat['itens']) for cat in dados.get('categorias', []))
            print(f"   - Itens totais: {total_itens}")
        
    except Exception as e:
        print(f"Erro ao salvar arquivo: {e}")

if __name__ == "__main__":
    main()