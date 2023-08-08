
## `std::set` Container

`std::set` is a container in C++ that stores unique elements in a sorted order. It is implemented as a balanced binary search tree, which provides logarithmic time complexity for most operations.

### Declaration

```cpp
std::set<type> mySet;
```

### Initialization

```cpp
std::set<int> mySet = {1, 2, 3, 4, 5};
```

### Insertion

```cpp
mySet.insert(value);
```

### Deletion

```cpp
mySet.erase(value);
```

### Size

```cpp
mySet.size();
```

### Iteration

```cpp
for (auto it = mySet.begin(); it != mySet.end(); ++it)
{
    // do something with *it
}
```

### Reverse Iteration

```cpp
for (auto it = mySet.rbegin(); it != mySet.rend(); ++it)
{
    // do something with *it
}
```

### Accessing Elements

```cpp
auto it = mySet.find(value);
if (it != mySet.end())
{
    // value found
}
```

### Counting Elements

```cpp
mySet.count(value);
```

### Clearing the Set

```cpp
mySet.clear();
```

### Checking if the Set is Empty

```cpp
mySet.empty();
```

### Lower Bound

```cpp
auto it = mySet.lower_bound(value);
if (it != mySet.end())
{
    // value found
}
```

### Upper Bound

```cpp
auto it = mySet.upper_bound(value);
if (it != mySet.end())
{
    // value found
}
```

### Equal Range

```cpp
auto range = mySet.equal_range(value);
for (auto it = range.first; it != range.second; ++it)
{
    // do something with *it
}
```

### Comparison

```cpp
mySet1 == mySet2;
mySet1 != mySet2;
mySet1 < mySet2;
mySet1 <= mySet2;
mySet1 > mySet2;
mySet1 >= mySet2;
```

### Swap

```cpp
mySet1.swap(mySet2);
```

### Performance

| Operation | Time Complexity |
|-----------|----------------|
| Insertion | O(log n)        |
| Deletion  | O(log n)        |
| Access    | O(log n)        |
| Search    | O(log n)        |

### Notes

- `std::set` stores unique elements in a sorted order.
- `std::set` is implemented as a balanced binary search tree.
- `std::set` provides logarithmic time complexity for most operations.
- `std::set` does not allow duplicate elements.
- `std::set` does not allow modification of elements once they are inserted.
- `std::set` provides iterators that allow traversal of the elements in sorted order.
- `std::set` provides functions for finding elements, counting elements, and accessing elements.
- `std::set` provides functions for inserting and deleting elements.
- `std::set` provides functions for clearing the set and checking if the set is empty.
- `std::set` provides functions for finding the lower bound, upper bound, and equal range of a value.
- `std::set` provides functions for comparing sets and swapping sets.

I hope you find this cheat sheet helpful! Let me know if you have any further questions.