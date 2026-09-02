def validar_ipr(pr, pb, j, pwf):
    if any(v < 0 for v in [pr, pb, j, pwf]):
        return False, "Error: Ningún parámetro puede ser negativo."
    if pr <= pb:
        return False, "Error: Para un reservorio subsaturado, Pr debe ser mayor a Pb."
    if pwf > pr:
        return False, "Error: La presión de fondo (Pwf) no puede ser mayor a Pr."
    return True, "OK"

def validar_perforacion(mw, md, tvd, pform):
    if mw <= 0 or md <= 0 or tvd <= 0:
        return False, "Error: MW, MD y TVD deben ser mayores a cero."
    if pform < 0:
        return False, "Error: La presión de formación no puede ser negativa."
    if tvd > md:
        return False, "Error: La profundidad vertical (TVD) no puede ser mayor a la medida (MD)."
    return True, "OK"

def validar_poes(area, h, ntg, porosidad, swi, boi, fr):
    if area <= 0 or h <= 0:
        return False, "Error: El área y el espesor deben ser mayores a cero."
    if not all(0 <= val <= 1 for val in [ntg, porosidad, swi, fr]):
        return False, "Error: NTG, Porosidad, Swi y FR deben ingresarse como fracciones (0 a 1)."
    if boi <= 0:
        return False, "Error: El factor volumétrico (Boi) debe ser mayor a cero."
    return True, "OK"