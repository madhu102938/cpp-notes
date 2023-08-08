
## `std::pair` Container

`std::pair` is a container in C++ that stores a pair of values. It is commonly used to return two values from a function or to store two related values together.

### Declaration

```cpp
std::pair<type1, type2> myPair;
```

### Initialization

```cpp
std::pair<int, std::string> myPair = std::make_pair(1, "hello");
```

### Accessing Elements

```cpp
myPair.first;
myPair.second;
```

### Comparison

```cpp
myPair1 == myPair2;
myPair1 != myPair2;
myPair1 < myPair2;
myPair1 <= myPair2;
myPair1 > myPair2;
myPair1 >= myPair2;
```

### Swap

```cpp
std::swap(myPair1, myPair2);
```

### Performance

| Operation | Time Complexity |
|-----------|----------------|
| Access    | O(1)           |

### Notes

- `std::pair` stores a pair of values.
- `std::pair` provides functions for accessing the first and second values.
- `std::pair` provides functions for comparing pairs and swapping pairs.
- `std::pair` provides constant time complexity for accessing the first and second values.


```cpp
#include <iostream>
#include <utility>

int main()
{
    // Create a pair of integers
    std::pair<int, int> myPair = std::make_pair(1, 2);

    // Access the first and second elements of the pair
    std::cout << "First element: " << myPair.first << std::endl;
    std::cout << "Second element: " << myPair.second << std::endl;

    // Create a pair of a string and a double
    std::pair<std::string, double> myOtherPair("Hello", 3.14);

    // Access the first and second elements of the pair
    std::cout << "First element: " << myOtherPair.first << std::endl;
    std::cout << "Second element: " << myOtherPair.second << std::endl;

    // Swap the elements of two pairs
    std::pair<int, int> pair1 = std::make_pair(1, 2);
    std::pair<int, int> pair2 = std::make_pair(3, 4);
    std::swap(pair1, pair2);
    std::cout << "Pair 1: (" << pair1.first << ", " << pair1.second << ")" << std::endl;
    std::cout << "Pair 2: (" << pair2.first << ", " << pair2.second << ")" << std::endl;

    return 0;
}
```

This example code creates two pairs, one of integers and one of a string and a double. It then accesses the first and second elements of each pair and swaps the elements of two pairs.