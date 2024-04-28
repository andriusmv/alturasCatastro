def sum_components(CONSTRU):
    
    component_values = {
        'I': 1,  # Una altura sobre rasante
        'II': 2,  # Dos alturas sobre rasante
        'III': 3,  # Tres alturas sobre rasante
        'IV': 4,  # Cuatro alturas sobre rasante
        'V': 5,  # Cinco alturas sobre rasante
        'VI': 6,
        'VII': 7,
        'VIII': 8,
        'IX': 9,
        'X': 10,
        'XI': 11,
        'XII': 12,
        'XIII': 13,
        'XIV': 14,
        'XV': 15,
        'XVI': 16,
        'XVII': 17,
        'XVIII': 18,
        'XIX': 19,
        'XX': 20,
        'XXI': 21,
        'XXII': 22,
        'XXIII': 23,
        'XXIV': 24,
        'XXV': 25,
        'XXVI': 26,
        'XXVII': 27,
        'XXVIII': 28,
        'XXIX': 29,
        'XXX': 30,
        'XXXI': 31,
        'XXXII': 32,
        'XXXIII': 33,
        'XXXIV': 34,
        'XXXV': 35,
        'XXXVI': 36,
        'XXXVII': 37,
        'XXXVIII': 38,
        'XXXIX': 39,
        'XL': 40,
        'XLI': 41,
        'XLII': 42,
        'XLIII': 43,
        'XLIV': 44,
        'XLV': 45,
        'XLVI': 46,
        'XLVII': 47,
        'XLVIII': 48,
        'XLIX': 49,
        'L': 50,
        'LI': 51,
        'LII': 52,  # Asumiendo edificio más alto de España como Torre de Cristal con 52 niveles en Madrid
        'B': 1,  # Balcón
        'T': 1,  # Tribuna (balcón techado)
        'TZA': 0,  # Terraza
        'POR': 1,  # Porche
        'SOP': 1,  # Soportal
        'PJE': 1,  # Pasaje
        'MAR': 1,  # Marquesina
        'P': 0,  # Patio
        'CO': 1,  # Cobertizo
        'EPT': 1,  # Entreplanta
        'SS': 0,  # Semisótano
        'ALT': 1,  # Altillo
        'PI': 0,  # Piscina
        'TEN': 0,  # Pista de Tenis
        'ETQ': 0,  # Estanque
        'SILO': 1,  # Silo
        'SUELO': 0,  # Suelo vacante
        'PRG': 1,  # Pérgola
        'DEP': 1,  # Depósito
        'ESC': 1,  # Escalera
        'TRF': 1,  # Transformador
        'JD': 0,  # Jardín
        'YJD': 0,  # Jardín que se valora
        'FUT': 0,  # Campo de Fútbol
        'VOL': 1,  # Voladizo
        'ZD': 0,  # Zona Deportiva
        'RUINA': 1,  # Ruinas
        'CONS': 0,  # En construcción
        'PRESA': 0,  # Cuerpo de presa en embalses
        'ZBE': 0,  # Balsas y estanques que se valoran
        'ZPAV': 0,  # Obras de urbanización interior
        'GOLF': 0,  # Campo de GOLF
        'CAMPING': 0,  # Camping
        'TERRENY': 0,  # Sinónimo de SUELO
        'HORREO': 0,  # Hórreo, panera, cabazo
        'PTLAN': 1,  # Pantalán embarcadero de pequeño porte
        'DARSENA': 1,  # Dársena
        '-I': 0,  # Un nivel bajo rasante

    }

    # Split por el signo '+'
    components = CONSTRU.split('+')

    # Inicia la suma
    total_sum = 0

    # Iteración por componente
    for component in components:
        # Busca el valor y lo convierte en numérico
        if component in component_values:
            total_sum += component_values[component]

    return total_sum
