
## `std::stack` Container

`std::stack` is a container in C++ that stores elements in a last-in, first-out (LIFO) order. It provides constant time complexity for insertion and deletion at the top of the stack, but linear time complexity for accessing elements at other positions.

### Declaration

```cpp
std::stack<type> myStack;
```

### Initialization

```cpp
std::stack<int> myStack;
```

### Insertion

```cpp
myStack.push(value);
```

### Deletion

```cpp
myStack.pop();
```

### Size

```cpp
myStack.size();
```

### Accessing Elements

```cpp
myStack.top();
```

### Clearing the Stack

```cpp
while (!myStack.empty())
{
    myStack.pop();
}
```

### Checking if the Stack is Empty

```cpp
myStack.empty();
```

### Comparison

```cpp
myStack1 == myStack2;
myStack1 != myStack2;
```

### Swap

```cpp
std::swap(myStack1, myStack2);
```

### Performance

| Operation | Time Complexity |
|-----------|----------------|
| Insertion | O(1)           |
| Deletion  | O(1)           |
| Access    | O(n)           |
| Search    | O(n)           |

### Notes

- `std::stack` stores elements in a last-in, first-out (LIFO) order.
- `std::stack` provides constant time complexity for insertion and deletion at the top of the stack.
- `std::stack` provides linear time complexity for accessing elements at other positions.
- `std::stack` provides functions for inserting and deleting elements.
- `std::stack` provides functions for clearing the stack and checking if the stack is empty.
- `std::stack` provides functions for accessing the top element.
- `std::stack` provides functions for comparing stacks and swapping stacks.

I hope you find this cheat sheet helpful! Let me know if you have any further questions.