#include <stdio.h>

//need to optimise this
//running in exponential time

/*
	one thing to note is that chain lengths can be memoized in an array
	but the problem is with odd numbers

	for example if you are finding chain length for the number 27, it being odd becomes 27*3 + 1 = 82
	now 82 hasn't been computed yet
	further 82 becomes 41 which still hasn't been computed

	
	****the solution is easy enough to understand*****

		all odd numbers are going to generate a number larger than the one in consideration
		which means the loop checking is: 

			******************************************************************************************
				while(chain_lengths_for_numbers_that_"may"_have_been_calculated >= number_in_consideration) 	
			******************************************************************************************

		
*/


/*  
	omit this function of computing chain lengths for the time being
	this is extremely inefficient, goes on calculating chain lengths for numbers that have
	already been found out

long find_chain_lengths(long num) {
	long chain_length = 1;

	while(num!=1) {
		num = (num % 2 == 0) ? n /2 : n * 3 + 1;
	}

	++chain_length;

	return chain_length;
} 
*/

int main() {

	int i, longest_chain_length_index = 2, chain_length, chain_lengths[1000000] = { 0, 1, 2 };
	long num;
	
	for(i=3; i<1000000; ++i) {
		chain_length = 0;
		num = i;

		while(num >= i) {
			num = (num % 2 == 0) ? (num / 2) : (num * 3 + 1);
			chain_length++;
		}

		/* as soon as num < i: 
			the chain length value for num can be looked in the array
			further the new chain length value for i can also be stored
		*/

		chain_lengths[i] = chain_length + chain_lengths[num];

		if(chain_lengths[i] > chain_lengths[longest_chain_length_index]) {
			longest_chain_length_index = i;
		}
	}	

	printf("%d", longest_chain_length_index);

	

	// unsigned long chain_length, longest_chain_length = 1, num_to_find, num = 2;

	// while(num <= 999999) {
	// 	chain_length = find_chain_lengths(num);
	// 	printf("Chain length %lu for number : %lu \n", chain_length, num);
	// 	if(longest_chain_length < chain_length) {
	// 		num_to_find = num;
	// 		longest_chain_length = chain_length;
	// 	}

	// 	++num;
	// }


	// printf("%lu",num_to_find);
	
	return 0;
}