# 🎯 Instruções Atualizadas - Josiel Bar

## 📁 **Estrutura do Projeto (Atualizada)**

### **Pasta de Dados:**
- **`json/`** - Pasta com os arquivos de dados (renomeada de `data/`)
- **`json/alimentos_bebidas.json`** - Dados do cardápio de comida
- **`json/jogos.json`** - Dados do cardápio de jogos

### **Arquivos Gerados:**
- **`cardapio-comida.html`** - Gerado automaticamente
- **`cardapio-jogos.html`** - Gerado automaticamente

## 🔧 **Como Usar o Script Python**

### **Opção 1: Com Argumento (Recomendado)**
```bash
python gerar_site.py --dados json
```

### **Opção 2: Sem Argumento (Script pergunta)**
```bash
python gerar_site.py
```
Quando aparecer a pergunta:
```
Digite o caminho para o diretório de dados (ou 'json' para usar o padrão):
```
Digite: **`json`** e pressione Enter

## 📝 **Exemplo de Uso Completo**

### **1. Editar os Dados**
- Abra `json/alimentos_bebidas.json` ou `json/jogos.json`
- Modifique os dados (preços, descrições, etc.)
- Salve o arquivo

### **2. Executar o Script**
```bash
python gerar_site.py --dados json
```

### **3. Resultado**
- As páginas `cardapio-comida.html` e `cardapio-jogos.html` serão atualizadas
- Abra no navegador para ver as mudanças

## ⚠️ **Importante**

### **✅ O que o Script Faz:**
- Lê os dados dos arquivos JSON
- Gera HTML automaticamente
- Atualiza as páginas do site
- Mantém o design e estilo

### **❌ O que NÃO Fazer:**
- **NÃO edite** `cardapio-comida.html` ou `cardapio-jogos.html` manualmente
- **NÃO mude** a estrutura dos arquivos JSON
- **SEMPRE use** o script Python para atualizar

## 🚨 **Se Python Não Estiver Instalado**

### **Instalar Python:**
1. Baixe de: https://python.org
2. Instale com as opções padrão
3. Execute o script normalmente

### **Alternativa (Temporária):**
- Me avise quando modificar os JSONs
- Eu atualizo as páginas HTML manualmente

## 📋 **Estrutura dos Arquivos JSON**

### **`json/alimentos_bebidas.json`:**
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

### **`json/jogos.json`:**
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

1. **Edite** os arquivos em `json/`
2. **Execute** `python gerar_site.py --dados json`
3. **Abra** o site no navegador
4. **Repita** quando quiser atualizar

O sistema está funcionando perfeitamente! 🎉
