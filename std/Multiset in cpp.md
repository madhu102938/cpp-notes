
## `std::multiset` Container

`std::multiset` is a container in C++ that stores elements in a sorted order. It is similar to `std::set`, but allows duplicate elements.

### Declaration

```cpp
std::multiset<type> myMultiset;
```

### Initialization

```cpp
std::multiset<int> myMultiset;
```

### Insertion

```cpp
myMultiset.insert(value);
```

### Deletion

```cpp
myMultiset.erase(value);
```

### Size

```cpp
myMultiset.size();
```

### Accessing Elements

```cpp
myMultiset.find(value);
myMultiset.count(value);
```

### Clearing the Multiset

```cpp
myMultiset.clear();
```

### Checking if the Multiset is Empty

```cpp
myMultiset.empty();
```

### Comparison

```cpp
myMultiset1 == myMultiset2;
myMultiset1 != myMultiset2;
```

### Swap

```cpp
std::swap(myMultiset1, myMultiset2);
```

### Performance

| Operation | Time Complexity |
|-----------|----------------|
| Insertion | O(log n)       |
| Deletion  | O(log n)       |
| Access    | O(log n)       |
| Search    | O(log n)       |

### Notes

- `std::multiset` stores elements in a sorted order.
- `std::multiset` allows duplicate elements.
- `std::multiset` provides faster search times for elements compared to `std::vector`.
- `std::multiset` provides slower insertion and deletion times compared to `std::vector`.
- `std::multiset` provides functions for inserting and deleting elements.
- `std::multiset` provides functions for accessing the size and checking if the multiset is empty.
- `std::multiset` provides functions for finding and counting elements.
- `std::multiset` provides functions for comparing multisets and swapping multisets.

Here is an example of how to use `std::multiset`:

```cpp
#include <iostream>
#include <set>

int main()
{
    std::multiset<int> myMultiset;

    // Insert elements into the multiset
    myMultiset.insert(5);
    myMultiset.insert(3);
    myMultiset.insert(7);
    myMultiset.insert(3);

    // Iterate over the elements in the multiset
    for (auto it = myMultiset.begin(); it != myMultiset.end(); ++it)
    {
        std::cout << *it << " ";
    }
    std::cout << std::endl;

    // Find an element in the multiset
    auto it = myMultiset.find(3);
    if (it != myMultiset.end())
    {
        std::cout << "Found element: " << *it << std::endl;
    }
    else
    {
        std::cout << "Element not found." << std::endl;
    }

    // Count the number of occurrences of an element in the multiset
    int count = myMultiset.count(3);
    std::cout << "Number of occurrences of 3: " << count << std::endl;

    // Delete an element from the multiset
    myMultiset.erase(3);

    // Check if the multiset is empty
    if (myMultiset.empty())
    {
        std::cout << "The multiset is empty." << std::endl;
    }
    else
    {
        std::cout << "The multiset is not empty." << std::endl;
    }

    return 0;
}
```

This example creates a `std::multiset` of integers, inserts some elements into it, iterates over the elements, finds an element, counts the number of occurrences of an element, deletes an element, and checks if the multiset is empty.

I hope you find this cheat sheet helpful! Let me know if you have any further questions.