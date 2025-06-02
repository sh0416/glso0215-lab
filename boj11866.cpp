#include <bits/stdc++.h>
#define fastio cin.tie(0); ios::sync_with_stdio(0)
typedef long long ll;
using namespace std;

int n,k;
list<int> arr;

int main()
{
    fastio;
    cin>>n>>k;
    for(int i=1;i<=n;++i) arr.push_back(i);
    auto i = arr.begin();
    int cnt = 0;
    cout<<'<';
    while(1)
    {
        ++cnt;
        if(cnt == k)
        {
            cout<<*i;
            i = arr.erase(i);
            --i;
            if(arr.empty()) break;
            cnt = 0;
            cout<<", ";
        }
        ++i;
        if(i == arr.end()) i = arr.begin();
    }
    cout<<'>';

}
