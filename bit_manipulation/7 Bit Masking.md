**We need to design a Set data structure, where we add, remove and print element in it**
Set data structure stores elements in ascending order
`long long int s = 0` means that there are 64 bits from 0 to 63 all set to 0
So we can insert numbers into this by masking
- Inserting 5
`s ^ (1 << 5)`
the value of s will become 32, but we have 5th bit (in binary) set to 5
- Removing 5
`s | ~(1 << 5)`
we are clearing 5th bit
- Printing all bits
```cpp
for (int i = 0; i < 64; i++)
{
	if (s & (1 << i))
		cout << i + 1;
}
```


```cpp
#include <bits/stdc++.h>
using namespace std;

class Set
{
public:
    long long int k;
    Set(long long int s = 0)
    {
        k = s;
    }
    
    void insert(int n)
    {
        k = k | (1LL << n);
    }

    void remove(int n)
    {
        k = k & ~(1LL << n); // Here we are using long long 1, which has 64 bits
    }

    void print()
    {
        for (int i = 0; i < 64; i++)
        {
            if (k & (1LL << i))
                cout << i << " ";
        }
    }
};

int main()
{
    Set ob;
    ob.insert(1);
    ob.insert(5);
    ob.insert(63);
    ob.remove(63);
    ob.remove(30);
    ob.print();
    return 0;
}
```


# A brief on Bit Masking
Bit masking is a technique used in computer programming to manipulate individual bits of a binary number. It involves using bitwise operators, such as AND (`&`), OR (`|`), XOR (`^`), NOT (`~`), and left shift (`<<`) and right shift (`>>`) operators, to set, clear, or toggle specific bits in a binary number.

For example, in the `Set` class provided, the `insert()` and `remove()` functions use bit masking to set or clear individual bits in the `k` member variable. The `print()` function also uses bit masking to print the indices of the bits that are set to 1 in the `k` variable.