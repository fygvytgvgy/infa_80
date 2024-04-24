from collections import Counter
sample_counter = Counter({'Math': 81, 'Physics': 83, 'Chemistry': 87})
sorted_counter = sorted(sample_counter.items(), key=lambda x: x[1], reverse=True)
print("Sorted Counter by value:", sorted_counter)
