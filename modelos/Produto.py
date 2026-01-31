import sys
print(sys.path)
class Produto:
    lista_produtos = {
    }
    catalogo_produtos =[]
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
    
    def buscar_por():
      chave = str(input("Nome, Marca ou Categoria? \n Qual o critério da busca: "))
      valor = str(input(f"Produto procurado pelo {chave}: "))
      for item in Produto.catalogo_produtos:
        if valor in item[chave]:
          print('Produto encontrado!')
          print(item)
          print(type(item))
        elif chave in item[chave]:
          print('Produto encontrado!')
          
          
    
    
    def buscar_por_nome():
      produto_procurado = str(input('Digite o nome do produto: '))
      for item in Produto.catalogo_produtos:
        if item["nome"] == produto_procurado:
          print('Produto encontrado!')
          print(f'produto: {item["nome"]} \n marca: {item["marca"]}\n categoria: {item["categoria"]}')
      
      
n=2
i=1
while i <= n:
  Produto.cadastrar_produto()
  print('Produto cadastrado!')
  i+=1


Produto.listar_produtos()
Produto.buscar_por()

