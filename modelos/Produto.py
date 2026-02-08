import sys
#import os
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
        print(type(produto["nome"]))
        print(produto)
    @staticmethod
    def verifica_campo(campo):
      if type(campo) == str:
        while campo == '':
          print(f'Campo vazio detectado!')
          campo = input(f'Favor, preencha o campo: ')
          if campo != '':
            break
          
      elif type(campo) == int or type(campo) == float:
        if campo < 0 or campo == '':
          print('Esse campo não recebe valores negativos.')
          campo = int(input('Por favor, use valores positivos: '))
      else:
        print('Valor incompatível com o necessario. Tente novamente.')
        pass
      return campo
      
    @classmethod
    def cadastrar_produto(cls):
      nome = str(input("Nome do Produto: ")).strip()
      cls.verifica_campo(nome)
      marca = str(input(f"Marca do {nome}: ")).strip()
      if marca == '':
        print(f'O campo marca está vazio.')
        marca = str(input(f"Marca do {nome}: ")).strip()
      categoria = str(input(f"Categoria do {nome}: ")).strip()
      if categoria == '':
        print(f'O campo marca está vazio.')
        categoria = str(input(f"Categoria do {nome}: ")).strip()
        
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
      chave = str(input("Nome, Marca ou Categoria? \n Qual o critério da busca: ")).lower()
      Produto.verifica_campo(chave)
      valor = str(input(f"Produto procurado pelo {chave}: ")).lower()
      Produto.verifica_campo(valor)

      
      for item in Produto.catalogo_produtos:
        if valor in item[chave].lower():
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