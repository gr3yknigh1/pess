import argparse


def find_number_factor(n: int) -> list[int]:
    number_factors: list[int] = []
    i: int = 1
    while n != 1:
        div, mod = divmod(n, i)
        # print(i, n, div, mod)
        if mod == 0 and i != 1:
            number_factors.append(i)
            n = div
        i += 1
    return number_factors


def main() -> int:

    parser = argparse.ArgumentParser()
    parser.add_argument("number", type=int)
    args = parser.parse_args()

    prime_numbers = find_number_factor(args.number)
    # print(prime_numbers)

    print(f"Answer: {max(prime_numbers)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
