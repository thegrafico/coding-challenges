def reverse_integer(x:int) ->int:
    
    bigger_int = 2**31 -1
    print(bigger_int)
    x = str(x)
    
    try:
        isNumber = int(x[0])
        isNumber = True
    except:
        isNumber = False
    
    if isNumber:
        x = int(x[::-1])
        return x if abs(x) < bigger_int else 0
    else:
        x = x[1:]
        x = - int(x[::-1])
        return x if abs(x) < bigger_int  else 0
     
if __name__ == "__main__":
    test = 1534236469
    result = reverse_integer(test)
    
    print("{} <==> {}".format(result, test))