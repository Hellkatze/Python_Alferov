from numbers import Number

def get_min(input_list: list):
    
    assert isinstance(input_list, list), "Входной параметр не является списком"
    assert len(input_list) > 0, "Входной параметр является пустым списком"

    current_min = input_list[0]
    for i in input_list: 
        assert isinstance(i, (int, float, complex)) and not isinstance(i, bool), "Входной параметр содержит не только числовые данные"
        if i < current_min: 
            current_min = i 

    return current_min

ind = []

example_list = [-5,-4,4556,123,44,-5,0,324]
min_value = get_min(example_list)

d = min_value

for i, j in enumerate(example_list):
    if j == d:
        ind.append(i)

print(ind)