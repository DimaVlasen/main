
from dataclasses import dataclass 

@dataclass 
class TypeOfMainAssets :
    code: int 
    type: str

@dataclass
class MoveOfMainAssets 
    name: str
    code: int 
    remainder: float 
    received: float 
    output: float 

type_array = []
type_arreay.append(TypeOfMainAssets(1"Код Валюти"))
type_arreay.append(TypeOfMainAssets(2"Курс грн на 1.10"))
type_arreay.append(TypeOfMainAssets(3"Курс грн на 1.11"))
type_arreay.append(TypeOfMainAssets(4"Курс грн на 1.12"))
type_arreay.append(TypeOfMainAssets(5"Рік"))

move_array = []
meve_array.append(MoveOfMainAssets("103", 5.65, 6.05, 10.03, 2003))
meve_array.append(MoveOfMainAssets("104", 1.13, 1.23, 2.00,  2003))
meve_array.append(MoveOfMainAssets("105", 2.28, 2.52, 4.12,  2003))
meve_array.append(MoveOfMainAssets("106", 2.02, 2.24, 3.66,  2003))
meve_array.append(MoveOfMainAssets("109", 2.68, 3.18, 5.12,  2003))
meve_array.append(MoveOfMainAssets("111", 3.34, 3.96, 6.53,  2003))
meve_array.append(MoveOfMainAssets("103", 1.10, 11.21,13.50, 2004))
meve_array.append(MoveOfMainAssets("104", 2.50, 2.60, 2.75,  2004))
meve_array.append(MoveOfMainAssets("105", 4.44, 4.65, 4.70,  2004))
meve_array.append(MoveOfMainAssets("106", 4.05, 4.25, 4.50,  2004))
meve_array.append(MoveOfMainAssets("109", 6.05, 6.30, 6.80,  2004))
meve_array.append(MoveOfMainAssets("111", 7.00, 7.25, 7.50,  2004))
meve_array.append(MoveOfMainAssets("103", 13.64,13.70,13.80, 2005))
meve_array.append(MoveOfMainAssets("104", 2.80, 2.83, 2.85,  2005))
meve_array.append(MoveOfMainAssets("105", 4.75, 4.80, 4.85,  2005))
meve_array.append(MoveOfMainAssets("106", 4.62, 4.64, 4.66,  2005))
meve_array.append(MoveOfMainAssets("109", 6.90, 6.95, 7.00,  2005))
meve_array.append(MoveOfMainAssets("111", 7.65, 7.5,  7.85,  2005))

def printMoveOfMainAssets(moveOfMainAssets):
    '''printMoveOfMainAssets function prints
    "Рух основних засобів"
    with names and values'''

    print("Код: {code}, Період: {period}, Товарообіг: {obig}, Валовий доход: {vdoxod}, Витрати обігу: {vobigu}, Прибуток від реалізації: {pributok}, Інший прибуток: {inspributok}, Податок: {podatok}"
        .format(code=moveOfMainAssets.code, period=moveOfMainAssets.period, obig=moveOfMainAssets.obig, vdoxod=moveOfMainAssets.vdoxod, vobigu=moveOfMainAssets.vobigu,
            pributok=moveOfMainAssets.pributok, inspributok=moveOfMainAssets.inspributok, podatok=moveOfMainAssets.podatok))

for data in move_array:
    printMoveOfMainAssets(data)

def printTypeOfMainAssets(typeOfMainAssets):
    '''printTypeOfMainAssets function prints
    "Вид основних засобів"
    with names and values'''
    
    print("Код: {code}, Назва: {name}, Площа: {plosha} "
        .format(code=typeOfMainAssets.code, name=typeOfMainAssets.name, plosha=typeOfMainAssets.plosha))

for data in type_array:
    printTypeOfMainAssets(data)




