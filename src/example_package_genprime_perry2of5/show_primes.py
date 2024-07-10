from example_package_genprime_perry2of5.primes import generate_primes
from example_package_genprime_perry2of5.primes import found_primes


if __name__ == '__main__':
    generate_primes(3, num=1000)

    for p in found_primes:
        print("   ", p)
    print(sorted(found_primes))
    print("Found ", len(found_primes), " primes.")
