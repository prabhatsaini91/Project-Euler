#include <stdio.h>

int main() {
	int i,j;
	FILE *fp = fopen("p067_triangle.txt","r");
	char nums[300];
	int grid[100][100];


	for(i=0;i<100;++i) {
		
		fgets(nums, sizeof(nums), fp);
		for(j=0;j<100;++j) {

			// since some lines are shorter
			if(nums[j*3]=='\0') {

				// i hate nested looping constructs. need to do it though
				while(j<100) {
					// substitute every number for zero
					grid[i][j] = 0;
					++j;
				}
			}
			else {
				grid[i][j] = (nums[j*3] - '0')*10 + (nums[j*3+1] - '0');
			}
		}
	}

	/*  Alright that takes care of the array. The grid now stores the elements. At a glance, it feels like
		a greedy approach would work.

		Behold! 
						******************************************************
						*  THE GREEDY APPROACH WILL NOT WORK IN THIS PROBLEM *
						******************************************************
						

		Let's see if greedy approach would work: 
			** The first element is 75. Add the elements in the next line. 
			** Delete line 1. Now the second line houses 95+75	64+75
			** Naturally it is better to take 95+75 = 170. 
			** Next, we have 170  139
			** Line 3 now becomes  187  217 or 186  221
			** I chose 170 earlier, but actually I should have chosen 139 which would have got me to a better sum

			Hence, my statement was true.


		Dynamic Programming is the answer. But that's not the thing to frown upon. 

		The thing is the approach. TOP-DOWN or BOTTOM-UP? 

		I believe both would work equally well. 
	*/

	// for(i=0;i<15;++i) {
	// 	for(j=0;j<15;++j) {
	// 		printf("%d ", grid[i][j]);
	// 	}
	// 	printf("\n");
	// }

	
	int max_sum;
	int sum_table[100];
	
	for(i=0;i<100;++i) {
		sum_table[i] = 0;
	}

	for(i=99;i>=0;--i) {
		for(j=0;j<99;++j) {
			if(grid[i][j] + sum_table[j] > grid[i][j] + sum_table[j+1]) {
				sum_table[j] = grid[i][j] + sum_table[j];
			}
			else {
				sum_table[j] = grid[i][j] + sum_table[j+1];
			}
		}
	}

	// for(i=0;i<15;++i) {
	// 	printf("%d ",sum_table[i]);
	// }

	printf("%d", sum_table[0]);




	return 0;
}