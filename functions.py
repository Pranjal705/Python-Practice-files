def say_hello(name='RAnbir Kapoor',emoji='  kaise ho'):
    print(f'hello {name}{emoji}')
#positional Argument
say_hello('Pranjal','__')

# keyword Argument
say_hello(emoji='__',name='Aditya')

say_hello()
li=[10,2,3,4,8,11]

#highest even
def highest_even(li):
    even=[]
    for item in li:
        if item%2==0:
            even.append(item)
    return max(even) 
            
        
        
    
    





print(highest_even([10,10,2,2,23,4,8,11]))
