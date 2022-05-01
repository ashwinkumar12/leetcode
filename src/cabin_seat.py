def get_seat_order(cabins, max_row):
    cabins_count = len(cabins)
 
    try:
#         import pdb;pdb.set_trace()
        for row in range(max_row):
            for cabin in range(cabins_count):
                if len(cabins[cabin]) > row:
                    print "Aisle: cabin {}, row {}".format(cabin, row)
 
        for row in range(max_row):
            if len(cabins[0]) > row:
                print "Window :: cabin {}, row {}".format(0, row)
 
            if len(cabins[-1]) > row:
                print "Window :: cabin {}, row {}".format(cabins_count, row)
         
        for row in range(max_row):
            for cabin in range(cabins_count):
                if len(cabins[cabin]) > row and len(cabins[cabin][row]) > 2:
                    for seat in range(1,len(cabins[cabin][row])-1):
                        print "Center :: cabss {}, ross {}".format(cabin, row)
 
    except Exception as e:
        print ""#traceback.format_exc(e)
 
if __name__ == '__main__':
    cabin_setup = [ [3,2], [4,3], [2,3], [3,4] ]
    cabin_setup = [[1,1], [3,2]]
    print cabin_setup
    ppl = 30
    cabins = []
    for cabin in cabin_setup:
        temp_cabin = []
        for row in range(cabin[1]):
            temp_cabin.append(['X' for seat in range(cabin[0])])
        cabins.append(temp_cabin)
    print cabins 
    max_row = max([i[1] for i in cabin_setup])
    get_seat_order(cabins, max_row)
