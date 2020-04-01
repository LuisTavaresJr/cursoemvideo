def notas(*n, sit=False):
    r = {}
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n) / len(n)
    if sit:
        if r['média'] >= 7:
            r['sitiação'] = 'Boa'
        if r['média'] >= 5:
            r['sitiação'] = 'Razoavel'
        else:
            r['sitiação'] = 'Ruim'
    return r



resp = notas(5.5, 2.5, 9, 8.5, sit=True)
print(resp)