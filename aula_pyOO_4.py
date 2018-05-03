############
# Funcional e OO
# Prof. Neylson
# Gerson Vasconcelos Neto
# aula 04 - python
###########

import pandas as pd    # Trabalhar com dataframes
import numpy as np    # Cálculo e estatística
import matplotlib.pyplot as plt    # Gráficos
import seaborn as sns    # Gráficos também

pnad = pd.read_csv('https://raw.githubusercontent.com/neylsoncrepalde/introducao_ao_python/master/pes_2012.csv')


pnad.shape    # tamanho do banco

pnad.columns    # nomes das variáveis

pnad.head()    # primeiros casos

pnad.dtypes    # qual que é o type de cada variável

pnad['V0101'].head()  # fazendo um head() de um subset
pnad.V0101.head()    # fazendo um head() de um subset

pnad.UF.head()
pnad.UF.dtype    # retorna como type objeto
pnad.UF = pnad.UF.astype('category')    # mudando para uma variável categórica


###########
# Sexo

pnad.V0302.head()
pnad['sexo'] = pnad.V0302.astype('category')    # atribuir como categórica para uma variável sexo
pnad.V0302.dtype
pnad.Sexo.dtype

##########
# Cor

pnad.V0404.head()
pnad.V0404.value_counts()   # frequência

# substituir nessa variável os sem declaração para NaN

# só o subset
pnad.loc[9,'V8005']    # usar os labels
pnad.iloc[2,2]    # usar o índice [pnad.columns]

# substituindo

pnad.loc[pnad['V0404'] == 'Sem declaração', 'V0404'] = np.nan
# selecionar na V0404 apenas os casos em que a V0404 serão 'Sem declaração' e transformá-los em NaN

pnad['V0404'] = pnad['V0404'].astype('category')
pnad.V0404.dtype


#########
# Renda de todos os trabalhos - V4720

pnad['V4720'].astype('float')   # nao consegui porque tem uma sem declaração no meio

pnad.loc[pnad['V4720'] == 'Sem declaração', 'V4720'] = np.nan
pnad['renda'] = pnad['V4720'].astype('float')    # atribui a uma nova variável em float

pnad.renda.describe()    # estatísticas descritivas

###################
# analisando distribuição de sexo

pnad.sexo.value_counts()
(pnad.sexo.value_counts() / pnad.sexo.value_counts().sum())*100    # em porcentagem
# mas não estão fidedignas porque não está levando em conta o peso amostral dos indivíduos
# análise viesada

# Idade

pnad.V8005.describe()    # estatísticas descritivas
pnad.V8005.mean()    # média  (está viesada)
pnad.V8005.var()    # variância
pnad.V8005.std()    # desvio padrão

np.average(pnad.V8005, weights = pnad.V4729)     # levando em consideração o peso amostral (a V4729 são os pesos)

##############
# cor 

# distribuição de frequência
pd.crosstab(index = pnad.V0404, columns = 'Counts')  # a diferença da value_counts é a ordenação

# distribuição de porcentagens (parametro para percentual = normalize)
pd.crosstab(index = pnad.V0404, columns = '%',
            normalize = True) * 100

# tabela cruzada entre sexo e cor
pd.crosstab(index = pnad.V0404, columns = pnad.sexo)

# em porcentagem pelas linhas (margins = mostra os totais)
pd.crosstab(index = pnad.V0404, columns = pnad.sexo,
            margins = True, normalize = 'index') * 100

# em porcentagem pelas colunas (margins = mostra os totais)
pd.crosstab(index = pnad.V0404, columns = pnad.sexo,
            margins = True, normalize = 'columns') * 100

# percetuais da tabela inteira
pd.crosstab(index = pnad.V0404, columns = pnad.sexo,
            margins = True, normalize = 'all') * 100

####################
# sexo em gráficos

# sns é do seaborn e plt é do matplotlib 
sns.countplot(x = pnad.sexo)
plt.title('Distribuição de sexo no Brasil - 2012')
plt.xlabel('Sexo')
plt.ylabel('Frequência')
plt.show()

# grafico deitado
sns.countplot(y = pnad.sexo)
plt.title('Distribuição de sexo no Brasil - 2012')
plt.ylabel('Sexo')
plt.xlabel('Frequência')
plt.show()
            
# cor / raça

sns.set(color_codes = True) # usando as paletas de cores do seaborn
sns.countplot(y = pnad.V0404)
plt.ylabel('Cor/Raça')
plt.xlabel('Frequência')
plt.show()

# tudo em vermelho

sns.set(color_codes = True) # usando as paletas de cores do seaborn
sns.countplot(y = pnad.V0404, color = 'r')
plt.ylabel('Cor/Raça')
plt.xlabel('Frequência')
plt.show()

# visualizando variáveis numéricas

# histograma
sns.distplot(pnad.renda.dropna(), kde = False)    # dropna para tirar as NaNs para poder plotar o gráfico
plt.show()


# densidade
sns.distplot(pnad.renda.dropna(), hist = False)
plt.show()


# modificando algumas coisas
fig, ax = plt.subplots()   # axys
fig.set_size_inches(8, 6)
sns.distplot(pnad.renda.dropna(), hist = False)
plt.show()

# cruzar uma numérica e uma categórica
sns.boxplot(x = 'V0404', y = 'V8005', data = pnad)
plt.show()

# cruzar duas variáveis numéricas
# gráfico de dispersão

plt.scatter(x = pnad.renda, y = pnad.V8005)
plt.show()

# scatter e a histograma de cada variável
sns.jointplot(x = pnad.renda, y = pnad.V8005)
plt.show()





