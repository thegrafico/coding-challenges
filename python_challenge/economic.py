import math

def annual_worth_analysis(data:list, interest:float, down:int) -> int:
    rate = (1 + interest/100)
    result = 0
    for index,number in enumerate(data):
        result += number * math.pow(rate, - (index+1) )
        # print("{} * {} = {}".format(number, math.pow(rate, - (index+1)), result ))
    
    result = result - down
    print("PRESENT VALUE:", result)
    divisor =  math.pow(rate, len(data)) 
    A = result * ( (interest/100 * divisor) / (divisor - 1) )
    print("A = {} * ({} / {})".format(result,rate*divisor, divisor-1 ))
    return A


if __name__ == "__main__":
    up = [100,140,180,220,200,200]
    down = 300
    interest = 15
    annual_worth = annual_worth_analysis(up, interest, down)
    
    print("A = {:.2f}".format(annual_worth))