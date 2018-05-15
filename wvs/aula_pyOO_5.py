# -*- coding: utf-8 -*-
"""
World Value Survey
Brincando com os dados
Gerson Vasconcelos
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
import numpy as np

os.listdir()   #listar o diretório atual

wvs = pd.read_csv('WV6_Data_ascii_v_2015_04_18.dat',
                  header = None)
# parametro header = None diz que não há nome para as variáveis


wvs.shape  # tamanho do banco
wvs.columns # nome das colunas

# 76 é brasil e 2 argelia, quantidade de entrevistados no brasil e na argelia
wvs.loc[(wvs[1] == 76) | 
        (wvs[2] == 12), 1].value_counts()

# 9 é a variável ser feliz, transformando em NaN (sao variaveis que nao foram respondidas #checar dict de var)
wvs.loc[wvs[9] == -2, 9] =np.nan
wvs.loc[wvs[9] == -5, 9] =np.nan
wvs.loc[wvs[9] == -1, 9] =np.nan

# quantidade de pessoas que responderam sobre felicidade
wvs[9].value_counts()

# em porcentagem, arredondamos para 2 casas decimais também
round(((wvs[9].value_counts()/\
wvs[9].value_counts().sum()) * 100), 2)

# onde as pessoas sao mais felizes, Brasil(variavel 76) ou EUA (variavel 840)

#brasil
round(((wvs.loc[wvs[1] == 76, 9].value_counts() /\
wvs.loc[wvs[1] == 76, 9].value_counts().sum()) * 100), 2)

#eua
round(((wvs.loc[wvs[1] == 840, 9].value_counts() /\
wvs.loc[wvs[1] == 840, 9].value_counts().sum()) * 100), 2)

## usando o ggplot

from ggplot import *

ggplot(wvs, aes(x = 9)) + geom_bar()

## com seaborn




















