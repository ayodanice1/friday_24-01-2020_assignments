def find_max(*nums) :
    res = nums[0]
    for num in nums :
        if num > res :
            res = num
    return res


if __name__ == '__main__' :
    print(find_max(1,2,3,4))