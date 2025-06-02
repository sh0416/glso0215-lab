#include<stdio.h>

int main(){
	int N, i;
	scanf("%d", &N);
	
	for(i=N/4; i>0; i--)
		printf("long ");
	printf("int");
	
	return 0;
}