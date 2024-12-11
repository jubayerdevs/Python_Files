x = 6
def sample():
    try:
        if x % 2 == 0:
            raise Exception("NOT ALLOWED")
            print(x)
            # print("NOT ALLOWED")
            # return
            # 
            #     #
        #
        #
        # raise Exception("I will not allow even numbers!")
        
    except Exception as e:
        print(e)