def main(): 
    
    class Number:
        
        def __init__(self,num,base):
            self.num = num
            self.base = base
        
        def base_change(self,new_base): 
            
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
                
                return converted_num
    
    
    





if __name__ == '__main__':
    main()
