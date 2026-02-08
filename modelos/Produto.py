import sys
print(sys.path)
class Produto:
    
    lista_produtos = {}
    catalogo_produtos =[{'id': 0, 'nome': 'Creme dental', 'marca': 'Colgate', 'categoria': 'Higiene'},
{'id': 1, 'nome': 'Refrigerante', 'marca': 'Coca-Cola', 'categoria': 'Bebida'}]
    contador_id = 0

    def __init__(self, nome,marca, categoria):
        self.id = Produto.contador_id
        self.nome = nome
        self.marca = marca
        self.categoria = categoria
        novo = Produto.lista_produtos[self.id] = {
            "id": self.id,
            "nome": nome,
            "marca": marca,
            "categoria": categoria
        }
        Produto.contador_id += 1
        self.catalogo_produtos.append(novo)
        #self.historico_precos = []  # Lista de ItensCompra
    def __str__(self):
      return f'{self.id} • {self.nome} {self.marca} - categoria: {self.categoria}'
      
    @staticmethod 
    def listar_produtos():
      for produto in Produto.catalogo_produtos:
        print(produto)
    
    @classmethod
    def cadastrar_produto(cls):
      nome = str(input("Nome do Produto: "))
      marca = str(input(f"Marca do {nome}: "))
      categoria = str(input(f"Categoria do {nome}: "))
      return cls(nome,marca,categoria)
    
    def valida_campo(campo):
      if isinstance(campo, str):
        if campo == '':
          print('O campo não pode ser vazio!')
          campo = input('Tente novamente: ')
          
    @staticmethod
    def buscar_por():
      chaves = ["nome","marca", "categoria"]
      print(f'Critérios de busca possíveis: {', '.join(chaves)}')
     
      chave = str(input("Sua escolha: ")).strip()
      while chave not in chaves:
        print("Critério inválido!")
        print(f'Critérios de busca possíveis: {', '.join(chaves)}')
        chave = str(input("Sua escolha: ")).strip()
    
      valor = str(input(f"Produto procurado pelo {chave}: ")).strip().capitalize()

      
      for item in Produto.catalogo_produtos:
        if valor in item[chave]:
          print('Produto encontrado!')
          print(item)
          return item 
        else:
          print('Produto não encontrado!')
          print('Deseja cadastrar? [S/N]')
          escolha = str(input('Escolha: ')).upper()
          if escolha == 'S':
            Produto.cadastrar_produto()
            Produto.listar_produtos()
          
    

#Produto.buscar_por()