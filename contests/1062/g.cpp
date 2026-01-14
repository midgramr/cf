#include <bits/stdc++.h>

#define DEBUG 0

using namespace std;
using ll = long long;
using pii = pair<int, int>;

constexpr char nl = '\n';

void solve() {
    int n;
    cin >> n;
    vector<ll> a(n), c(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }
    for (int i = 0; i < n; ++i) {
        cin >> c[i];
    }

    vector<ll> lis{c};
    ll total = accumulate(c.begin(), c.end(), 0LL);
    for (int i = 1; i < n; ++i) {
        for (int j = 0; j < i; ++j) {
            if (a[i] >= a[j]) {
                lis[i] = max(lis[i], lis[j] + c[i]);
            }
        }
    }

    ll hi = *max_element(lis.begin(), lis.end());
    cout << total - hi << nl;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    int t;
    cin >> t;
    while (t--) {
        solve();
    }
}
