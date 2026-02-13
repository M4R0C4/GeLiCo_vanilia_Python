
class Produto:
    catalogo_produtos =[    {
        "id": 101,
        "nome": "Teclado Mecânico",
        "marca": "HyperX",
        "categoria": "Periféricos"
    },
    {
        "id": 102,
        "nome": "Café Torrado",
        "marca": "3 Corações",
        "categoria": "Alimentos"
    },
    {
        "id": 103,
        "nome": "Caderno Universitário",
        "marca": "Tilibra",
        "categoria": "Papelaria"
    }]
    contador_id = 0
    def __init__(self, nome,marca, categoria):
        self.id = Produto.contador_id
        self.nome = nome
        self.marca = marca
        self.categoria = categoria
        Produto.contador_id += 1
        #self.catalogo_produtos.append(novo)
        #self.historico_precos = []  # Lista de ItensCompra
        
    def __str__(self):
      return f'{self.id} • {self.nome} {self.marca} - categoria: {self.categoria}'
      
    @staticmethod 
    def listar_produtos():
      texto = '🄿🅁🄾🄳🅄🅃🄾🅂 🄲🄰🄳🄰🅂🅃🅁🄰🄳🄾🅂'
      print(texto.center(10))
      for produto in Produto.catalogo_produtos:
        print(f'• {produto['id']} {produto['nome']} {produto['marca']} {produto['categoria']}')
    
    @classmethod
    def cadastrar_produto(cls):
      texto = '🄲🄰🄳🄰🅂🅃🅁🄾 🄳🄴 🄽🄾🅅🄾🅂 🄿🅁🄾🄳🅄🅃🄾🅂'
      print(texto.center(10))
      nome = str(input("Nome do Produto: "))
      Produto.valida_campo(nome)
      marca = str(input(f"Marca: "))
      Produto.valida_campo(marca)
      categoria = str(input(f"Categoria: "))
      Produto.valida_campo(categoria)
      
      for produto in cls.catalogo_produtos:
        if produto["nome"].lower() == nome.lower() and produto["marca"].lower() == marca.lower() and produto["categoria"].lower() == categoria.lower():
          print('produto ja existe')
          escolha = input('Deseja adicionar algum outro produto? [s/n]: ').strip().lower()
          if escolha == 's':
            cls.cadastrar_produto()
          elif escolha == 'n':
            print('produtos adicionados:')
            print(cls.catalogo_produtos)
            return
      novo_produto = cls(nome,marca,categoria)
      cls.catalogo_produtos.append({
        "id": novo_produto.id,
        "nome": novo_produto.nome,
        "marca": novo_produto.marca,
        "categoria": novo_produto.categoria
        })
      print(novo_produto)
      return novo_produto
    
    @staticmethod
    def valida_campo(campo):
      if isinstance(campo, str):
        if not campo:
          while not campo:
            print('O campo não pode ser vazio!')
            campo = input('Tente novamente: ')
        
        elif len(campo) < 3:
          while len(campo) < 3:
            print('Valor curto demais. Precisa de mais caractere!')
            campo = input('Tente novamente: ')
        else:
          return campo
      elif isinstance(campo, int):
        if not campo:
          while not campo:
            print('O campo não pode ser vazio!')
            campo = input('Tente novamente: ')
        elif campo < 0:
          while campo < 0:
            print('O campo nao pode ser menor que zero!')
            campo = input('Tente novamente: ')
        else:
          return campo
      elif isinstance(campo,float):
        if not campo:
          while not campo:
            print('O campo não pode ser vazio!')
            campo = input('Tente novamente: ')
        elif campo < 0:
          while campo < 0:
            print('O campo nao pode ser menor que zero!')
            campo = input('Tente novamente: ')
        else:
          return campo      
    
    @staticmethod
    def buscar_por():
      texto_busca = '🄱🅄🅂🄲🄰 🄳🄴 🄿🅁🄾🄳🅄🅃🄾🅂'
      print(texto_busca.center(10))
      chaves = ["nome","marca", "categoria"]
      print(f'Critérios de busca possíveis: {', '.join(chaves)}')
     
      chave = str(input("Sua escolha: ")).strip()
      while chave not in chaves:
        print("Critério inválido!")
        print(f'Critérios de busca possíveis: {', '.join(chaves)}')
        chave = str(input("Sua escolha: ")).strip()
        
      valor = str(input(f"Produto procurado pelo {chave}: ")).strip().capitalize()
      resultados =[]
      for item in Produto.catalogo_produtos:
        if valor in item[chave]:
          print('Produto encontrado!')
          print(f'• {produto['id']} {produto['nome']} {produto['marca']} {produto['categoria']}')
          return item
        else:
          print('Produto não encontrado!')
          print('Deseja cadastrar? [S/N]')
          escolha = str(input('Escolha: ')).upper()
          if escolha == 'S':
            Produto.cadastrar_produto()
            Produto.listar_produtos()
          
    

