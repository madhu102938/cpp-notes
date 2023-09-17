### Reversing an array using recursion
```c++
#include <iostream>
#include <vector>
void swapp(int &a, int &b);

int reverse(std::vector<int> &a, int l, int r)
{
    if(l >= r)
        return 0;
    swapp(a[l], a[r]);
    return reverse(a, l + 1, r - 1);
}

void swapp(int &a, int &b)
{
    int temp = a;
    a = b;
    b = temp;
}

int main()
{
    std::vector<int> v = {1, 2, 3, 4, 5};
    reverse(v, 0, v.size() - 1);
    for(auto i : v)
        std::cout << i << " ";
    return 0;
}
```
without using `l` and `r`, we can just use single variable, we can swap till N/2 and then stop there.
#### using only 1 parameter
```c++
#include <iostream>
#include <vector>
void swapp(int &a, int &b);

int reverse(std::vector<int> &a, int l)
{
    if(l > a.size() / 2)
        return 0;
    swapp(a[l], a[a.size() - 1 - l]);
    return reverse(a, l + 1);
}

void swapp(int &a, int &b)
{
    int temp = a;
    a = b;
    b = temp;
}

int main()
{
    std::vector<int> v = {1, 2, 3, 4, 5};
    reverse(v, 0);
    for(auto i : v)
        std::cout << i << " ";
    return 0;
}
```

### Checking whether a string is palindrome or not
```cpp
#include <iostream>
#include <string>

bool palindrome(std::string s, int l = 0)
{
    if(l > s.size() / 2)
        return true;
    if(s[l] == s[s.size() - 1 - l])
        return palindrome(s, l + 1);
    else
        return false;
}

int main()
{
    std::string S = "asdsaa";
    std::cout << palindrome(S);
    return 0;
}
```