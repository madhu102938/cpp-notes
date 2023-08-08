In C++, passing a variable by reference allows you to modify the original variable directly, rather than creating a copy of the variable. This is different from C, where passing a variable by reference is not possible.

In C, you can pass a pointer to a variable to a function, which allows you to modify the original variable indirectly. However, this requires you to use pointer syntax to access the variable inside the function, which can be more cumbersome than using reference syntax in C++.

Here's an example of how you could pass a variable by reference in C++ and modify it directly:

```cpp
#include <iostream>

void increment(int& x)
{
    x++;
}

int main()
{
    int a = 5;
    increment(a);
    std::cout << a << std::endl; // prints 6
    return 0;
}
```

In this example, the `increment()` function takes an integer reference `x` and modifies it directly by incrementing it. The `main()` function calls the `increment()` function on the integer `a`, which modifies `a` directly. Finally, the `main()` function prints the value of `a` using `std::cout`.

Here's an example of how you could pass a variable by pointer in C and modify it indirectly:

```c
#include <stdio.h>

void increment(int* x)
{
    (*x)++;
}

int main()
{
    int a = 5;
    increment(&a);
    printf("%d\n", a); // prints 6
    return 0;
}
```

In this example, the `increment()` function takes an integer pointer `x` and modifies the value of the integer indirectly by dereferencing the pointer and incrementing the value. The `main()` function calls the `increment()` function on the address of the integer `a`, which modifies `a` indirectly. Finally, the `main()` function prints the value of `a` using `printf()`.

I hope this helps! Let me know if you have any further questions.