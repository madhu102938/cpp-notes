### Sum of first N numbers
#### 1. Parameterized way
```c++
#include <iostream>

int sum(int a, int add = 0)
{
    if (a == 0)
        return add;
    return sum(a-1, add+a);
}

int main()
{
    int N;
    std::cin >> N;
    std::cout << sum(N);
    return 0;
}
```
`main() -> sum(4, 0) -> sum(3, 4) -> sum(2, 7) -> sum(1, 9) -> sum(0, 10) -> return 10 -> return 10 -> return 10 -> return 10 -> cout<<10`

#### 2. Functional way
```c++
#include <iostream>

int sum(int a)
{
    if (a == 0)
        return 0;
    return a + sum(a-1);
}

int main()
{
    int N;
    std::cin >> N;
    std::cout << sum(N);
    return 0;
}
```
`main() -> std::cin -> sum(4) -> 4+sum(3) -> 7+sum(2) -> 9+sum(1) -> 10+sum(0) -> return 10 -> return 10 -> return 10 -> return 10 -> cout<<10`

### Factorial using recursion
```cpp
#include <iostream>

int fact(int a)
{
    if (a <= 1)
        return 1;
    return a * fact(a-1);
}

int main()
{
    int N;
    std::cin >> N;
    std::cout << fact(N);
    return 0;
}
```