#include<stdio.h>
#include<string.h>

int check_palindrome_permutation(char* string) {

	int bitvector = 0;
	for (int i=0;i< strlen(string);i++) {
		
		int char_num = string[i] - 'a';

		bitvector ^= 1 << char_num;
	}
	if (((bitvector - 1) & bitvector) == 0) 
		return 1;
	return 0;
}




void main() {

	int result = check_palindrome_permutation("abcdabcc");
	printf("result is %d\n", result);

}
