# 📋 Instruções de Uso - Script Python

## 🐍 Como Executar o Script

### Opção 1: Com argumento na linha de comando
```bash
python gerar_site.py --dados data
```

### Opção 2: Sem argumentos (interativo)
```bash
python gerar_site.py
```
O script irá perguntar o caminho dos dados.

### Opção 3: Especificando diretório diferente
```bash
python gerar_site.py --dados caminho/para/seus/dados
```

## 📁 Estrutura dos Arquivos de Dados

### alimentos_bebidas.json
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
          "imagem": "images/nome-da-imagem.jpg"
        }
      ]
    }
  ]
}
```

### jogos.json
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
          "imagem": "images/nome-da-imagem.jpg"
        }
      ]
    }
  ]
}
```

## 🔄 Como Atualizar o Site

1. **Edite os arquivos JSON** em `data/`:
   - Adicione novos itens ao cardápio
   - Modifique informações existentes
   - Remova itens desnecessários

2. **Execute o script novamente**:
   ```bash
   python gerar_site.py --dados data
   ```

3. **As páginas HTML serão atualizadas automaticamente**

## ⚠️ Solução de Problemas

### Erro: "Python não foi encontrado"
- Instale o Python 3.6+ do site oficial: https://python.org
- Certifique-se de que o Python está no PATH do sistema

### Erro: "Arquivo não encontrado"
- Verifique se os arquivos JSON existem em `data/`
- Confirme se o caminho está correto

### Erro: "JSON inválido"
- Verifique a sintaxe dos arquivos JSON
- Use um validador JSON online se necessário

### Páginas não são geradas
- Verifique se as pastas `templates/` existem
- Confirme se os templates HTML estão corretos

## 📝 Exemplo de Uso Completo

1. **Primeira execução**:
   ```bash
   python gerar_site.py --dados data
   ```
   Saída esperada:
   ```
   🎲 Gerador de Site - Dice & Drinks
   ========================================
   📁 Usando dados de: data
   📊 Carregando dados...
   🔨 Gerando cardápio de comidas e bebidas...
   🎮 Gerando cardápio de jogos...
   📄 Gerando páginas HTML...
   ✅ Página gerada: cardapio-comida.html
   ✅ Página gerada: cardapio-jogos.html
   
   🎉 Site gerado com sucesso!
   📋 Páginas criadas:
      • cardapio-comida.html
      • cardapio-jogos.html
   ```

2. **Após modificar os dados**:
   - Edite `data/alimentos_bebidas.json` ou `data/jogos.json`
   - Execute o script novamente
   - As páginas serão atualizadas automaticamente

## 🎯 Dicas Importantes

- **Sempre faça backup** dos arquivos JSON antes de fazer alterações
- **Teste o JSON** em um validador online antes de executar o script
- **Mantenha as imagens** na pasta `images/` com os nomes corretos
- **Execute o script** sempre que modificar os dados JSON

## 📞 Suporte

Se encontrar problemas:
1. Verifique se todos os arquivos estão no lugar correto
2. Confirme se o Python está instalado e funcionando
3. Teste os arquivos JSON em um validador online
4. Verifique se as imagens existem nas pastas corretas
