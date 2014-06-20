f = open('problem18.txt','r')

nums = []
lines = f.readlines()
for line in lines :
    l = line.replace('\n','').split(' ',-1)
    l = [int(item) for item in l]
    nums += [l]

for i in range(len(nums)-2,-1,-1) :
    for j in range(i+1) :
        nums[i][j] += max(nums[i+1][j],nums[i+1][j+1])
print(nums[0][0])
        


