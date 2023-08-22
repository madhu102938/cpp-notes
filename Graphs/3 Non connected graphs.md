![](https://lh6.googleusercontent.com/AvJI6MEwrQF3eXS0OtWYgNtXG4H-2oMq5Fhz3Yy7VU1xAuC3uPPzGRUaKkYOKUHpRkUxDU-f5aXpehu3-K6uoGT2uHaJ4PXXh8E3BM8WkSeXpFS_zGEYrtI7ZoX7NOCThx-R4ZNl_uLKiMPCdwZ2KoE)

We can have graph like these
**This is still a single graph** but there are different components to it

To traverse all of them we use this
```cpp
for (int i = 0; i < V; i++)
{
	if (!vis[i])
		traversal(i);
}
```

This makes sure that we traverse all nodes (even if they are not connected)