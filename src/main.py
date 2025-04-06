def main(): 
    
    class Number:
        
        def __init__(self,num,base):
            self.num = num
            self.base = base
        
        def base_change(self,new_base): 
            
            #decimal to another base
            if self.base == 10:
                quotient = int(self.num)
                remainder_list = []
                
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
                
                if type(self.num) == float:
                    int_num = int(self.num)
                    dec_num = self.num - int_num
                    dec_num_list = []
                    
                    lenght = len(str(dec_num))
                    lenght -= 2
                    
                    
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
                else: return converted_num

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
                    elif 1 == 'C': i == 12
                    elif 1 == 'D': i == 13
                    elif 1 == 'E': i == 14
                    elif 1 == 'F': i == 15
                    converted_num += int(i) * (self.base ** exponent)
                    
                    exponent -= 1
                
                return converted_num
    
    def addition(base,*number):
        result = 0
        
        for i in number:
            result += float(i.base_change(10))
        
        
        new_num = Number(result,10)
        print(new_num.num)
        return new_num.base_change(base)


if __name__ == '__main__':
    main()
