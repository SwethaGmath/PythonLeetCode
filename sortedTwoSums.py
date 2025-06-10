def sorted_two_sum(nums, goal):
    # fill in
    res = list()
    sortednums = sorted(nums)
    for i in range(len(sortednums)):
      for j in range(i+1, len(sortednums)):
        if(sortednums[i]+sortednums[j] == goal):
            res.append(i)
            res.append(j)
        elif (sortednums[i]+sortednums[j] > goal):
            print("Not comparing with the rest elemns as they are already greater than the goal")
            continue
    return res

print(sorted_two_sum([1, 9, 13, 20, 47], 6))
print(sorted_two_sum([3, 6, 13, 14], 16) )
print(sorted_two_sum([1, 9, 13, 20, 47], 67))