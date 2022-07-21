def find_missing_letter(chars):
    abecedario = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    indice = abecedario.find(chars[0])
    fragmento = abecedario[indice:indice+len(chars)+1]
    for e,i in enumerate(fragmento):
        if chars[e] != fragmento[e]:
            return fragmento[e]

if __name__ == "__main__":
    find_missing_letter()