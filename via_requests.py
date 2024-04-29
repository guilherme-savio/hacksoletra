import hrequests

if __name__ == "__main__":
    resp = hrequests.get("https://g1.globo.com/jogos/static/soletra.json").json()
    
    words = [word['word'] for word in resp["word_list"]]
    words.sort(key=len)
    print("-- Palavras do dia --")
    for word in words:
        print(word)