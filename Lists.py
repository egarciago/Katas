print "List implementation"
#Lista declarada, vacia
listX = []
#Lista declarada, con valores de diferentes tipos
listY = ['y', 'n', 1, 0, True, False, '1']
#Esta lista contiene las dos anteriores
listZ = listX + listY
listY.append(1)
listX.append('azul')
listX.append('verde')
listX.append('rojo')
print listX.index('rojo')
listX.reverse()
print listX.index('rojo')
print 'Cantidad:' + str(listY.count(1))
listZA = listX + listY
#Se recorre la lista, se agrega a una variable cada elemento de la lista
for result in listZA:
	print result

#Mostrar el tamano de cada lista
print 'ListX ' + str(len(listX))
print 'ListY ' + str(len(listY))
print 'ListZ ' + str(len(listZ))
print 'ListZA ' + str(len(listZA))


