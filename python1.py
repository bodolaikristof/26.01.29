''' 01---------------------------------------------------------------------------
# Feladat: Két szám összege.
#Írj egy függvényt "osszead" néven, amely két számot kap és visszatér a két szám összegével.'''
def osszead(a, b):
    return a + b

#assert osszead(12, -8) == 4
#assert osszead(12,  8) == 20

''' 02-------------------------------------------------------------------
# Feladat: Melyik a kisebb?
# Írj egy függvényt "kisebb" néven, amely két számot kap és visszatér a legkisebbel.'''
def kisebb(a, b):
    if a < b:
        return a
    else:
        return b
        

#assert kisebb(12, -8) == -8
#assert kisebb(-8, 12) == -8

''' 03---------------------------------------------------------------------------
# Feladat: Melyik a nagyobb?
# Írj egy függvényt "nagyobb" néven, amely két számot kap és visszatér a legnagyobbal.'''
def nagyobb(a, b):
    if a > b:
        return a
    else:
        return b

#assert nagyobb(12, -8) == 12    
#assert nagyobb(-8, 12) == 12    

''' 04---------------------------------------------------------------------------
# Feladat: Számtani közép
# Írj "szamtani_kozep" néven függvényt, amely két számot kap bemenetként és visszatér a számtani középpel.'''
def Számtani_közép(a, b):
    return (a + b) / 2


#assert szamtani_kozep(3, 5) == 4.0


''' 05---------------------------------------------------------------------------'''

'''# Feladat: Négyzet kerülete'''
'''# Írj "negyzet_kerulet" néven függvényt, amely egy négyzet oldalhosszát kapja bemenetként és visszatér a négyzet kerületével.'''
def Négyzet_kerülete(a):
    return 4 * a
#assert negyzet_kerulet(5.1) == 20.4

''' 06---------------------------------------------------------------------------'''

'''# Feladat: Négyzet területe'''
'''# Írj "negyzet_terulet" néven függvényt, amely egy négyzet oldalhosszát kapja bemenetként és visszatér a négyzet területével.'''
def Négyzet_területe(a):
    return a * a
    

#assert negyzet_terulet(5.0) == 25.0

''' 07---------------------------------------------------------------------------'''

'''# Feladat: Téglalap kerülete'''
'''# Írj "teglalap_kerulet" néven függvényt, amely egy téglalap oldalhosszait kapja bemenetként és visszatér a téglalap kerületével.'''
def Téglalap_kerülete(a, b):
    return (a + b) * 2
    

#assert teglalap_kerulet(5, 6) == 22

''' 08---------------------------------------------------------------------------'''

'''# Feladat: Téglalap területe'''
'''# Írj "teglalap_terulet" néven függvényt, amely egy téglalap oldalhosszait kapja bemenetként és visszatér a téglalap területével.'''
def Téglalap_kerülete(a, b):
    return a * b

#assert teglalap_terulet(5, 6) == 30

''' 09------------------------------------------------------------------------------------------------------------'''

'''# Feladat: Két szám különbsége'''
'''# Írj "kulonbseg" néven függvényt, amely két számot kap bemenetként és visszatér a két szám különbségével.'''
def különbsége(a, b):
    return a - b


#assert kulonbseg(5, 6) == -1

''' 10------------------------------------------------------------------------------------------------------------'''

'''# Feladat: Maradékos osztás:'''  
'''# Írj egy "maradek" nevü függvényt, amely két számot kap bemenetként és visszatér a két szám osztásának maradékával.'''


#assert maradek(9, 4) == 1
#assert maradek(8, 4) == 0

''' 11------------------------------------------------------------------------------------------------------------'''

'''# Feladat: Páros szám:  '''
'''#Írj egy "paros" nevü függvényt, amely egy számot kap bemenetként, majd True-val tér vissza, ha a szám páros és False-al ha a szám páratlan.'''


#assert paros(9) == False
#assert paros(8) == True

''' 12------------------------------------------------------------------------------------------------------------'''

