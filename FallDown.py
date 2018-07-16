class FallDownException(Exception):
    def __str__(self):
        return "在 80 樓被接住了！"

class FallDownStrongerException(Exception):
    def __str__(self):
        return "在 5 樓被接住了！"

def slip(floor):
    try:
        while floor:
            floor -= 1
            print("現在在 {} 樓".format(floor))

            if floor == 80:
                raise FallDownException
                
    except FallDownException as e:
        print(e)
        print("突破機關！")
        while floor:
            floor -= 1
            print("現在在 {} 樓".format(floor))
            
            if floor == 5:
                raise FallDownStrongerException
     
try:
    slip(106)
except:
    print("接住但死了!!")