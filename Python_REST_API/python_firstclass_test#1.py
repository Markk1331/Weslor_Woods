Porsche_collection = [{"Model":"Macan", "Year":2017},{"Model":"911", "Year":2018},{"Model":"Caynne", "Year":2015},
                      {"Model":"Cayman", "Year":2021},{"Model":"Boxter", "Year":2022},{"Model":"Taycan", "Year":2023}]


def porsche_sales (lst:list, models, system_lock):

    for item in lst:
        if system_lock(item) == models:
            return(f'Found the model in the stock. The target -- {models} can be found available with details of {item}')
        else:
            pass
    raise TimeoutError('No such stock in inventory')


def finder_model(model):
    return model['Model']




print(porsche_sales(Porsche_collection, 'Taycan', finder_model))


#for i in Porsche_collection:
    #for k,v in i.items():
        #if v == '911':
            #print ('yes')
    #print(type(i))

