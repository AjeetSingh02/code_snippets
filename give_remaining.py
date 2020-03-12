def give_remaining(s):
    s = sorted(s, reverse=True)
    ini_sum = sum(s)
    temp = []

    for ele in s:
        if ele not in temp:
            small = ele - 1 
            big = ele + 1

            if small in s and small not in temp:
                ini_sum -= small
                temp.append(small)

            if big in s and big not in temp:
                ini_sum -= big
                temp.append(big)

    return ini_sum
    
    
inp1 = "8 7 9 10 3"
s = list(map(int, inp1.split(" ")))

give_remaining(s)
