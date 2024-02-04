chs = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
guess = [0]

while True:
    print(''.join(chs[i] for i in guess))
    result = input()
    if result == 'ACCESS GRANTED':
        break
    
    t = int(result.split()[2][1:])
    # minimally, it takes 1ms (if) + 3ms (!=) + 1ms (return) = 5ms
    # for the algorithm to indicate wrong password length
    if t == 5:
        guess.append(0)
    
    # minimally, it takes 1ms (if) + 3ms (!=) +
    #                     1ms (for) + 1ms (i = 0) + 1ms (return) = 7ms
    # to initialise the for loop and return false
    # additionally, it takes 3ms (<) + 1ms (if) + 3ms (!=) = 7ms
    # each iteration of the for loop to check each pair of characters
    # additionally, it takes 1ms (for) + 1ms (i++) = 2ms
    # each other iteration of the for loop to update the i variable
    else:
        guess[(t - 14) // 9] += 1
