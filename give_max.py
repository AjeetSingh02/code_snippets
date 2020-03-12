import operator

def give_max(inp1, inp2):
    times = list(map(int, inp2.split(" ")))
    result_list = []

    for i in range(inp1):
        addition_list = [0] * inp1
        count = 0
        for j in range(i+1, inp1):
            count += 1
            addition_list[j] += count
        for k in range(0, i):
            count = count + 1
            addition_list[k] += count

        subtract = list(map(operator.sub, addition_list, times))
        result_list.append(sum(x > -1 for x in subtract))

    return result_list.index(max(result_list)) + 1
