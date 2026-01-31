
# OU importação absoluta
from models.Produto import Produto

class Item():
  lista_itens_atual = []
  item_atual = {}
  contador_id = 0
  def __init__(self,produto,preco,quantidade,medida):
    self.id = Item.contador_id
    self.produto = produto
    self.preco = preco
    self.quantidade = quantidade
    self.medida = medida
    self.dados_item = {
      "id": self.id,
      "produto": self.produto,
      "quantidade": self.quantidade,
      "medida": self.medida,
    }
    self.lista_itens_atual.append(self.dados)
    Item.contador_id+=1
    
  def __str__(self):
    return f'{quantidade}x {produto} {medida} {preco}'
    #entrada de itens interativo
  classmethod  
  def novo_item(cls):
    print('''
𝕀𝕟𝕤𝕚𝕣𝕒 𝕦𝕞 𝕚𝕥𝕖𝕞
    ''')
    produto = Produto.buscar_por()
    preco = float(input(f'Insira o preço de {produto["nome"]}: '))
    quantidade = float(input(f'Insira o preço de {produto["nome"]}: '))
    medida = float(input(f'Qual a medida (L,Kg,g): ')).upper()
    #data (criado em...)
    return cls(produto=produto, preco=preco, quantidade=quantidade,medida=medida)
  
    # Tabela de conversão para unidade base
    CONVERSOES = {
        "g": 0.001,     # 1g = 0.001kg
        "kg": 1.0,
        "ml": 0.001,    # 1ml = 0.001L
        "L": 1.0,
        "un": 1.0       # unidade
    }
    
    def preco_por_unidade_base(self):
        """Calcula preço por kg/L/unidade base"""
        fator = self.CONVERSOES.get(self.medida, 1.0)
        quantidade_base = self.quantidade * fator
        return self.preco / quantidade_base
        
Produto.novo_item()