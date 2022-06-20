#include <iostream>
#include <vector>
#include <limits>


namespace console
{
    template<typename T>
    const static void log(T msg)
    {
        std::cout << msg << std::endl;
    }
}


void divmod(long long& n, int& d, int& r, int& m)
{
    r = n / d;
    m = n % d;
}

int max(std::vector<int> ls)
{
    int largest = -std::numeric_limits<int>::infinity();
    for (int i = 0; i < ls.size(); i++)
    {
        if (ls[i] > largest)
        {
            largest = ls[i];
        }
    }
    return largest;
}

std::vector<int> find_prime_factors(long long n)
{
    std::vector<int> number_factors = {};
    int i = 1;
    int div = 0;
    int mod = 0;

    while (n != 1)
    {
        divmod(n, i, div, mod);

        if (mod == 0)
        {
            number_factors.push_back(i);
            n = div;
        }
        i++;
    }
    return number_factors;
}


int main()
{
    auto prime_numbers = find_prime_factors(600851475143);
    console::log(max(prime_numbers)); 
    return 0;
}
