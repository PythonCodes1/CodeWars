# Filters out anything other than integers
# 7 kyu

def filter_list(lst):
  return [x for x in lst if type(x) is int]
