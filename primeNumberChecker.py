def is_prime(num):
    prime = True
    for i in range(2,num//2+1):
        
        if num %i == 0 and i != num:
               prime = False
    if prime:
            return  True
    return False
