#include <bits/stdc++.h>

#define pb push_back
#define ppb pop_back
#define DEBUG 0

using namespace std;
using ll = long long;
using pii = pair<int, int>;
using vi = vector<int>;

constexpr char nl = '\n';

void solve() {
    int n, k, x;
    cin >> n >> k >> x;
    vi a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    priority_queue<pii> pq;

    sort(a.begin(), a.end());
    // Brute force through every possible position
    for (int p = 0, i = 0; p <= x; ++p) {
        if (p > a[i] && i < n - 1) {
            i++;
        }
        #if DEBUG
        cout << "p = " << p << ", i = " << i << nl;
        #endif
        int d = abs(a[i] - p);
        if (i > 0) {
            d = min(d, abs(a[i - 1] - p));
        }
        pq.push({d, p});
    }

    vi ans;
    for (int i = 0; i < k; ++i) {
        auto [d, p] = pq.top();
        pq.pop();
        ans.pb(p);
    }

    for (int i = 0; i < k; ++i) {
        cout << ans[i];
        if (i < k - 1) {
            cout << ' ';
        }
    }

    cout << nl;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int t;
    cin >> t;
    while (t--)
        solve();
}
