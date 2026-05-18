#include <bits/stdc++.h>
#define all(a) (a).begin(), (a).end()
#define sz(a) (int)(a).size()
#define rep(i, a, b) for (int i = a; i < b; ++i)
#define rrep(i, a, b) for (int i = a; i >= b; --i)

constexpr char nl = '\n';
using namespace std;
using ll = long long;
using pii = pair<int, int>;

void solve() {
    int x, y; cin >> x >> y;
    // If x + y is odd, all odds is possible, otherwise there must be 1 even
    // Most evens is floor((x + y) / 2)
    if (x > (x + y) / 2 || (x == 0 && (x + y) % 2 == 0)) {
        cout << "NO" << nl;
        return;
    }
    cout << "YES" << nl;
    if (x > 0) {
        rep(i, 2, 2 * x + 1) {
            cout << i - 1 << ' ' << i << nl;
        }
        rep(i, 2 * x + 1, x + y + 1) {
            cout << 2 * x << ' ' << i << nl;
        }
    } else {
        rep(i, 2, y + 1) {
            cout << 1 << ' ' << i << nl;
        }
    }
}

int main() {
    cin.tie(0)->sync_with_stdio(0);
    int t; cin >> t;
    while (t--) {
        solve();
    }
}
