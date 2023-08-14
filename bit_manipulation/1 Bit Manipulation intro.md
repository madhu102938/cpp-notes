A computer is really fast at bit manipulation rather than actually doing some long division, so we can use bit manipulation to decrease execution time.
## Operators
- and `&` *(both should be 1 to get a 1)*
- or `|` *(either one should be 1 to get a 1)*
- xor `^` *(both should not be same to get a 1)*
- negation `~` *(toggles the bit)*
- right shift `>>`
	- `1101 >> 2` is `11` last two bits are gone
	- right shift by `x` means integral division by $2^x$
- left shift `<<`
	- `1101 << 2` is `110100` last two bits are added
	- left shift by `x` means integral multiplication by $2^x$