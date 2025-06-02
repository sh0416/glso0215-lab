#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

int isEqual(int* arr1, int* arr2, int n) {
	for (int i = 0; i < n; i++)
	{
		if (arr1[i] != arr2[i]) return 0;
	}
	return 1;
}

void testcase1()
{
	int arr[] = { 3, 2, 1 };
	int expected[] = { 1, 2, 3 };
	sortFunc(arr, sizeof(arr) / sizeof(int));
	printf("Test1: %s\n", isEqual(arr, expected, sizeof(arr) / sizeof(int)) ? "pass" : "fail");
}

void testcase2()
{
	int arr[] = { 5, 1, 4, 2, 3 };
	int expected[] = { 1, 2, 3, 4, 5 };
	sortFunc(arr, sizeof(arr) / sizeof(int));
	printf("Test2: %s\n", isEqual(arr, expected, sizeof(arr) / sizeof(int)) ? "pass" : "fail");
}

void testcase3()
{
	int arr[] = { 1 };
	int expected[] = { 1 };
	sortFunc(arr, sizeof(arr) / sizeof(int));
	printf("Test3: %s\n", isEqual(arr, expected, sizeof(arr) / sizeof(int)) ? "pass" : "fail");
}

void testcase4()
{
	int arr[] = { 3, 2 };
	int expected[] = { 2, 3 };
	sortFunc(arr, sizeof(arr) / sizeof(int));
	printf("Test4: %s\n", isEqual(arr, expected, sizeof(arr) / sizeof(int)) ? "pass" : "fail");
}

void test()
{
	testcase1();
	testcase2();
	testcase3();
	testcase4();
}