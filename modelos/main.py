# main.py - Arquivo PRINCIPAL que você executa

# 1. Importa o helper
from importador import importar_classe

# 2. Carrega as classes usando o helper
Produto = importar_classe("Produto", "Produto")
Item = importar_classe("Item", "Item")
Lista = importar_classe("Lista", "Lista")

<<<<<<< HEAD
# 3. Inicia o programa
# Greetings
def greetings():
  print('''
      𝔹𝕖𝕞 𝕧𝕚𝕟𝕕𝕠
          ao 
       G͟e͟L͟i͟C͟o͟
  ''')
 
  #Listar Produtos
def listar_catalogo_produtos():
  catalogo = Produto.listar_produtos()
  return catalogo

  #Listar Itens
  
  
  #Listar ITENS
def listar_itens():
  lista_itens = Item.mostrar_lista_atual()
  return lista_itens

#Produto.cadastrar_produto()
def criar_produto():
    produto = Produto.cadastrar_produto()
    return produto
    
#Item.novo_item()
def criar_item():
  item = Item.novo_item()
  return item
  
# Menu Retorno
def retorno_menu():
  print('''
  𝐃𝐞𝐬𝐞𝐣𝐚 𝐫𝐞𝐭𝐨𝐫𝐧𝐚𝐫 𝐚𝐨
   >𝙼𝚎𝚗𝚞 𝙿𝚛𝚒𝚗𝚌𝚒𝚙𝚊l<
  ''')
  try:
    escolha = input('[𝐒]𝐢𝐦 𝐨𝐮 [𝐍]𝐚̃𝐨: ').strip().upper()
    if escolha == 'S':
      menu_principal()
    elif escolha == 'N':
      print('Encerrando o programa!')
    else:
      print('Opção invalida!')
      retorno_menu()
  except Exception as erro:
    print(f'erro: {erro}')
    retorno_menu()

#Menu Produtos
def menu_produtos():
  opcoes = '''
𝟷. 𝙽𝚘𝚟𝚘
𝟸. 𝙻𝚒𝚜𝚝𝚊𝚛 
𝟹. 𝙱𝚞𝚜𝚌𝚊𝚛 
[𝚁]𝚎𝚝𝚘𝚛𝚗𝚊𝚛
[𝚂]𝚊𝚒𝚛
  '''
  print(opcoes.center(10))
  escolha = input('𝙴𝚜𝚌𝚘𝚕𝚑𝚊: ').strip()
  if escolha == '1':
    criar_produto()
    retorno_menu()
    #Novo Produto
  elif escolha == '2':
    #Listar Produtos
    listar_catalogo_produtos()
    retorno_menu()
  elif escolha == '3':
    #Buscar Produtos
    print('Nada aqui... por enquanto!')
    menu_produtos()
  elif escolha.lower() == 'r':
    #retornar ao Menu
    menu_principal()
  
  elif escolha.lower() == 's':
    #Sair
    print('Encerrando programa!')
  else:
    print('Opção inválida! Tente novamente')
    menu_produtos()

#Menu Itens  
def menu_itens():
  opcoes = '''
𝟷. 𝙽𝚘𝚟𝚘
𝟸. 𝙻𝚒𝚜𝚝𝚊𝚛 
𝟹. 𝙱𝚞𝚜𝚌𝚊𝚛 
[𝚁]𝚎𝚝𝚘𝚛𝚗𝚊𝚛
[𝚂]𝚊𝚒𝚛
  '''
  print(opcoes.center(10))
  escolha = input('𝙴𝚜𝚌𝚘𝚕𝚑𝚊: ').strip()
  if escolha == '1':
    #Novo Item
    criar_item()
    retorno_menu()
  elif escolha == '2':
    #Listar Item
    listar_itens()
    retorno_menu()
  elif escolha == '3':
    #Buscar Item
    print('Nada aqui... por enquanto')
    menu_itens()
  elif escolha.lower() == 'r':
    #retornar ao Menu Principal
    menu_principal()
  
  elif escolha.lower() == 's':
    #Sair
    print('Encerrando Programa!')
  else:
    print('Opção inválida! Tente novamente')
    menu_itens()
    
# Menu PRINCIPAL
def menu_principal():
  titulo = '𝙼𝚎𝚗𝚞 𝙿𝚛𝚒𝚗𝚌𝚒𝚙𝚊𝚕'
  menu = '''𝟷. 𝙿𝚛𝚘𝚍𝚞𝚝𝚘𝚜
𝟸. 𝙸𝚝𝚎𝚗𝚜
𝟹. 𝙻𝚒𝚜𝚝𝚊𝚜
[𝚂]𝚊𝚒𝚛
  '''
  print(titulo.center(10))
  print(menu)
  try:
    escolha = input('Escolha uma opção: ').strip().upper()
    if escolha == '1':
  # Opcao 1: Produto
      menu_produtos()
      
    elif escolha == '2':
  # Opcao 1: Itens
      menu_itens()
  
    elif escolha == '3':
  # Opcao 3: Listas
      print('Nada aqui... por enquanto')
      menu_principal()
    elif escolha == "S":
     print('Opcao Sair')  
  # Opcao 6: Sair
    else:
      print('Opção inválida')
      print('Tente Novamente!')
      menu_principal()
  
  except Exception as erro:
    print('Escolha inválida. Tente novamente.')
    print(f'{erro}')
    menu_principal()

def main():
  greetings()
  menu_principal()

#Produto.listar_produtos()
if __name__ == "__main__":
  main()
  

=======
#Produto.cadastrar_produto()
#Produto.listar_produtos()
Item.novo_item()
Item.mostrar_lista_atual()
>>>>>>> 107e402f4fdc2f9c3c340d031c2c032d0cb1952e
