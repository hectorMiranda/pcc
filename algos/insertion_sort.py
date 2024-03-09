def insertion_sort(numbers):
    for i in range(1, len(numbers)):
        j = i

        # Insert numbers[i] into sorted part 
        # stopping once numbers[i] in correct position
        while j > 0 and numbers[j] < numbers[j - 1]:
            # Swap numbers[j] and numbers[j - 1]
            temp = numbers[j]
            numbers[j] = numbers[j - 1]
            numbers[j - 1] = temp
            j -= 1
    
# Create a list of unsorted values    
numbers = [10, 2, 78, 4, 45, 32, 7, 11]

# Print unsorted list
print('UNSORTED:', numbers)

# Initial call to insertion_sort with index 
insertion_sort(numbers)

# Print sorted list
print('SORTED:', numbers)
