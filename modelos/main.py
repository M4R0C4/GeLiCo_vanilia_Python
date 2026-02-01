# main.py - Arquivo PRINCIPAL que você executa

# 1. Importa o helper
from importador import importar_classe

# 2. Carrega as classes usando o helper
Produto = importar_classe("Produto", "Produto")
Item = importar_classe("Item", "Item")

# 3. TESTES DAS CLASSES (igual antes, mas sem import direto)
print("=" * 50)
print("🎯 TESTANDO SISTEMA GELICO")
print("=" * 50)

# Teste 1: Criar produtos
print("\n1. Criando produtos...")
p1 = Produto("Arroz", "Tio João", "Alimentos")
p2 = Produto("Feijão", "Kicaldo", "Alimentos")
print(f"   Produtos criados: {Produto.contador_id}")

# Teste 2: Listar produtos
print("\n2. Listando produtos...")
Produto.listar_produtos()

# Teste 3: Buscar produto
print("\n3. Buscando produto...")
# Chama buscar_por() diretamente da classe
# (Precisa ajustar buscar_por() para ser @staticmethod)

# Teste 4: Criar item
print("\n4. Criando item...")
item1 = Item(p1, 25.90, 2, "kg",5)
print(f"   Item criado: {item1}")
print(f"   Preço por kg: R$ {item1.preco_por_unidade_base():.2f}")

# Teste 5: Usar novo_item() interativo
print("\n5. Modo interativo...")
print("   (Descomente a linha abaixo para testar)")
# Item.novo_item()  # Descomente quando quiser testar interativo

print("\n" + "=" * 50)
print("✅ TESTES CONCLUÍDOS!")
print("=" * 50)