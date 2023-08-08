
## `std::list` Container

`std::list` is a container in C++ that stores elements in a linked list. It provides constant time complexity for insertion and deletion at any position, but linear time complexity for accessing elements.

### Declaration

```cpp
std::list<type> myList;
```

### Initialization

```cpp
std::list<int> myList = {1, 2, 3, 4, 5};
```

### Insertion

```cpp
myList.insert(position, value);
myList.insert(position, count, value);
myList.push_front(value);
myList.push_back(value);
```

### Deletion

```cpp
myList.erase(position);
myList.pop_front();
myList.pop_back();
```

### Size

```cpp
myList.size();
```

### Iteration

```cpp
for (auto it = myList.begin(); it != myList.end(); ++it)
{
    // do something with *it
}
```

### Reverse Iteration

```cpp
for (auto it = myList.rbegin(); it != myList.rend(); ++it)
{
    // do something with *it
}
```

### Accessing Elements

```cpp
myList.front();
myList.back();
```

### Clearing the List

```cpp
myList.clear();
```

### Checking if the List is Empty

```cpp
myList.empty();
```

### Sorting the List

```cpp
myList.sort();
myList.sort(compare_function);
```

### Splicing the List

```cpp
myList.splice(position, otherList);
myList.splice(position, otherList, otherPosition);
myList.splice(position, otherList, first, last);
```

### Removing Elements

```cpp
myList.remove(value);
myList.remove_if(predicate_function);
```

### Reversing the List

```cpp
myList.reverse();
```

### Unique Elements

```cpp
myList.unique();
myList.unique(compare_function);
```

### Comparison

```cpp
myList1 == myList2;
myList1 != myList2;
```

### Swap

```cpp
myList1.swap(myList2);
```

### Performance

| Operation | Time Complexity |
|-----------|----------------|
| Insertion | O(1)           |
| Deletion  | O(1)           |
| Access    | O(n)           |
| Search    | O(n)           |

### Notes

- `std::list` stores elements in a linked list.
- `std::list` provides constant time complexity for insertion and deletion at any position.
- `std::list` provides linear time complexity for accessing elements.
- `std::list` provides iterators that allow traversal of the elements in order.
- `std::list` provides functions for inserting and deleting elements.
- `std::list` provides functions for clearing the list and checking if the list is empty.
- `std::list` provides functions for sorting the list, splicing the list, removing elements, and reversing the list.
- `std::list` provides functions for finding unique elements.
- `std::list` provides functions for comparing lists and swapping lists.

I hope you find this cheat sheet helpful! Let me know if you have any further questions.