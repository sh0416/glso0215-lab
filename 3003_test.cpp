#include <iostream>

using namespace std;

void testcase(){
    int chesstest_arr[7][6] = {
        {1, 3, 2, 4, 2, 8},
        {1, 0, 2, 0, 2, 8},
        {1, 7, 2, 2, 2, 8},
        {1, 8, 2, 4, 3, 8},
        {1, 0, 2, 7, 6, 8},
        {1, 7, 9, 8, 2, 8},
        {1, 8, 2, 9, 2, 11},
    };
}


int matchtest() {
	int chess[6] = {1, 1, 2, 2, 2, 8};
	int chesstest_arr[7][6] = {
        {1, 3, 2, 4, 2, 8},
        {1, 0, 2, 0, 2, 8},
        {1, 7, 2, 2, 2, 8},
        {1, 8, 2, 4, 3, 8},
        {1, 0, 2, 7, 6, 8},
        {1, 7, 9, 8, 2, 8},
        {1, 8, 2, 9, 2, 11},
    };
	
	
	for (int j = 0; j < 7; j++)
    {
        for(int i=0; i<6; i++) {
            cout << (chess[i]-chesstest_arr[j][i]) << " ";
        }
    }
    
	
	return 0;
}


int main() {
	matchtest();
	return 0;
}