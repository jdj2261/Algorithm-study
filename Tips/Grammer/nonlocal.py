def func1():
    n = 1 
    def func2():
        nonlocal n
        n += 1
        print(n) # 2
    func2()
    
func1()

# def func1():
# 	n = 1
#     def func2():
#         global n
#         n += 1
#         print(n) # error
#     func2()
    
# func1()