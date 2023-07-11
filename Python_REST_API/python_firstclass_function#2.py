import itertools

Porsche_collection = [{"Model" :"911", "Year" : 2018, "Price": 193020, 'Color': "Lime Green"},
                      {"Model" : "Macan", "Year" : 2017, "Price": 163020, 'Color': "Dark Red"},
                      {"Model" : "Caynne", "Year" : 2015, "Price": 156200, 'Color': "Dark Orange"},
                      {"Model" :"Cayman", "Year" : 2021, "Price": 132100, 'Color': "La Plame"},
                      {"Model" : "Boxter", "Year" : 2022, "Price": 131000, 'Color': "Yellow"},
                      {"Model" : "Taycan", "Year" : 2023, "Price": 189000, 'Color': "White"}
                      ]


def porsche_sales (lst:list, *models, model_lock, year_lock):

    #dic of parameter inserts --> * models
    model_dic = {models[i]:models[i+1] for i in range(0,len(models),2)}

    #dic of the parameter list --> Porsche_collection
    new_lst = []
    for i in lst:
        for k, v in list(i.items())[:2]:
            new_lst.append(v)
    new_list_dict = {new_lst[i]:new_lst[i+1] for i in range(0,len(new_lst),2)}


    for item in lst:
        if model_lock(item) in list(model_dic.keys()):
            if year_lock(item) in  list(model_dic.values()):
                return(f'Found the matched model in the stock. The target -- {models} can be found available with details of {item}')
            else:
                print(f'For model {models[0]}, Theres only the year of {new_list_dict.get(models[0])}, but not of {models[1]}')
        else:
            pass

    raise TimeoutError('No such stock in inventory')


def model_finder(model):
    return model['Model']

def year_finder(year):
    return year['Year']


print(porsche_sales(Porsche_collection, 'Cayman',2021, model_lock=model_finder, year_lock=year_finder))





