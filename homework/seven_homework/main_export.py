from create_database import create_data
from export import export_txt
from data import list_dic


data_one = create_data()
list_dic.append(data_one)
export_txt(data_one)
