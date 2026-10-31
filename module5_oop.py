class Numbers:
    def __init__(self):
        self.data = []

    def insert(self, num):
        self.data.append(num)

    def search(self, x):
        if x in self.data:
            return self.data.index(x) + 1
        return -1


n = int(input("Enter N: "))
nums = Numbers()

for i in range(n):
    nums.insert(int(input("Enter a number: ")))

x = int(input("Enter X: "))
print(nums.search(x))
