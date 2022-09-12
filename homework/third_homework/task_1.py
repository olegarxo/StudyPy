def Summ_number(lists):
    true_list = []
    lang = len(lists)
    flag = True
    count = 0
    sum_num = 0
    tamp = 0
    while flag:
        if count >= lang:
            flag = False
        else:
            true_list.append(lists[count])
            sum_num += true_list[tamp]
            count += 2
            tamp +=1
    print(f'на нечетных позициях элементы {true_list}, ответ= {sum_num}')
number = [1,2,214,15]
Summ_number(number)
