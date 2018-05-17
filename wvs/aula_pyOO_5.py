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
wvs.loc[wvs[10] == -2, 10] =np.nan
wvs.loc[wvs[10] == -5, 10] =np.nan
wvs.loc[wvs[10] == -1, 10] =np.nan

# quantidade de pessoas que responderam sobre felicidade
wvs[10].value_counts()

# em porcentagem, arredondamos para 2 casas decimais também
round(((wvs[10].value_counts()/\
wvs[10].value_counts().sum()) * 100), 2)

# onde as pessoas sao mais felizes, Brasil(variavel 76) ou EUA (variavel 840)

#brasil
round(((wvs.loc[wvs[1] == 76, 10].value_counts() /\
wvs.loc[wvs[1] == 76, 10].value_counts().sum()) * 100), 2)

#eua
round(((wvs.loc[wvs[1] == 840, 10].value_counts() /\
wvs.loc[wvs[1] == 840, 10].value_counts().sum()) * 100), 2)

# comparando as média de felicidade entre BRA e EUA
wvs.loc[wvs[1] == 840, 10].mean()
wvs.loc[wvs[1] == 76, 10].mean()

happyBrazil = wvs.loc[wvs[1] == 76, 10]
happyUS = wvs.loc[wvs[1] == 840, 10]

# nao precisa colocar a media no scipy, ele já calcula só
t, p1 = stats.ttest_ind(happyBrazil,
                       happyUS,
                       nan_policy = 'omit')

print(f'A estatística de teste foi {t}. \n O p-valor foi {p1}.')



# comparando se a importância de política tem relação com a importância que as
# pessoas dão para a família

#### seperando as variáveis de interesse: família, amigos, tempo livre,
# política, trabalho e religião

# família
wvs[4].value_counts()

# transformando categorias de NR em NaN
wvs.loc[wvs[4] == -2, 4] =np.nan
wvs.loc[wvs[4] == -5, 4] =np.nan
wvs.loc[wvs[4] == -1, 4] =np.nan

wvs[4].value_counts()

# política
wvs[7].value_counts()

wvs.loc[wvs[7] == -2, 7] =np.nan
wvs.loc[wvs[7] == -5, 7] =np.nan
wvs.loc[wvs[7] == -1, 7] =np.nan
wvs.loc[wvs[7] == -3, 7] =np.nan

wvs[4].value_counts()

# plotando o valor da família e da política

#1) usando seaborn (família)
sns.set(color_codes = True)  # set serve para definir estilo do gráfico
sns.countplot(x = wvs[4])
plt.title('Valor dado à Família')
plt.xlabel('Família')
plt.ylabel('Frequência')
plt.show()

#2) usando o matplotlib   CORRIGIR
#plt.bar(x = wvs[4], height = True)
#plt.title('Valor dado à Família')
#plt.xlabel('Família')
#plt.ylabel('Frequência')
#plt.show()

#3) usando pandas
wvs[4].value_counts().plot(kind = 'bar')
plt.show()

# plotando para política

sns.set(color_codes = True)  # set serve para definir estilo do gráfico
sns.countplot(x = wvs[7])
plt.title('Valor dado à Política')
plt.xlabel('Política')
plt.ylabel('Frequência')
plt.show()

# testar se existe associção entre as duas. 
# A forma como uma pessoa pensa sobre política tem relação com a forma
# como essa pessoa pensa sobre família

# criar uma tabela cruzada
tabela = pd.crosstab(wvs[4], wvs[7])

# teste qui-quadrado para ver a relação de variáveis categóricas

from scipy import stats

# fiz um unpack para cada um dos resultados que ele retorna
chi2, p, dof, expec = stats.chi2_contingency(tabela)
print(f'Chi-square: {chi2}')
print(f'P-value: {p}')
print(f'Degrees of Freedom: {dof}')

###


































