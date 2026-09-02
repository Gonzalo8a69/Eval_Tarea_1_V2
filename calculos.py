import numpy as np

def calcular_ipr(reservorio, pwf_actual):
    pr, pb, j = reservorio.pr, reservorio.pb, reservorio.j
    qb = j * (pr - pb)
    qmax = qb + (j * pb / 1.8)
    
    if pwf_actual >= pb:
        qo = j * (pr - pwf_actual)
        estado = "Por encima de Pb (Flujo Lineal)"
    else:
        qo = qb + (j * pb / 1.8) * (1 - 0.2 * (pwf_actual / pb) - 0.8 * (pwf_actual / pb)**2)
        estado = "Por debajo de Pb (Flujo de Vogel)"
        
    pwf_array = np.linspace(0, pr, 50)
    qo_array = [
        j * (pr - p) if p >= pb else qb + (j * pb / 1.8) * (1 - 0.2 * (p / pb) - 0.8 * (p / pb)**2)
        for p in pwf_array
    ]
            
    return qo, qb, qmax, estado, pwf_array, qo_array

def calcular_hidrostatica(pozo):
    gh = 0.052 * pozo.mw
    ph = gh * pozo.tvd
    dp = ph - pozo.pform
    
    if dp > 0:
        condicion = "Sobrebalance"
    elif abs(dp) < 50:
        condicion = "Balance aproximado"
    else:
        condicion = "Bajo balance"
        
    return gh, ph, dp, condicion

def calcular_volumetria(prop):
    hn = prop.h * prop.ntg
    poes_stb = (7758 * prop.area * hn * prop.porosidad * (1 - prop.swi)) / prop.boi
    poes_mmstb = poes_stb / 1_000_000
    rec_stb = poes_stb * prop.fr
    rec_mmstb = rec_stb / 1_000_000
    
    return hn, poes_stb, poes_mmstb, rec_stb, rec_mmstb