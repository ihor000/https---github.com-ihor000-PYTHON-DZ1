# В ячейке ниже представлен код генерирующий DataFrame,
# которая состоит всего из 1 столбца.
# Ваша задача перевести его в one hot вид.
# Сможете ли вы это сделать без get_dummies?


import pandas as pd
import random 
lst = ['robot'] * 10  
lst += ['human'] * 10  
random.shuffle(lst)  
data = pd.DataFrame({'human': data['whoAmI'] == 'human',
               'robot': data['whoAmI'] == 'robot'}).astype(int).head(10)
data.head(10)
         
# human	robot
# 0	0	1
# 1	1	0
# 2	1	0
# 3	1	0
# 4	1	0
# 5	0	1
# 6	0	1
# 7	0	1
# 8	0	1
# 9	1	0