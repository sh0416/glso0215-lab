#include <iostream>
#include <vector>
#define FastIO ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);
using namespace std;

int main()
{
	int count = 1;
	int N;
	cin >> N;
	int firstNum = N;
	while (true)
	{
		if (firstNum == (N / 10 + N % 10) % 10 + (N % 10 * 10))
		{
			cout << count;
			exit(0);
		}
		else
		{
			N = (N / 10 + N % 10) % 10 + (N % 10 * 10);
			count++;
		}
	}
}
