# for i in range(1,11):
#     for ii in range(1,6):
#         print(f"{i} x {ii} = {i*ii}")

# for i in range (2,21):
#     is_prime = True
#     for j in range(2, int(i**0.5) + 1):
#         if i % j == 0:
#             is_prime = False
#             break
#     if is_prime:
#         print(f"{i} is a prime number.")
#     else:
#         print(f"{i} is not a prime number.")

for i in range (2,21):
    prime_num = True
    for ii in range (2,i):
        if i % ii == 0:
            prime_num = False
            break
    if prime_num:
            print(f"{i} is a PRIME NUMBER.")
    # else:
    #         print(f"{i} is NOT a PRIME NUMBER.")
