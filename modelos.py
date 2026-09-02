from dataclasses import dataclass

@dataclass
class ReservorioSubsaturado:
    """Parámetros para la IPR (Producción)."""
    pr: float
    pb: float
    j: float

@dataclass
class DatosPozo:
    """Parámetros de Perforación."""
    mw: float
    md: float
    tvd: float
    pform: float

@dataclass
class PropiedadesPetrofisicas:
    """Parámetros Volumétricos (Reservorios)."""
    area: float
    h: float
    ntg: float
    porosidad: float
    swi: float
    boi: float
    fr: float