'''# Feladat: Kettővel osztható:  '''
'''# Írj egy "kettovel_oszthato" nevü függvényt, amely egy számot kap bemenetként és True-val tér vissza, ha a szám kettővel osztható és False-al ha nem.'''
def Kettővel_osztható (szam1):
    return 2 % == 0

#assert kettovel_oszthato(12) == True
#assert kettovel_oszthato(13) == False

''' 13------------------------------------------------------------------------------------------------------------'''
'''# Feladat: Hárommal osztható:'''
'''# Írj egy "harommal_oszthato" nevü függvényt, amely egy számot kap bemenetként és True-val tér vissza, ha a szám hárommal osztható és False-al ha nem.'''
def Kettővel_osztható (szam1):
    return 3 % == 0

#assert harommal_oszthato(15) == True
#assert harommal_oszthato(16) == False

''' 14------------------------------------------------------------------------------------------------------------'''
'''# Feladat: Héttel osztható: ''' 
'''# Írj egy "hettel_oszthato" nevü függvényt , amely egy számot kap bemenetként és True-val tér vissza, ha a szám héttel osztható és False-al ha nem.'''
def Kettővel_osztható (szam1):
    return 7 % == 0

#assert hettel_oszthato(21) == True
#assert hettel_oszthato(22) == False

''' 15------------------------------------------------------------------------------------------------------------'''
'''# Feladat: Kocka térfogat: ''' 
'''# Írj egy "kocka_terfogat" nevü függvényt , amely bemenetként megkapja a kocka oldal hosszúságát és a kocka térfogatával tér vissza.'''
def Kocka_térfogat(a):
    return a * a * a

#assert kocka_terfogat(2) == 8
#assert kocka_terfogat(3) == 27

''' 16------------------------------------------------------------------------------------------------------------'''
'''# Feladat: Téglatest térfogat:'''  
'''# Írj egy "teglatest_terfogat" nevü függvényt , amely bemenetként megkapja a téglatest oldalainak hosszúságát és a téglatest térfogatával tér vissza.'''


#assert teglatest_terfogat(2, 3, 4) == 24

''' 17------------------------------------------------------------------------------------------------------------'''
'''# Feladat: Derékszögü háromszög területe:  '''
'''# Írj egy "derekszogu_haromszog_terulet" nevü függvényt , amely bemenetként megkapja a befogók hosszát és a háromszög területével tér vissza.'''
def Derékszög_háromszög_területe(a, b):
    terulet = a * b / 2
    return terulet 

#assert derekszogu_haromszog_terulet(3, 4) == 6

''' 18-----------------------------------------------------------------------------------------------------------'''
'''# Feladat: Derékszögü háromszög átfogója: '''
'''# Írj egy "derekszogu_haromszog_atfogo" nevü függvényt , amely bemenetként megkapja a befogók hosszát és az átló hosszával tér vissza.'''
def Derékszögü_háromszög_átfogója(a, b):
    return (a ** 2 + b**2) **0,5

#assert derekszogu_haromszog_atfogo(3, 4), 5.0

''' 19-----------------------------------------------------------------------------------------------------------'''
'''# Feladat: Négyzet átlója:  '''
'''# Írj egy "negyzet_atloja" nevü függvényt , amely bemenetként megkapja a négyzet oldalának hosszát és az átló hosszával tér vissza.'''


#assert round(negyzet_atloja(10),5) == round(14.142135623730951,5)

''' 20-----------------------------------------------------------------------------------------------------------'''
'''# Feladat: Téglalap átlója: '''
'''# Írj egy "teglalap_atloja" nevü függvényt , amely bemenetként megkapja az oldalak hosszát és az átló hosszával tér vissza.'''

    

#assert teglalap_atloja(3, 4) == 5.0
#assert teglalap_atloja(6, 8) == 10.0

''' 21-----------------------------------------------------------------------------------------------------------'''
'''# Feladat: Abszolútérték: '''
'''# Írj egy "abszolut" nevü függvényt , amely a bemenő paraméterként kapott szám abszolút értékével tér vissza.'''


#assert abszolut( 3) == 3
#assert abszolut(-7) == 7
#assert abszolut( 0) == 0
'''#========================================================================================================================'''
