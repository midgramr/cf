#include <bits/stdc++.h>

#define DEBUG 0

using namespace std;
using ll = long long;
using pii = pair<int, int>;

constexpr char nl = '\n';

void solve() {
    int n, k;
    cin >> n >> k;

    vector<vector<int>> adj(n + 1);
    for (int i = 0; i < n - 1; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    vector<int> cnt(n + 1, 1);
    function<int(int, int)> dfs1 = [&](int u, int p) {
        for (auto v : adj[u]) {
            if (v != p) {
                cnt[u] += dfs1(v, u);
            }
        }
        return cnt[u];
    };
    dfs1(1, 0);

    ll ans = 0;
    for (int u = 1; u <= n; ++u) {

    }
    cout << ans << nl;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    int t;
    cin >> t;
    while (t--)
        solve();
}
