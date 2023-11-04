import math, random

def perms(iterable, r=None):
    items = list(iterable)
    n = len(items)

    if r is None:
        r = n
    if r > n:
        return []
    
    result = []

    # Helper function to generate permutations
    def generate(k):
        if k == 0:
            result.append(list(items[:r]))
        else:
            for i in range(k):
                items[k - 1], items[i] = items[i], items[k - 1]
                generate(k - 1)
                items[k - 1], items[i] = items[i], items[k - 1]

    generate(r)
    return result

def path_cal(li_input, order):
    
    path_len = 0
    for index in range(len(order)-1):    
        path_len += li_input[order[index]][order[index+1]]
        
    last_city = order[-1]
    path_len += li_input[last_city][0]

    return path_len

def BF(li_input):
    input_perms = perms(range(len(li_input)))

    city_orders = []
    for perm in input_perms:
        if perm[0] == 0:
            city_orders.append(perm)

    ans_city_order = []
    ans_min_path = 100000000

    for order in city_orders:
        path_len = 0
        # for index in range(len(order)-1):    
        #     path_len += li_input[order[index]][order[index+1]]
            
        # last_city = order[-1]
        # path_len += li_input[last_city][0]
        path_len = path_cal(li_input, order)

        # selections[1].append(path_len)

        if ans_min_path > path_len:
            ans_city_order = order
            ans_min_path = path_len

    ans_city_order.append(0)

    # print('最短路徑：' + str(ans_city_order))
    # print('最短距離：' + str(ans_min_path))
    return str(ans_city_order), str(ans_min_path)