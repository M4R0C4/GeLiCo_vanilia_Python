class Produto:
    lista_produtos = {}
    contador_id = 1

    def __init__(self, nome,marca, categoria):
        self.id = Produto.contador_id
        Produto.contador_id += 1
        self.nome = nome
        self.marca = marca
        self.categoria = categoria
        Produto.lista_produtos[self.id] = {
            "nome": nome,
            "marca": marca,
            "categoria": categoria
        }
        #self.historico_precos = []  # Lista de ItensCompra
    def __str__(self):
      return f'{self.nome} {self.marca} - categoria: {self.categoria}'
    @classmethod
    def cadastrar_produto(cls):
      nome = str(input('Insira o nome do produto: '))
      marca = str(input(f'Insira o nome de {nome}: '))
      categoria = str(input(f'categoria de {nome}: '))
      novo_produto = cls(nome,marca,categoria)
      return novo_produto
      
    @staticmethod 
    def listar_produtos():
      for produto in Produto.lista_produtos.items():
        print(produto)
    
    @staticmethod
    def filtrar_nome(procurado):
      produtos_encontrados = []
      for id_produto, dados in Produto.lista_produtos.items():
        if procurado.lower() == dados["nome"].lower():
          produtos_encontrados.append({
            "id":id_produto,
            "nome": dados["nome"],
            "categoria":dados["categoria"]
          })
      print(produtos_encontrados)
    

