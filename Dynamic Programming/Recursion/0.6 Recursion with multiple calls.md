### Fibonacci series
```cpp
#include <iostream>

int fibo(int a)
{
    if(a <= 1)
        return a;
    return fibo(a - 1) + fibo(a - 2);
}

int main()
{
    int a;
    std::cin >> a;
    std::cout << fibo(a);
    return 0;
}
```
***Time complexity** : $2^n$*