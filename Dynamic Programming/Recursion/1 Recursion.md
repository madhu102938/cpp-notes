- When a function calls itself
- until a specific condition is met
```c++
f()
{
	cout << '1';
	f();
}
```
If we call this function we get a <mark style="background: #FFF3A3A6;">segmentation fault</mark> after a certain '1's are printed out.
- we get a segmentation fault because whenever a function is called it is stored in a memory in a stack, as there is not **base condition**, the function keeps on calling itself 
- As the function keeps on calling itself, the function calls stack up in the memory and we get a stack overflow which results in segmentation fault

<hr>
### Base Condition
\In recursion, the base condition is the condition that terminates the recursive function calls and returns a value. It is the condition that is checked at the beginning of each recursive call to determine whether the function should continue to call itself or return a value.

Without a base condition, a recursive function would continue to call itself indefinitely, eventually leading to a stack overflow error.

For example, consider the following recursive function to calculate the factorial of a number:

```cpp
int factorial(int n) {
    if (n == 0) {
        return 1; // base condition
    } else {
        return n * factorial(n - 1); // recursive call
    }
}
```

In this function, the base condition is `n == 0`, which checks whether the input `n` is equal to `0`. If it is, the function returns `1`, which is the base case for the factorial function. If `n` is not equal to `0`, the function makes a recursive call to itself with the argument `n - 1`.

I hope this helps! Let me know if you have any further questions.