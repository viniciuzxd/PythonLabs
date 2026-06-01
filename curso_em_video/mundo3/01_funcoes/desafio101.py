def voto(ano_nascimento):
    # Importando dentro da função: a biblioteca datetime só existe quando voto() é chamada
    from datetime import date
    atual = date.today().year
    idade = atual - ano_nascimento
    
    if idade < 16:
        return f'Com {idade} anos: VOTO NEGADO.'
    elif 16 <= idade < 18 or idade >= 65:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'

nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))