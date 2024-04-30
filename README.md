# Para qué sirve
Convierte la nomenclatura tipo string de Catastro (ES) del campo CONSTRU a valor numérico. El resultado puede usarse para extruir los polígonos al muktiplicarlos por un valor de referencia (altura de cada altura, casi siempre 3 m). Un ejemplo de la nomenclatura es -II+IV+TZA (indicando dos niveles bajo rasante, cuatro niveles sobre rasante y terraza).

# De dónde sale
En el documento de referencia de Catastro España (tro.hacienda.gob.es/ayuda/manual_descriptivo_shapefile.pdf) se especifica la Nomenclatura de Subparcelas (pág. 13:

``4 ANEXO I:``
``4.1 NOMENCLATURA DE SUBPARCELAS``
- ``-I, -II ....... Volúmenes bajo rasante (1, 2 alturas)``
- `` I, II ........ Volúmenes sobre rasante (1, 2 alturas)``
- `` B ............. Balcón``
- `` T ............. Tribuna (balcón techado)``
- `` TZA ............. Terraza``
- `` POR ............. Porche``
- `` SOP ............. Soportal``
- `` PJE ............. Pasaje``
- `` MAR ............. Marquesina``
- `` P ............. Patio``
- `` CO ............. Cobertizo``
- `` EPT ............. Entreplanta``
- `` SS ............. Semisótano``
- `` ALT ............. Altillo``
- `` PI ............. Piscina``
- `` TEN ............. Pista de Tenis``
- `` ETQ ............. Estanque``
- `` SILO ............. Silo``
- `` SUELO ............. Suelo vacante, sin construir. También se puede utilizar el sinónimo TERRENY``
- `` PRG ............. Pérgola``
- `` DEP ............. Depósito``
- `` ESC ............. Escalera``
- `` TRF ............. Transformador``
- `` JD ............. Jardín``
- ``YJD ………. Jardín que se valora``
- `` FUT ............. Campo de Fútbol``
- `` VOL ............. Voladizo``
- `` ZD ............. Zona Deportiva``
- `` RUINA ............. Ruinas``
- `` CONS ............. En construcción``
- `` PRESA ............. Cuerpo de presa en embalses``
- `` ZBE ............. Balsas y estanques que se valoran``
- `` ZPAV ............. Obras de urbanización interior``
- `` GOLF ............. Campo de GOLF``
- `` CAMPING.......... Camping``
- `` TERRENY…….. Sinónimo de SUELO``
- `` HORREO……… Hórreo, panera, cabazo``
- `` PTLAN ............. Pantalán (embarcadero de pequeño porte, soportado por pilotes y a veces
móvil). Se utilizará este código particularmente para los puntos de amarre
de puertos deportivos. Un muelle se codificará con el código genérico
ZPAV.``
-  ``DARSENA.......... Dársena, aguas resguardadas artificialmente por un puerto.``
``Para codificar un atributo de subparcela que esté compuesto por varios elementos de la nomenclatura
anterior, se hará uniendo estos códigos, en sentido ascendente, con el signo (+).
Ejemplo: -II+IV+TZA``

 # Cómo usarlo
El uso de este script está pensado para ArcGIS Pro, aunque podría aplicarse en otras soluciones de software (feel free to contribute):

1. Descargar el shapefile del municipio de interés en [Descarga de cartografía vectorial por provincia (formato Shapefile)](https://www.sedecatastro.gob.es/Accesos/SECAccDescargaDatos.aspx)
2. Abrir el shapefile en una escena global o local en ArcGIS Pro.
3. Agregar un campo tipo "Entero corto" en la tabla de atributos llamado "Altura" o similar.
4. Calcular el campo creado e incluir la expresión del archivo "alturasCatastro.py". Hay dos casillas a llenar, primer casilla "Altura = " debe contener "sum_components(!CONSTRU!)", segunda casilla llamada Code block debe ser igual al código de "alturasCatastro.py".
5. Resultado debe mostrar valores numéricos en el campo Altura.
6. Con la capa del shapefile seleccionada en el panel de Contenido, dirigirse a pestaña Capa de entidad (Feature layer), buscar opción de Extrusión, escoger el campo Altura y completar expresión de la siguiente manera: "$feature.Altura*3". Puede variar el 3 por cualquier valor de altura por nivel como considere.
7. El resultado debe mostrar la extrusión de cada polígono en función del campo Altura.
8. Opcionalmente se puede crear una búsqueda de definición (definition query) sobre la capa del shapefile descargado para que no muestra valores de Altura iguales a cero (Altura <> 0). Esto se logra desde las Propiedades de la capa, en la pestaña Búsqueda de definición.
9. Este video puede ser de utilidad: [Resumen en YouTube](https://youtu.be/HL67Pwvk33Y)

# Cómo contribuir
Directamente con un fork de este repo o enviándome un correo a andresmorenovasquez@outlook.com

 
