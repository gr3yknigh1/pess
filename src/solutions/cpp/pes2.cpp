#include <iostream>
#include <cmath>


namespace fib
{
    double sqrt_from_5 = sqrt(5); 
    const float Phin = (1 + sqrt_from_5) / 2; 
    const float phin = (1 - sqrt_from_5) / 2;

    inline int compute(int n)
    {
        return (pow(Phin, n) - pow(phin, n)) / sqrt_from_5;  // WTF: when n=33 calcs it's failed
    }
}


bool is_even(int n)
{
    return n % 2 == 0;
}


int main()
{
    const int FIB_VAL_TRESHOLD = 4000000;
    int fib_sum = 0;
    int n = 0;
    while (true)
    {
        int fib_n = fib::compute(n);
        if (fib_n > FIB_VAL_TRESHOLD)
        {
            break;
        } 
        if (is_even(fib_n))
        {
            std::cout << "+[" << n << "] " << fib_n << std::endl;
            fib_sum += fib_n;
        }
        else
        {
            std::cout << "-[" << n << "] " << fib_n << std::endl;
        }
        n++;
    }
    std::cout << "Even fib sum: " << fib_sum << std::endl;
    return 0;
}