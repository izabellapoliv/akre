from calculations.helpers.default import default_tax

def calculate_total(importancia_segurada):
    cotacao_taxa = 10
    return (cotacao_taxa / 100) * importancia_segurada

def calculate_premio_liquido_conteudo(importancia_segurada):
    return (importancia_segurada * default_tax)/1000
