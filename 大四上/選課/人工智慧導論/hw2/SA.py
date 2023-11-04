import math, random

def path_cal(li_input, order):
    
    path_len = 0
    for index in range(len(order)-2):    
        path_len += li_input[order[index]][order[index+1]]
        
    last_city = order[-2]
    path_len += li_input[last_city][0]

    return path_len

def city_rand_swap(order):
    
    new_order = order[:]
    city_amt = len(order)-2
    
    # print('<-----\n', 'order:', order, ' | ', 'new:', new_order)
    a, b = random.sample(range(city_amt), 2)
    a += 1
    b += 1
    # order[a], order[b] = order[b], order[a]
    tar_a = order[a]
    tar_b = order[b]
    # print('換之前', new_order)
    new_order[a] = tar_b
    # print('換a:', new_order)
    new_order[b] = tar_a
    # print('換b:', new_order)
    # print('a:', a, ' | ', 'b:', b)
    # print('order:', order, ' | ', 'new:', new_order, '\n----->')
    
    return new_order

def SA(li_input, temp, cooling_rate, iter_times):

    # iter_times = 10
    # temp = 100
    # cooling_rate = 0.001

    city_amt = len(li_input)
    ans_city_order = []
    ans_min_path = 100000000

    # 隨機產生一組路徑長度並計算長度
    cur_path = [0]
    for index in range(city_amt-1):
        cur_path.append(index+1)
    cur_path.append(0)
    # cur_path = [0,3,4,1,2,0]
    # print('init_path:', str(path_cal(li_input, cur_path)))

    cur_path_len = path_cal(li_input, cur_path)

    for ctr in range(iter_times):
        # print(ctr)
        
        # 隨機交換兩個非起終點的城市
        new_path = city_rand_swap(cur_path)
        # print('cur:', cur_path)
        new_path_len = path_cal(li_input, new_path)
        # print('<-----', 'new:', str(new_path), str(new_path_len), '\n', 'cur:', str(cur_path), str(cur_path_len), '----->')

        if new_path_len <= cur_path_len:
            cur_path = new_path
            cur_path_len = new_path_len
            # print('cur:', cur_path_len, ' | ', 'new:', new_path_len)
            # print('cur:', cur_path, ' | ', 'new:', new_path)
            # print('---------------------')
        
        if new_path_len > cur_path_len and random.random() <= math.exp((cur_path_len-new_path_len)/temp):
            cur_path = new_path
            cur_path_len = new_path_len
            # print('cur:', cur_path_len, ' | ', 'new:', new_path_len)
            # print('cur:', cur_path, ' | ', 'new:', new_path)
            # print('---------------------')


        if ans_min_path > cur_path_len:
            ans_city_order = cur_path
            ans_min_path = cur_path_len
        #     print('cur:', cur_path_len, ' | ', 'ans:', ans_min_path)
        #     print('cur:', cur_path, ' | ', 'ans:', ans_city_order)
        #     print('---------------------')

        # print('=================')
        temp *= cooling_rate
        
    # print(ans_city_order)
    # print(ans_min_path)
    return ans_city_order, ans_min_path
