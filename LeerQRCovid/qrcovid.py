import sys
import zlib
import base45
import cbor2
import pprint #Para imprimir los diccionarios

#Copiar aquí el texto QR Covid
certificado = ""

dato_base45 = certificado.replace("HC1:", "")

zlibdata = base45.b45decode(dato_base45)

cbordata = zlib.decompress(zlibdata)

decoded = cbor2.loads(cbordata)

#print(cbor2.loads(decoded.value[2]))

pprint.pprint(cbor2.loads(decoded.value[2]))

