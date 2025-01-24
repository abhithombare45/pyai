def calculate_mean(numbers):
    total = sum(numbers)
    count = len(numbers)
    mean = total / count
    return mean


data = [10, 20, 30, 40, 50]
result = calculate_mean(data)
print("Mean:", result)
