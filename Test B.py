    a = 100 # G1
    b = 200 # G2

    def func_A():
        a = 10 # L1  
        b = 20 # L1
        print(f"In func_A: a = {a}") # Print 1    
        print(f"In func_A: b = {b}") # Print 2     

    def func_B():
        global b # G2
        a = 30 # L2
        b = 40 # G2 (被修改了)
        print(f"In func_B: a = {a}") # Print 3     
        print(f"In func_B: b = {b}") # Print 4     

    def func_C():
        c = 50 # E1
        def inner_C():
            print(f"In inner_C: a = {a}") # Print 5 (a 在哪里？) 
            print(f"In inner_C: c = {c}") # Print 6 (c 在哪里？)    
        inner_C()
    
    # --- 主程序执行 ---
    print(f"Global: a = {a}") # Print 7    #a =100  
    print(f"Global: b = {b}") # Print 8    #b = 200

    func_A()

    print(f"Global: a = {a}") # Print 9    #error
    print(f"Global: b = {b}") # Print 10   #error

    func_B()

    print(f"Global: a = {a}") # Print 11   #error
    print(f"Global: b = {b}") # Print 12   #b = 40
    
    func_C()  #error #c =50
