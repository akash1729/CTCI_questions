#include<stdio.h>



void rotate_matrix(int matrix[][3]) {

		:wq
			


}



void main(){

	int matrix[][3] = {{0,2,3}, {4,5,6}, {7,8,9}, {10,11,12}};

	int m = sizeof(matrix)/sizeof(matrix[0]);
	int n = sizeof(matrix[0])/sizeof(matrix[0][0]);


	printf("size : %dx%d\n", m, n); 
	
	rotate_matrix(matrix);
}
