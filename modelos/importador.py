def importar_classe(nome_classe, nome_arquivo=None):
    
    # === TENTATIVA 1: IMPORT NORMAL (PC) ===
    try:
        # Se tivermos nome do arquivo
        if nome_arquivo:
            # Passo 1: Importa o arquivo (módulo)
            # Ex: __import__("produto") → import produto
            arquivo_importado = __import__(nome_arquivo)
            
            # Passo 2: Pega a classe dentro do arquivo
            # Ex: getattr(arquivo_importado, "Produto") → arquivo_importado.Produto
            classe_desejada = getattr(arquivo_importado, nome_classe)
            
            return classe_desejada
            
        else:
            # Se não tiver nome_arquivo, assume que é igual ao nome da classe
            arquivo_importado = __import__(nome_classe.lower())  # "Produto" → "produto"
            classe_desejada = getattr(arquivo_importado, nome_classe)
            return classe_desejada
    
    # === SE FALHOU (provavelmente no Acode) ===        
    except ImportError:
        # TENTATIVA 2: CARREGAMENTO MANUAL (Acode)
        try:
            import os
            
            # Verifica se o arquivo existe
            caminho_arquivo = f"{nome_arquivo}.py"
            if nome_arquivo and os.path.exists(caminho_arquivo):
                
                # Lê o conteúdo do arquivo como texto
                with open(caminho_arquivo, "r") as arquivo:
                    codigo_fonte = arquivo.read()  # String com todo o código Python
                
                # Cria um "container" vazio para executar o código
                container = {}
                
                # Executa o código dentro do container
                # Tudo definido no código vai para o container
                exec(codigo_fonte, container)
                
                # Pega a classe do container
                classe_desejada = container.get(nome_classe)
                
                if classe_desejada:
                    return classe_desejada
                    
        except Exception:
            # Se algo deu errado no carregamento manual
            pass
        
        # === TENTATIVA 3: CLASSE FANTASMA (último recurso) ===
        print(f"⚠️  AVISO: Classe {nome_classe} não pôde ser carregada!")
        
        # Cria uma classe vazia para não quebrar o código
        class ClasseTemporaria:
            def __init__(self, *args, **kwargs):
                print(f"  (Usando classe temporária para {nome_classe})")
                pass
        
        return ClasseTemporaria