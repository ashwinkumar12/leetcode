from copy import deepcopy
from pprint import pprint

if __name__ == '__main__':
    num = 10
    partitions = {}
    if num==1:
        print 1
    else:
        for i in range(num, 1, -1):
            partitions[i] = [[1,i-1]]
        print "#########"
        print partitions
        print "#########"

        for key in partitions.keys():
            if partitions.get(key-1):
                for val in partitions[key-1]:
                    new_list = deepcopy(partitions[key][0])
                    new_list.pop(-1)
                    new_list.extend(val)
                    partitions[key].append(sorted(new_list))
                    
                    count = new_list.count(1)
                    if count!=key:
                        sum_list = sorted([sum(new_list)-count, count])
                        if not sum_list in partitions[key]:
                            partitions[key].append(sum_list)
                        
                        ext_list = filter(lambda x: x!=1, new_list)
                        if len(ext_list)  > 1:
                            ext_list.append(count)
                            ext_list.sort()
                            if not ext_list in partitions[key]:
                                partitions[key].append(ext_list)
                
        pprint(partitions)
        product = max([reduce((lambda x,y: x*y), lis) for lis in partitions[num]])
        print product
    