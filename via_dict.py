import duckdb
import numpy as np


if __name__ == "__main__":
    dicionario = duckdb.sql("SELECT * FROM dicionario.parquet")

    letras = input("Insira as letras (separadas por espaço) que a palavra possa ter: ").lower().split(' ')
    
    i = ...
    while i != 0:
        inicio = input("Insira a letra inicial: ").lower()
        tamanho = int(input("Insira quantas letras a palavra possui: "))
        mapping_letras = np.array([ord(letra) for letra in letras])

        palavras = duckdb.sql(f"SELECT {inicio} FROM dicionario WHERE LENGTH({inicio}) = {tamanho}").fetchnumpy().get(inicio)
        
        print('\n')
        for palavra in palavras:
            palavra = np.array([ord(letra) for letra in palavra])
            result = np.setdiff1d(palavra, mapping_letras)
            
            if result.size == 0:
                result = ''.join([chr(letra) for letra in palavra])
                print(result)
                continue
            continue
        print('\n')
