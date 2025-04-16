class Number:   
    def __init__(self,num,base):
        self.num = num
        self.base = base
        
    def base_change(self,new_base): 
        assert type(new_base) == int, "Base must be an integer"
        assert new_base > 1, "Base must be greater than 1"
        
        #decimal to another base
        if self.base == 10:
            quotient = int(self.num)
            remainder_list = []
        
            if quotient == 0:
                return "0"
            else:
                while quotient != 0:
                    remainder = quotient % new_base
                    if new_base == 16: 
                        if remainder == 10: remainder = 'A'
                        elif remainder == 11: remainder = 'B'
                        elif remainder == 12: remainder = 'C'
                        elif remainder == 13: remainder = 'D'
                        elif remainder == 14: remainder = 'E'
                        elif remainder == 15: remainder = 'F'
                    
                    remainder_list.append(remainder)
                    
                    quotient = quotient // new_base
                
                remainder_list.reverse()
                
                converted_num = ("".join(map(str,remainder_list)))
                
                if self.num == int(self.num):
                    return converted_num
                else: 
                    int_num = int(self.num)
                    dec_num = self.num - int_num
                    dec_num_list = []
                    
                    lenght = len(str(dec_num)) - 2
                    
                    for i in range(0,lenght):
                        int_dec_num = int(dec_num)
                        dec_num = dec_num - int_dec_num
                        
                        dec_num = dec_num * new_base
                        
                        dec_num_list.append(int(dec_num))
                    
                    dec_converted = ("".join(map(str,dec_num_list)))
                    
                    if converted_num == str: 
                        converted_num = converted_num + "."+ dec_converted
                    else: converted_num = "0."+ dec_converted
                    return converted_num
        #other systems to decimal
        if new_base == 10: 
            converted_num = float()
            number = str(self.num)
            
            
            if '.' in number:
                point_index = number.index('.')
                int_part = number[0:point_index]
                dec_part = number[point_index+1:len(number)]
                number = int_part + dec_part
                exponent = len(int_part)-1
            else: 
                exponent = len(number)-1
            
            
            for i in number:
                if i == 'A': i = 10
                elif i == 'B': i == 11
                elif i == 'C': i == 12
                elif i == 'D': i == 13
                elif i == 'E': i == 14
                elif i == 'F': i == 15
                converted_num += int(i) * (self.base ** exponent)
                
                exponent -= 1
            
            return converted_num

def addition(base,*number):
    assert len(number) > 0, "At least one number is required"
    assert type(base) == int, "Base must be an integer"
    assert base > 1, "Base must be greater than 1"

    result = 0
    
    for i in number:
        result += float(i.base_change(10))
    
    
    new_num = Number(result,10)
    return new_num.base_change(base)

def subtraction(base,*number):
    assert len(number) > 1, "At least two numbers are required"
    assert type(base) == int, "Base must be an integer"
    assert base > 1, "Base must be greater than 1"

    result = float(number[0].base_change(10))
    
    for i in number[1:]:
        result -= float(i.base_change(10))
    
    
    new_num = Number(result,10)
    return new_num.base_change(base)

def multiplication(base,*number):
    assert len(number) > 1, "At least two numbers are required"
    assert type(base) == int, "Base must be an integer"
    assert base > 1, "Base must be greater than 1"

    result = float(number[0].base_change(10))
    
    for i in number[1:]:
        result *= float(i.base_change(10))
    
    
    new_num = Number(result,10)
    return new_num.base_change(base)

def division(base,*number):
    assert len(number) > 1, "At least two numbers are required"
    assert type(base) == int, "Base must be an integer"
    assert base > 1, "Base must be greater than 1"
    assert number[1:] != 0, "You can divide by Zero" 

    result = float(number[0].base_change(10))
    
    for i in number[1:]:
        result /= float(i.base_change(10))
    
    new_num = Number(result,10)
    return new_num.base_change(base)

def main(): 
    #Here you can execute the calculator
    num1 = Number("1011",2)
    num2 = Number("11",2)
    
    print(division(2,num1,num2))

if __name__ == '__main__':
    main()
