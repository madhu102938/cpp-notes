### Print name N times using recursion
```c++
#include <iostream>

void hello(int a, int i = 0)
{
    if (i == a)
        return;
    std::cout << "Madhu" << '\n';
    hello(a, ++i);
}

int main()
{
    int a;
    std::cin >> a;
    hello(a);
    return 0;
}
```
***Time Complexity** - Since there are N function calls being made so it is O(n)
**Space Complexity** - There is no space being consumed, but the function calls need to wait in the stack for the last function to return, thus space complexity is the depth of the tree which is O(n)*

### Print linearly from 1 to N
```c++
#include <iostream>

void hello(int a, int i = 1)
{
    if (i == a)
        return;
    std::cout << i << '\n';
    hello(a, ++i);
}

int main()
{
    int a;
    std::cin >> a;
    hello(a);
    return 0;
}
```

### Print from N to 1
```c++
#include <iostream>

void hello(int i, int a = 1)
{
    if (i < a)
        return;
    std::cout << i << '\n';
    hello(i-1, a);
}

int main()
{
    int N;
    std::cin >> N;
    hello(N);
    return 0;
}
```

### Printing from 1 to N using back tracking
```c++
#include <iostream>

void hello(int i, int a = 1)
{
    if (i < a)
        return;
    hello(i-1, a);
    std::cout << i << '\n';
}

int main()
{
    int i;
    std::cin >> i;
    hello(i);
    return 0;
}
```
`main() -> hello(4) -> hello(3) -> hello(2) -> hello(1) -> hello(0) -> std::cout<<1 -> std::cout<<2 -> std::cout<<3 -> std::cout<<4 -> return`

### Printing from N to 1 using back tracking
```c++
#include <iostream>

void hello(int a, int i = 1)
{
    if (a < i)
        return;
    hello(a, i+1);
    std::cout << i << '\n';
}

int main()
{
    int N;
    std::cin >> N;
    hello(N);
    return 0;
}
```
`main() -> hello(4) -> hello(4, 2) -> hello(4, 3) -> hello(4, 4) -> hello(4, 5) -> std::cout<<4 -> std::cout<<3 -> std::cout<<2 -> std::cout<<1 -> return`