def permutations(iterable, r=None):
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

# # Example usage
# items = [1, 2, 3]
# permutations_list = permutations(items)

# print(type(permutations_list))
# for perm in permutations_list:
#     print(perm)


li_input1 = [[0,2,1,6],
            [2,0,5,3],
            [1,5,0,4],
            [6,3,4,0]]


# li_input = [[0,2,1,6],
#             [2,0,5,3],
#             [1,5,0,4],
#             [6,3,4,0]]

li_input2 = [[0, 10, 15, 20],
            [10, 0, 35, 25],
            [15, 35, 0, 30],
            [20, 25, 30, 0]]

# PNMCA
li_input3 = [[0, 210, 280, 420, 230], # P
            [210, 0, 310, 350, 310], # N
            [280, 310, 0, 240, 170], # M
            [420, 350, 240, 0, 290], # C
            [230, 310, 170, 290, 0]] # A

# ans: PAMCNP, 1300

import BF, SA

# best_path, best_dist = BF.BF(li_input3)
best_path, best_dist = SA.SA(li_input3, 1, 0.01, 10)
print('最短路徑：' + str(best_path))
print('最短距離：' + str(best_dist))





