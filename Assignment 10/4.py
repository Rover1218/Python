max_number = 50
prime_set = set()
for num in range(2, max_number + 1):
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        prime_set.add(num)
print(f"Prime numbers up to {max_number}:", prime_set)