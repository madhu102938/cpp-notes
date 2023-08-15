**Q) Given an array where all elements repeat once, except one which only occurs once, return that element**
- We can take **XOR** of all the elements in the array to get the number which occurs only once
```cpp
int func(int arr[], int n)
{
	int ans = arr[0];
	for (int i = 1; i < n; i++)
		ans = ans ^ arr[i];
	return ans;
}
```

<hr>

**Q) Swapping two elements without using a temp variable**
- `a = 5`
- `b = 7`
- `a = a^b` 
- `b = a^b`  Here `b = (a^b)^b` and `b^b` cancels and we get `b = a`
- `a = a^b`  Here `a = (a^b)^a` and `a^a` cancels and we get `a = b`

<hr>

Q) Given N print print the XOR of all numbers between 1 to N (both included) in O(1) time
N = 1 -> 1
N = 2 -> 3
N = 3 -> 0
N = 4 -> 4
N = 5 -> 1
N = 6 -> 7
N = 7 -> 0
N = 8 -> 8
- We can see a pattern here, that if N is multiple of 4, we get answer as N
- If N is in form of 4n+1 then answer is 1
- if N is in form of 4n+2 then answer is N+1
- If N is in form of 4n+3 then answer is 0
```cpp
int func(int n)
{
	if (n % 4 == 0)
		return n;
	else if (n % 4 == 1)
		return 1;
	else if (n % 4 == 2)
		return n+1;
	else
		return 0;  
}
```

<hr>

**Q) Given a range (L->R) print the XOR from L to R ((L)^(L+1)^(L+2)^.........^(R-1)^(R)) in O(1) time**
We can find XOR of all numbers from 1 to L-1 lets say the answer is N
similarly the XOR of all numbers from 1 to R is M
we should do `M ^ N` to get our answer
*Example*
	L = 3, R = 6
	we need to find 3^4^5^6
	we can find 1^2 and 1^2^3^4^5^6
	now we make xor of (1^2^3^4^5^6) ^ (1^2), the 1 and 2 will be cancelled and we get the required answer
```cpp
int func(int n) // function for finding xor of all numbers from 1 to n
{
	if (n % 4 == 0)
		return n;
	else if (n % 4 == 1)
		return 1;
	else if (n % 4 == 2)
		return n+1;
	else
		return 0;  
}

int answerfunc(int L, int R)
{
	int n = func(L-1);
	int m = func(R);
	return m^n;
}
```