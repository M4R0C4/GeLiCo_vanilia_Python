from Produto import Produto
class Item():
  # Tabela de conversão para unidade base
  CONVERSOES = {
        "g": 0.001,     # 1g = 0.001kg
        "kg": 1.0,
        "ml": 0.001,    # 1ml = 0.001L
        "L": 1.0,
        "un": 1.0       # unidade
    }
  
  lista_itens_atual = []
  item_atual = {}
  contador_id = 0
  
  def __init__(self,produto,preco,quantidade,medida,valor_medida):
    self.id = Item.contador_id
    self.produto = produto
    self.preco = preco
    self.quantidade = quantidade
    self.medida = medida
    self.valor_medida = valor_medida
    self.dados_item = {
      "id": self.id,
      "produto": self.produto,
      "quantidade": self.quantidade,
      "medida": self.medida,
      "valor_medida": self.valor_medida
    }
    self.lista_itens_atual.append(self.dados_item)
    Item.contador_id+=1
    
  def __str__(self):
    return f'{self.quantidade}x {self.produto.nome} {self.produto.marca} {self.valor_medida}{self.medida} R${self.preco}'
  
  #entrada de itens interativo
  @classmethod  
  def novo_item(cls):
    print('''
𝕀𝕟𝕤𝕚𝕣𝕒 𝕦𝕞 𝕚𝕥𝕖𝕞
    ''')
    produto = Produto.buscar_por()
    Produto.verifica_campo(produto)
    preco = float(input(f'Insira o preço do {produto['nome']}: '))
    Produto.verifica_campo(preco)
    
    quantidade = float(input(f'Insira a quantidade de {produto['nome']}: '))
    Produto.verifica_campo(quantidade)
    medida = input(f'Qual a medida (L,Kg,g): ').upper()
    Produto.verifica_campo(medida)
    valor_medida = float(input(f'Quantos {medida} tem {produto['nome']}: '))
    Produto.verifica_campo(valor_medida)
    #data (criado em...)

    print(cls(produto=produto, preco=preco, quantidade=quantidade,medida=medida, valor_medida=valor_medida))
    return cls(produto=produto, preco=preco, quantidade=quantidade,medida=medida, valor_medida=valor_medida)  
  
  def mostrar_lista_atual():
    for item in Item.lista_itens_atual:
      print(item)

  def preco_por_unidade_base(self):
        """Calcula preço por kg/L/unidade base"""
        fator = self.CONVERSOES.get(self.medida, 1.0)
        quantidade_base = self.quantidade * fator
        return self.preco / quantidade_base
        
