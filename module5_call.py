from module5_mod import Numbers

n = int(input("Enter N: "))
nums = Numbers()

for i in range(n):
    nums.insert(int(input("Enter a number: ")))

x = int(input("Enter X: "))
print(nums.search(x))
