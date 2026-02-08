from Produto import Produto
class Item():
  lista_itens_atual = []
  item_atual = {}
  contador_id = 0
  
  def __init__(self,produto,valor_unitario,quantidade, valor_total):
    self.id = Item.contador_id
    self.produto = produto
    self.valor_unitario = valor_unitario
    self.quantidade = quantidade
    self.valor_total = valor_total
    self.dados_item = {
      "id": self.id,
      "produto": self.produto,
      "valor_unitario": self.valor_unitario,
      "quantidade": self.quantidade,
      "valor_total": self.valor_total,
    }
    self.lista_itens_atual.append(self.dados_item)
    Item.contador_id+=1
    
  def __str__(self):
    return f'{self.quantidade}x {self.produto["nome"]} {self.produto["marca"]} R${self.valor_unitario} TOTAL: R${self.valor_total}'
  
  #entrada de itens interativo
  @classmethod  
  def novo_item(cls):
    coleta_dados = True
    print('''
          𝕀𝕟𝕤𝕚𝕣𝕒 𝕦𝕞 𝕚𝕥𝕖𝕞
    ''')
    produto = Produto.buscar_por()
    while coleta_dados == True:
      valor_unitario = float(input(f'Insira o preço do {produto['nome']}: '))
      quantidade = float(input(f'Insira a quantidade de {produto['nome']}: '))
      if valor_unitario != '' and quantidade != '':
        coleta_dados = False
 #data (criado em...)
  
    novo_item = cls(produto=produto,valor_unitario=valor_unitario, quantidade=quantidade,valor_total = valor_unitario * quantidade)  
    #valor_total = novo_item.valor_item()
   
    print(novo_item)
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
  
  def valor_item(self):
    valor_final = self.valor_unitario * self.quantidade
    return valor_final


Item.novo_item()
