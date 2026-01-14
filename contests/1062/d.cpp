#include <bits/stdc++.h>

#define pb push_back
#define ppb pop_back

using namespace std;
using ll = long long;
using pii = pair<int, int>;
using vi = vector<int>;

constexpr char nl = '\n';

vector<ll> primes{2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61,
    67, 71};

void solve() {
    int n; cin >> n;
    vector<ll> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    for (auto p : primes) {
        for (int i = 0; i < n; ++i) {
            if (a[i] % p != 0) {
                cout << p << nl;
                return;
            }
        }
    }

    cout << -1 << nl;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int t; cin >> t;
    while (t--) solve();
}
