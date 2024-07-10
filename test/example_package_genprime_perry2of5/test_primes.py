from math import floor
from example_package_genprime_perry2of5.primes import generate_primes
from example_package_genprime_perry2of5.primes import found_primes
from test.example_package_genprime_perry2of5.known_primes import first_1000_primes
from test.example_package_genprime_perry2of5.known_primes import primes_under_100

debugging = False


def test_primes_under_100():
    generate_primes(3, 100)
    generated_primes_under_100 = sorted(set(range(1, 100)) & set(found_primes))
    print("actual", sorted(primes_under_100))
    print("found:", sorted(generated_primes_under_100))
    assert primes_under_100 == generated_primes_under_100


def test_primes_under_1000():
    generate_primes(3, 1000)
    generated_first_1000_primes = found_primes[0:1000:]
    if debugging:
        batch_size = 20
        for i in range(0, floor(1000/batch_size)):
            gens = generated_first_1000_primes[
                batch_size * i: batch_size * (i + 1):]
            known = first_1000_primes[batch_size * i: batch_size * (i + 1):]
            print("comparing ", batch_size * i, "to", batch_size * (i + 1) - 1)
            print("known:    ", known)
            print("generated:", gens)
            print()
            assert known == gens
    else:
        assert first_1000_primes == generated_first_1000_primes
