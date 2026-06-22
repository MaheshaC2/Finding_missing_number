# Remove Duplicates from a List (Maintain Order)
nums = list(map(int, input("Enter numbers separated by space: ").split()))

unique_nums = []

for num in nums:
    if num not in unique_nums:
        unique_nums.append(num)

print("List after removing duplicates:", unique_nums)
