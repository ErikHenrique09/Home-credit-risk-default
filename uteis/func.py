
from uteis.modules import *

def selection_features(dataset, n=20, model=LogisticRegression()):
    
    dataset = normaliza(dataset)
    
    x = dataset.drop('TARGET', axis=1)
    y = dataset['TARGET']
    
    features = RFE(model, n_features_to_select = n)
    fit = features.fit(x,y)
    
    print("Dividido e fitado")
    
    cols = fit.get_support(indices=True)
    features = list(dataset.iloc[:,cols].columns)
    
    features.append("TARGET")
    
    print("Etapa: Seleção de Features concluida")
    
    return features
    

def padroniza(df):    
    
    obj_std = StandardScaler().fit(df)
    df_scalonado = pd.DataFrame(obj_std.transform(df), columns=df.columns)
    
    return df_scalonado


def normaliza(df):    
  
    obj_norm = MinMaxScaler().fit(df)
    df_normalizado = pd.DataFrame(obj_norm.transform(df), columns=df.columns)
    
    return df_normalizado


def modelagem(x, y, model):
  
    model.fit(xtrain, ytrain)
    
    return model

def class_categorical(dataset):
    # Efetua a transformação das categoricas para inteiro, classificando as no dataset
    # Pega todas as categoricas e as classifica numericamente
    
    dic_transforms = {}
    cols = dataset.columns

    for col in cols:        
        
        if dataset[col].dtypes in (object, int): 
            dataset[col] = dataset[col].fillna((dataset[col].mode()))
            dataset[col].replace(np.nan,dataset[col].mode()[0], inplace=True)
            values_dic = list(dataset[col].unique())
            dic = {}
            for index, value in enumerate(values_dic):
                if index == np.nan:
                    value = dataset[col].mode()[0]
                
                dic[value] = index

            dic_transforms[col] = dic
        else:
            dataset[col].replace(np.nan, dataset[col].median(), inplace=True)
        
    return dic_transforms


def transform(dataset, op=0, refatora=0, dic=0):
    #Realiza a transformação coluna a coluna, dps da classificação delas 
    #atraves de um dicionario
    
    filter_rows(dataset)
    
    if dic:
        dicionario = dic
    else:
        dicionario =  class_categorical(dataset)
    
    if op :
        for key, value in dicionario.items():
            for dickey, valuekey in value.items():
                if refatora and dic: 
                    dataset[key].replace(value[dickey], dickey, inplace=True)
                else:
                    dataset[key].replace(dickey, value[dickey], inplace=True)
    
    if refatora:
        dicionario = None
            
    return dicionario
          
    
def filter_rows(dataset):
    # Função que exclui colunas que contenham < que 33% dos dados
    
    rows = np.shape(dataset)[0]
    for col in list(dataset.columns):
        if dataset[col].count() < rows/2.5:
            dataset.drop(col, axis=1, inplace=True)
            
    
def slice_database(database):
    
    # Função que retorna a database dividida entre categoricas e numericas
    
    l1 = []
    l2 = []
    
    for k in database.columns:
        if (database[k].nunique()) < 60:
            l1.append(k)
        else:
            l2.append(k)
    
    return l1,l2


def submit(dataset, predict):
    # Transforma as predições em arquivo pra mandar pro kaggle
    sub = pd.Series(predict, index=dataset['SK_ID_CURR'], name='TARGET')
    sub.to_csv('./submit_kaggle.csv', header=True)


def data_visualization(data):
    df2 = data.copy()
    
    df2['CODE_GENDER'] = df2['CODE_GENDER'].replace('XNA', 'F')
    df2['CODE_GENDER'] = df2['CODE_GENDER'].replace('F', 'Feminino')
    df2['CODE_GENDER'] = df2['CODE_GENDER'].replace('M', 'Masculino')
    df2['AGE'] = df2['AGE'].apply(lambda x: int(x))
    
    df2.to_csv('../Dashboard/dados/HomeCredit.csv', encoding='utf-8')
    
    
def imput_outliers(dataset):
    
    df = dataset.copy()
    
    for col in df.columns:
        if df[col].nunique() > 70:
            aux = df[col]

            Q1 = aux.quantile(0.25)
            Q3 = aux.quantile(0.75)

            IQR = Q3 - Q1

            lim_inf = Q1-(IQR*1.5)
            lim_sup = Q3+(IQR*1.5)
            
    
            
            df[col].loc[(df[col] < lim_inf) | (df[col] > lim_sup)] = np.nan
            
    imputer = KNNImputer(n_neighbors=50, weights = 'uniform')
    imputer.fit(df)
            
    df_out = pd.DataFrame(imputer.transform(df), columns = dataset.columns)
    
    return df_out


def alter_outliers(dataset):
    
    df = dataset.copy()
    
    for col in df.columns:
        if df[col].nunique() > 70:
            aux = df[col]

            Q1 = aux.quantile(0.25)
            Q3 = aux.quantile(0.75)

            IQR = Q3 - Q1

            lim_inf = Q1-(IQR*1.5)
            lim_sup = Q3+(IQR*1.5)
            
            df[col].loc[(df[col] < lim_inf)] = lim_inf
            df[col].loc[(df[col] > lim_sup)] = lim_sup

    return df