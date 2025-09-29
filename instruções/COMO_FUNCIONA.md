# 🎯 Como o Sistema Funciona - Josiel Bar

## 📋 **Estrutura do Projeto (Conforme Regras do Trabalho)**

### **1. Arquivos Estáticos (Não Gerados Automaticamente)**
- **`index.html`** - Página inicial estática
- **`styles.css`** - Estilos CSS para todo o site
- **`images/`** - Pasta com todas as imagens

### **2. Arquivos Gerados Automaticamente pelo Python**
- **`cardapio-comida.html`** - Gerado a partir de `data/alimentos_bebidas.json`
- **`cardapio-jogos.html`** - Gerado a partir de `data/jogos.json`

### **3. Script Python**
- **`gerar_site.py`** - Script que gera as páginas automaticamente
- **`templates/`** - Templates HTML para as páginas geradas

### **4. Dados de Entrada**
- **`data/alimentos_bebidas.json`** - Dados do cardápio de comida
- **`data/jogos.json`** - Dados do cardápio de jogos

## 🔧 **Como Atualizar o Site**

### **Passo 1: Editar os Dados**
1. Abra `data/alimentos_bebidas.json` ou `data/jogos.json`
2. Modifique os dados (adicionar/remover itens, preços, etc.)
3. Salve o arquivo

### **Passo 2: Executar o Script Python**
```bash
# Opção 1: Com argumento
python gerar_site.py --dados data

# Opção 2: Sem argumento (o script pedirá o diretório)
python gerar_site.py
```

### **Passo 3: Verificar Resultado**
- As páginas `cardapio-comida.html` e `cardapio-jogos.html` serão atualizadas automaticamente
- Abra no navegador para ver as mudanças

## ⚠️ **Importante - Regras do Trabalho**

### **✅ O que DEVE ser feito:**
- **Cardápios gerados automaticamente** pelo script Python
- **Dados em arquivos JSON** (não HTML)
- **Script com argumentos de linha de comando**
- **Templates HTML** com delimitadores
- **Validação de entrada** do usuário

### **❌ O que NÃO deve ser feito:**
- **Editar manualmente** `cardapio-comida.html` ou `cardapio-jogos.html`
- **Usar pacotes** que automatizem HTML/CSS
- **Gerar todo o site** automaticamente (apenas os cardápios)

## 🚨 **Problema Atual**

**Python não está instalado** no sistema, então o script não pode ser executado automaticamente.

### **Soluções:**
1. **Instalar Python** de https://python.org
2. **Usar o script** para gerar as páginas automaticamente
3. **Seguir as regras** do trabalho corretamente

## 📝 **Estrutura Correta dos Dados**

### **`data/alimentos_bebidas.json`:**
```json
{
  "categorias": [
    {
      "nome": "Entradas",
      "itens": [
        {
          "nome": "Batata Frita",
          "preco": "R$ 15,90",
          "descricao": "Porção de batata frita crocante",
          "ingredientes": "Batata, óleo, sal",
          "imagem": "images/batata-frita.jpg"
        }
      ]
    }
  ]
}
```

### **`data/jogos.json`:**
```json
{
  "categorias": [
    {
      "nome": "Jogos de Estratégia",
      "itens": [
        {
          "nome": "Catan",
          "descricao": "Jogo de colonização e comércio",
          "tipo": "Estratégia",
          "jogadores": "3-4",
          "tempo": "60-90 min",
          "imagem": "images/tab.jpg"
        }
      ]
    }
  ]
}
```

## 🎯 **Resumo**

O sistema está **correto** e segue as regras do trabalho:
- ✅ **Script Python** gera cardápios automaticamente
- ✅ **Dados em JSON** (não HTML)
- ✅ **Templates** com delimitadores
- ✅ **Argumentos de linha de comando**
- ✅ **Validação de entrada**

**Para usar:** Instale Python e execute `python gerar_site.py --dados data`
