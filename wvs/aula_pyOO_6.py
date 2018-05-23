# -*- coding: utf-8 -*-
"""
World Value Survey
Exercício
Gerson Vasconcelos

Objetivo do dia:
Descobrir a partir do WVS qual dos países
abaixo é mais feliz(10), qual tem o maior engajamento 
político(7) e qual é o mais religioso(9).
Brasil 76
Canadá 124 (não tem)
Azerbaijão 31
China 156
Latvia 428 (não tem)
Suiça 756 (não tem)
Egito 818
"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
import numpy as np

# lendo os dados
wvs = pd.read_csv('WV6_Data_ascii_v_2015_04_18.dat',
                  header = None)

# 9 é a variável ser feliz, transformando em NaN (são variaveis que não foram respondidas)
wvs.loc[wvs[10] == -2, 10] =np.nan
wvs.loc[wvs[10] == -5, 10] =np.nan
wvs.loc[wvs[10] == -1, 10] =np.nan

# transformando as categorias NR de política em NaN

wvs.loc[wvs[7] == -2, 7] =np.nan
wvs.loc[wvs[7] == -5, 7] =np.nan
wvs.loc[wvs[7] == -1, 7] =np.nan
wvs.loc[wvs[7] == -3, 7] =np.nan

# transformando as categorias NR de religião em NaN

wvs[9].value_counts()

wvs.loc[wvs[9] == -2, 9] =np.nan
wvs.loc[wvs[9] == -5, 9] =np.nan
wvs.loc[wvs[9] == -1, 9] =np.nan

## ps. os que estão comentados não tem nessa onda
# olhando as médias de felicidade
felizBrazil = round(wvs.loc[wvs[1] == 76, 10].mean(), 2)
#wvs.loc[wvs[1] == 124, 10].mean()
felizAzerb = round(wvs.loc[wvs[1] == 31, 10].mean(), 2)
felizChina = round(wvs.loc[wvs[1] == 156, 10].mean(), 2)
#wvs.loc[wvs[1] == 428, 10].mean()
#wvs.loc[wvs[1] == 756, 10].mean()
felizEgypt = round(wvs.loc[wvs[1] == 818, 10].mean(), 2)

# printando (sendo mais perto de 1, mais feliz)
print(f'A média de felicidade no Brasil é {felizBrazil}')
print(f'A média de felicidade na China é {felizChina}')
print(f'A média de felicidade no Azerbeijão é {felizAzerb}')
print(f'A média de felicidade no Egito é {felizEgypt}')

# INACABADO
dic = {'Brasil': felizBrazil,
       'Egito' : felizEgypt,
       'Azerbaijão': felizAzerb,
       'China': felizChina}

maisFeliz = min(dic.keys()) # mais feliz
menosFeliz = max(dic.keys()) # menos feliz
qntFeliz = min(dic.values()) # quanto feliz
qntTriste = max(dic.values()) # quanto triste

print(f'O país mais feliz é {maisFeliz} e sua média de felicidade é {qntFeliz}')
print(f'O país menos feliz é {menosFeliz} e sua média de felicidade é {qntTriste}')

# olhando as médias de política
polBrazil = wvs.loc[wvs[1] == 76, 7].mean()
#wvs.loc[wvs[1] == 124, 7].mean()
polChina = wvs.loc[wvs[1] == 31, 7].mean()
polAzerb = wvs.loc[wvs[1] == 156, 7].mean()
#wvs.loc[wvs[1] == 428, 7].mean()
#wvs.loc[wvs[1] == 756, 7].mean()
polEgypt = wvs.loc[wvs[1] == 818, 7].mean()


# olhando as médias de religião
relBrazil = wvs.loc[wvs[1] == 76, 9].mean()
#wvs.loc[wvs[1] == 124, 9].mean()
relChina = wvs.loc[wvs[1] == 31, 9].mean()
relAzerb = wvs.loc[wvs[1] == 156, 9].mean()
#wvs.loc[wvs[1] == 428, 9].mean()
#wvs.loc[wvs[1] == 756, 9].mean()
relEgypt = wvs.loc[wvs[1] == 818, 9].mean()
























