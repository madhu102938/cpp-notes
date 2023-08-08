
## `std::map` Container

`std::map` is a container in C++ that stores key-value pairs in a sorted order based on the keys. It is implemented as a balanced binary search tree, which provides logarithmic time complexity for most operations.

### Declaration

```cpp
std::map<key_type, value_type> myMap;
```

### Initialization

```cpp
std::map<std::string, int> myMap = {{"apple", 1}, {"banana", 2}, {"orange", 3}};
```

### Insertion

```cpp
myMap.insert(std::make_pair(key, value));
myMap.insert(std::pair<key_type, value_type>(key, value));
myMap[key] = value;
```

### Deletion

```cpp
myMap.erase(key);
```

### Size

```cpp
myMap.size();
```

### Iteration

```cpp
for (auto it = myMap.begin(); it != myMap.end(); ++it)
{
    // do something with it->first and it->second
}
```

### Reverse Iteration

```cpp
for (auto it = myMap.rbegin(); it != myMap.rend(); ++it)
{
    // do something with it->first and it->second
}
```

### Accessing Elements

```cpp
auto it = myMap.find(key);
if (it != myMap.end())
{
    // key found, value is it->second
}
```

### Counting Elements

```cpp
myMap.count(key);
```

### Clearing the Map

```cpp
myMap.clear();
```

### Checking if the Map is Empty

```cpp
myMap.empty();
```

### Lower Bound

```cpp
auto it = myMap.lower_bound(key);
if (it != myMap.end())
{
    // key found, value is it->second
}
```

### Upper Bound

```cpp
auto it = myMap.upper_bound(key);
if (it != myMap.end())
{
    // key found, value is it->second
}
```

### Equal Range

```cpp
auto range = myMap.equal_range(key);
for (auto it = range.first; it != range.second; ++it)
{
    // do something with it->first and it->second
}
```

### Comparison

```cpp
myMap1 == myMap2;
myMap1 != myMap2;
myMap1 < myMap2;
myMap1 <= myMap2;
myMap1 > myMap2;
myMap1 >= myMap2;
```

### Swap

```cpp
myMap1.swap(myMap2);
```

### Performance

| Operation | Time Complexity |
|-----------|----------------|
| Insertion | O(log n)        |
| Deletion  | O(log n)        |
| Access    | O(log n)        |
| Search    | O(log n)        |

### Notes

- `std::map` stores key-value pairs in a sorted order based on the keys.
- `std::map` is implemented as a balanced binary search tree.
- `std::map` provides logarithmic time complexity for most operations.
- `std::map` does not allow duplicate keys.
- `std::map` provides iterators that allow traversal of the elements in sorted order.
- `std::map` provides functions for finding elements, counting elements, and accessing elements.
- `std::map` provides functions for inserting and deleting elements.
- `std::map` provides functions for clearing the map and checking if the map is empty.
- `std::map` provides functions for finding the lower bound, upper bound, and equal range of a key.
- `std::map` provides functions for comparing maps and swapping maps.

I hope you find this cheat sheet helpful! Let me know if you have any further questions.