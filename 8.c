#include <stdio.h>

int main() {

	char num[1000];

	int i, j, temp;
	unsigned long product, largest_product = 1 ;

	FILE *fp = fopen("number","r");
	fgets(num, 1001, fp);
	fclose(fp);

	for(i = 0; i < 988; ++i) {
		product = 1;
		for(j = i; j < i + 13; ++j) {
			temp = num[j] - '0';
			printf("%c",num[j]);
			product = product * temp;
		}

		// printf("--");


		if(product > largest_product) {
			largest_product = product;
		}				
	}

	printf("%lu",largest_product);

	return 0;
}
