#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

void sortFunc(int* arr, int n) {
	for (int i = 1; i < n; i++)
	{
		int v = arr[i];
		for (int j = i - 1; j >= 0; j--)
		{
			if (arr[j] > v) {
				arr[j + 1] = arr[j];
			}
			else {
				arr[j + 1] = v;
				break;
			}
			if (j == 0) arr[j] = v;;
		}
	}
}

void printFunc(int* arr, int n) {
	for (int i = 0; i < n; i++) printf("%d\n", arr[i]);
}

int main()
{
	//int n = 0; scanf("%d", &n);
	//int* arr = (int*)malloc(sizeof(int) * n);
	//for (int i = 0; i < n; i++) scanf("%d", arr + i);

	//sortFunc(arr, n);
	//printFunc(arr, n);
	test();

	return 0;
}