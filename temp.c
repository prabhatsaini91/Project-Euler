#include <stdio.h>

int main() {
	int i, max_index = 2, chain_length, chain_lengths[1000000] = { 0, 1, 2 };
	long num;

	
	for (i = 3; i < 1000000; ++i) {
		chain_length = 0;
		num = i;

		while (num >= i) {
			num = (num % 2 == 0) ? (num / 2) : (num * 3 + 1);
			chain_length++;
		}

		chain_lengths[i] = chain_length + chain_lengths[num];


		if (chain_lengths[i] > chain_lengths[max_index]) {
			max_index = i;
		}
	}

	printf("%d", max_index);

	return 0;
}