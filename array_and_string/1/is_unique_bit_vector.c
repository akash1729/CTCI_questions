#include<stdio.h>
#include<string.h>



int is_unique(char* string) {

	int counter = 0;

	for(int i=0;i<strlen(string);i++) {

		int letter = string[i] - 'a';

		if ((counter & 1 << letter) > 0) {
			printf("stopping for letter %d\n", letter);	
			return 0;

		}
		counter |= 1 << letter;
	}
	return 1;
}


void main() {


	printf("%d\n", is_unique("abcdefghijklmnop"));

}
