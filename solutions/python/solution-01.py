from __future__ import annotations


def main() -> int:

    res = []
    for i in range(1, 1000):
        if i % 3 == 0 or i % 5 == 0:
            res.append(i)

    print(f"Answer: {sum(res)}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
