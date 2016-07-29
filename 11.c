#include <stdio.h>

int main() {
	int i, j, product;
	long largest_product = 1;
	char nums[60];
	int grid[20][20];
	FILE *fp = fopen("grid", "r");

	for(i=0; i<20; ++i) {
		fgets(nums, sizeof(nums), fp);
		
		// printf("%s", nums);
		for(j=0; j<20; ++j) {
			grid[i][j] = ((nums[j*3] - '0') * 10) + (nums[j*3+1] - '0');
		}
		//printf("\nwhat seems to be the problem %c",getc(fp));	// an extra \n at the end is causing trouble
		getc(fp);
	}
	
	fclose(fp);

	// for(i=0;i<20;++i) {
	// 	for(j=0;j<20;++j) {
	// 		printf("%d ",grid[i][j]);
	// 	}
	// }

	for(i=0; i<20; ++i) {
		for(j=0; j<17; ++j) {

			//calculating E/W products
			product = grid[i][j] * grid[i][j+1] * grid[i][j+2] * grid[i][j+3];
			if(product > largest_product) {
				largest_product = product;
			}

			//calculating N/S products
			product = grid[j][i] * grid[j+1][i] * grid[j+2][i] * grid[j+3][i];
			if(product > largest_product) {
				largest_product = product;
			}
		}
	}

	//calculating NW/SE product
	for(i=0;i<17;++i) {
		for(j=0;j<17;++j) {
			product = grid[i][j] * grid[i+1][j+1] * grid[i+2][j+2] * grid[i+3][j+3];
			if(product > largest_product) {
				largest_product = product;
			}
		}
	}

	//calculating NE/SW product
	for(i=3;i<20;++i) {
		for(j=0;j<16;++j) {
			product = grid[i][j] * grid[i-1][j+1] * grid[i-2][j+2] * grid[i-3][j+3];
			if(product > largest_product) {
				largest_product = product;
			}
		}
	}

	printf("%lu",largest_product);
	return 0;
}