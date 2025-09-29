# 🎲 Dice & Drinks - Bar de Jogos de Tabuleiro

Site web completo para um bar de jogos de tabuleiro desenvolvido com HTML, CSS e Python.

## 📁 Estrutura do Projeto

```
Trabalho web parte 1/
├── index.html                    # Página inicial
├── styles.css                    # Estilos CSS
├── gerar_site.py                 # Script Python para gerar cardápios
├── README.md                     # Este arquivo
├── data/                         # Dados em formato JSON
│   ├── alimentos_bebidas.json    # Cardápio de comidas e bebidas
│   └── jogos.json               # Biblioteca de jogos
├── templates/                    # Templates HTML
│   ├── cardapio-comida-template.html
│   └── cardapio-jogos-template.html
├── images/                       # Imagens do site (criar manualmente)
└── videos/                       # Vídeos do site (criar manualmente)
```

## 🚀 Como Usar

### 1. Executar o Script Python

Para gerar automaticamente os cardápios a partir dos dados JSON:

```bash
# Opção 1: Especificar o diretório de dados
python gerar_site.py --dados data

# Opção 2: Executar sem argumentos (será solicitado o caminho)
python gerar_site.py
```

### 2. Atualizar Dados

Para adicionar novos itens ao cardápio ou jogos:

1. Edite os arquivos JSON em `data/`:
   - `alimentos_bebidas.json` - Para comidas e bebidas
   - `jogos.json` - Para jogos de tabuleiro

2. Execute o script Python novamente:
   ```bash
   python gerar_site.py --dados data
   ```

### 3. Visualizar o Site

Abra o arquivo `index.html` em um navegador web para ver o site completo.

## 📋 Funcionalidades

### ✅ Página Inicial
- Apresentação do bar com fotos e vídeos
- Seção "Sobre" com informações do estabelecimento
- Destaques dos diferenciais do bar
- Navegação para outras seções

### ✅ Cardápio de Comidas e Bebidas
- **Gerado automaticamente** a partir de `data/alimentos_bebidas.json`
- Organizado por categorias (Entradas, Pratos Principais, Bebidas, Sobremesas)
- Cada item inclui: nome, preço, descrição, ingredientes e foto
- Design responsivo e moderno

### ✅ Cardápio de Jogos
- **Gerado automaticamente** a partir de `data/jogos.json`
- Organizado por categorias (Clássicos, Modernos, Partida Rápida, etc.)
- Cada jogo inclui: nome, tipo, número de jogadores, descrição e detalhes
- Interface intuitiva para navegação

### ✅ Script Python
- Gera automaticamente as páginas HTML dos cardápios
- Suporte a linha de comando com argumentos
- Validação de dados e tratamento de erros
- Interface interativa quando não há argumentos

## 🎨 Design

- **Responsivo**: Funciona em desktop, tablet e mobile
- **Moderno**: Design limpo e profissional
- **Acessível**: Navegação intuitiva e clara
- **Temático**: Visual adequado para um bar de jogos

## 📝 Formato dos Dados

### Alimentos e Bebidas (alimentos_bebidas.json)
```json
{
  "categorias": [
    {
      "nome": "Nome da Categoria",
      "itens": [
        {
          "nome": "Nome do Item",
          "preco": "R$ XX,XX",
          "descricao": "Descrição do item",
          "ingredientes": "Lista de ingredientes",
          "imagem": "caminho/para/imagem.jpg"
        }
      ]
    }
  ]
}
```

### Jogos (jogos.json)
```json
{
  "categorias": [
    {
      "nome": "Nome da Categoria",
      "jogos": [
        {
          "nome": "Nome do Jogo",
          "tipo": "Tipo do Jogo",
          "jogadores": "X",
          "tempo": "XX min",
          "descricao": "Descrição do jogo",
          "detalhes": "Detalhes adicionais",
          "imagem": "caminho/para/imagem.jpg"
        }
      ]
    }
  ]
}
```

## 🔧 Requisitos

- Python 3.6+ (para executar o script)
- Navegador web moderno
- Editor de texto (para modificar os dados JSON)

## 📸 Imagens Necessárias

Para o funcionamento completo, adicione as seguintes imagens na pasta `images/`:

### Página Inicial
- `bar-hero.jpg` - Imagem de fundo da seção hero
- `bar-poster.jpg` - Poster do vídeo
- `bar-interior1.jpg` - Interior do bar
- `bar-interior2.jpg` - Mesas de jogos

### Cardápio de Comidas
- `nachos.jpg`, `wings.jpg`, `bruschetta.jpg`
- `hamburguer.jpg`, `pizza.jpg`, `carbonara.jpg`, `caesar.jpg`
- `cerveja-ipa.jpg`, `coquetel-d20.jpg`, `refrigerante.jpg`, `suco-natural.jpg`
- `brownie.jpg`, `tiramisu.jpg`

### Cardápio de Jogos
- `xadrez.jpg`, `damas.jpg`, `monopoly.jpg`
- `catan.jpg`, `ticket-to-ride.jpg`, `wingspan.jpg`
- `sushi-go.jpg`, `love-letter.jpg`, `splendor.jpg`
- `pandemic.jpg`, `forbidden-island.jpg`
- `dnd.jpg`, `call-of-cthulhu.jpg`

## 🎯 Características Técnicas

- **HTML5 semântico**: Estrutura clara e acessível
- **CSS3 moderno**: Flexbox, Grid, animações e responsividade
- **Python puro**: Sem dependências externas além da biblioteca padrão
- **JSON**: Formato de dados simples e legível
- **Templates**: Sistema de templates para reutilização de código

## 📞 Suporte

Para dúvidas ou problemas:
- Verifique se o Python está instalado corretamente
- Confirme se os arquivos JSON estão no formato correto
- Certifique-se de que todas as imagens estão na pasta `images/`

---

**Desenvolvido para o Trabalho Web Parte 1**  
*Site completo e funcional para bar de jogos de tabuleiro*
