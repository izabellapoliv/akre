from calculations.helpers.default import default_iof

def calculate_iof_total(premio_liquido):
    return round((premio_liquido * default_iof) / 100, 2)
