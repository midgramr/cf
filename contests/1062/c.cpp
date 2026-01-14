#include <bits/stdc++.h>

#define pb push_back
#define ppb pop_back

using namespace std;
using ll = long long;
using pii = pair<int,int>;
using vi = vector<int>;

constexpr char nl = '\n';

void solve() {
    int n; cin >> n;
    vi a(n);
    bool even = false, odd = false;
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
        if (a[i] % 2 == 0) {
            even = true;
        } else {
            odd = true;
        }
    }
    if (even && odd) {
        sort(a.begin(), a.end());
    }
    for (int i = 0; i < n; ++i) {
        cout << a[i];
        if (i < n - 1) {
            cout << ' ';
        }
    }
    cout << nl;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int t; cin >> t;
    while (t--) solve();
}
