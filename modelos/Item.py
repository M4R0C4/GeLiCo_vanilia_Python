from Produto import Produto

class Item():
  lista_itens = []
  contador_id = 0
  
  def __init__(self,produto,valor_unitario,quantidade, valor_total):
    self.id = Item.contador_id
    self.produto = produto
    self.valor_unitario = valor_unitario
    self.quantidade = quantidade
    self.valor_total = valor_total
    Item.contador_id+=1
    
  def __str__(self):
    return f'{self.quantidade}x {self.produto["nome"]} {self.produto["marca"]} R${self.valor_unitario} TOTAL: R${self.valor_total}'
  
  #entrada de itens interativo
  @classmethod  
  def novo_item(cls):
    texto_novo_item = '🄲🄰🄳🄰🅂🅃🅁🄾 🄳🄴 🄸🅃🄴🄽🅂'
    print(texto_novo_item.center(10))
    try:
      produto = Produto.buscar_por()
      valor_unitario = float(input(f'Insira o valor unitário: '))
      quantidade = float(input(f'Insira a quantidade: '))
      valor_total = quantidade * valor_unitario
      for item in cls.lista_itens:
        if item["produto"].lower() == produto.lower() and item["valor_unitario"] == valor_unitario:
          print('Item já foi criado!')
          escolha = input('Deseja criar outro item? [s/n]: ').lower().strip()
          if escolha == 's':
            cls.novo_item()
          elif escolha == 'n':
            print('Ok...')
            return
      novo_item = cls(produto=produto,valor_unitario=valor_unitario, quantidade=quantidade,valor_total=valor_total) 
      cls.lista_itens.append(novo_item)
      print(novo_item)
    except TypeError as e:
      print(f'erro: {e}')
      print('Nao foi possivel inserir novo item. Tente novamente!')
      Item.novo_item()
  
  @staticmethod
  def mostrar_lista_atual():
    texto = '🄸🅃🄴🄽🅂 🄸🄽🅂🄴🅁🄸🄳🄾🅂'
    print(texto.center(10))
    for item in Item.lista_itens:
      print(item)
  def teste():
    print('Classe Item importada com sucesso!')
      
  
  
