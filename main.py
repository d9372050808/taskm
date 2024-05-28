import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from os import stat
from datetime import datetime

class Element:
  index_id=0

  def __init__(self,element_type,name):
    Element.index_id=Element.index_id+1
    self.name=name
    self.element_type=element_type

  def to_dict(self):
    return {"index_id":self.index_id,
            'element_type':self.element_type,
            'name':self.name}

class ElementMethod:
  def __init__(self):
    self.df=pd.DataFrame(columns=["index_id", "name", "element_type"])


  def add_element(self,element_type,name):
    new_element=Element(element_type,name)# тут создаем новый экземпляр
    new_element_df=pd.DataFrame([new_element.to_dict()]) # тут делаем из него датафрейм
    self.df=pd.concat([self.df,new_element_df],ignore_index=True) # тут обьединяем путой self.df и новую строку из созданного экземпляра
    return new_element

  def list_element(self):
    return self.df

method=ElementMethod()

method.add_element('status','завтра')
method.add_element('status','рр')
print(method.list_element())

# status=Element('status','завтра')
# status=Element('status','сегодня')
# # status.to_dict()
# pd.DataFrame(status.to_dict(), pd.DataFrame(columns=["element_id", "name", "element_type"]))