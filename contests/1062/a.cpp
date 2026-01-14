#include <bits/stdc++.h>

#define pb push_back
#define ppb pop_back

using namespace std;
using ll = long long;
using pii = pair<int, int>;
using vi = vector<int>;

constexpr char nl = '\n';

void solve() {
    int a, b, c, d;
    cin >> a >> b >> c >> d;
    cout << (a == b && b == c && c == d ? "YES" : "NO") << nl;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int t; cin >> t;
    while (t--) {
        solve();
    }
}
