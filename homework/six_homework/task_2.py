values = [1, 12, 42, 51, 13, '21w']
transformation = lambda x: x
transformed_values = list(map(transformation, values))
if values == transformed_values:
    print("ok")
else:
    print('fail')