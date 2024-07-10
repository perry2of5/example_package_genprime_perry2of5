found_primes = [2, 3]


def candidates(last_tested=3):
    min_prime = last_tested + 2
    return [x for x in range(min_prime, min_prime + 20, 2)]


def generate_primes(last_tested, num=10):
    found = len(found_primes)
    num_tested = 0
    while found < num and num_tested < 10000:
        for candidate in candidates(last_tested):
            num_tested += 1
            last_tested = candidate
            factored = False
            for prime in found_primes:
                if prime >= 3 and candidate % prime == 0:
                    # print("not prime:", candidate, "(", prime, ")")
                    factored = True
                    break
            if factored == False:
                found_primes.append(candidate)
                # print("found prime", found, ":", candidate)
                found += 1
    return last_tested


if __name__ == '__main__':
    generate_primes(3, num=25)

print("loaded primes.py *******************************************")
