# main.py - Arquivo PRINCIPAL que você executa

# 1. Importa o helper
from importador import importar_classe

# 2. Carrega as classes usando o helper
Produto = importar_classe("Produto", "Produto")
Item = importar_classe("Item", "Item")

#Produto.cadastrar_produto()
#Produto.listar_produtos()
Item.novo_item()
Item.mostrar_lista_atual()