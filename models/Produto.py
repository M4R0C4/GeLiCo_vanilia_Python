
class Produto:
    lista_produtos = {
    }
    db_produtos =[]
    contador_id = 0

    def __init__(self, nome,marca, categoria):
        self.id = Produto.contador_id
        Produto.contador_id += 1
        self.nome = nome
        self.marca = marca
        self.categoria = categoria
        novo = Produto.lista_produtos[self.id] = {
            "id": Produto.contador_id,
            "nome": nome,
            "marca": marca,
            "categoria": categoria
        }
        self.db_produtos.append(novo)
        #self.historico_precos = []  # Lista de ItensCompra
    def __str__(self):
      return f'{self.id} • {self.nome} {self.marca} - categoria: {self.categoria}'
      
    @staticmethod 
    def listar_produtos():
      for produto in Produto.db_produtos:
        print(produto)
    
    @classmethod
    def cadastrar_produto(cls):
      nome = str(input("Nome do Produto: "))
      marca = str(input(f"Marca do {nome}: "))
      categoria = str(input(f"Categoria do {nome}: "))
      return cls(nome,marca,categoria)
    
    
      
      
n=2
i=1
while i <= n:
  Produto.cadastrar_produto()
  print('Produto cadastrado!')
  i+=1


Produto.listar_produtos()

