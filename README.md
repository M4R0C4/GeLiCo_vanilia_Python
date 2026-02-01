<h1>GeLiCo - Gerenciador de Listas de Compra</h1>
<p>Trata-se de um projeto de aprendizagem pessoal, sem fins lucrativos. Que visa por à prova conhecimentos adquiridos estudando programação. Este projeto está sendo desenvolvido pelo computador (VSCode) e pelo smartphone (Acode).</p>

## Objetivos do projeto
GeLiCo será um gerenciador de lista de compras, permitindo ao usuário:
- Criar ==Produtos== (nome, marca e categoria)
- Criar ==Item de compra== (data, produto, preço, quantidade, unidade de medida e valor de medida)
- Criar ==Lista de Compras== (data, itens, quantidade de itens, valor final)

A ideia é que o usuário tenha seus produtos favoritos e listas de compras organizados. Também acompanhar a variação de preço dos itens.
Além disso, o usuário poderá, através do histórico do produto, ter uma estimativa do valor do produto a partir de uma média desses valores. 

## Estrutura
O GeLiCo Venilia Python é um projeto que utilizará apenas conceitos de orientação a objetos e persistencia de dados em JSON em seu desenvolvimento. 
Trata-se de um protótipo para modelos que serão utilizados no framework Flask com banco de dados SQLite.

## Etapas:

✅ Criação da Classe Produtos
✅ Criação da Classe Item
[ ] Criação da Classe Lista
[ ] Validações da criação de Produtos
[ ] Validações da criação de Item
[ ] Validações da criação de Lista
[ ] Persistência de Dados em JSON
[ ] Acesso aos dados 
[ ] Testes

#### 🎯 Estrutura final dos dados JSON:
Esse é um exemplo de como as listas de compras serão guardadas. É possível observar também os relacionamentos associados com o Item e o Produto.


````json
lista = {
    "itens": [
        {
            "id_item": 56,
            "id_produto": 986,
            "produto": {
                "nome": "Farinha de trigo",
                "marca": "Dona Benta",
                "categoria": "farinhas"
            },
            "valor": 5.78,
            "quantidade": 2
        },
        {
            "id_item": 57,
            "id_produto": 987,
            "produto": {
                "nome": "Café",
                "marca": "3 Corações",
                "categoria": "matinais"
            },
            "valor": 15.78,
            "quantidade": 1
        }
    ],
    "quantidade_itens": 3,
    "total_lista": 27.34
}
````
### Aprendizagens abordadas
- POO
- Resolução de problemas
