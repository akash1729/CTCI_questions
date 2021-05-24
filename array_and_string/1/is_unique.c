#include<string.h>
#include<stdio.h>



int is_unique(char* string) {

	int counter[128] = {0};
	
	for(int i=0;i<strlen(string);i++) {
		if (counter[string[i]] == 1)
			return 0;
		counter[string[i]] = 1;	
	}
	return 1;
}


void main(){

		printf("%d\n", is_unique("akash"));

}
