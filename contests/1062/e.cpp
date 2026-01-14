#include <bits/stdc++.h>

#define pb push_back
#define ppb pop_back

using namespace std;
using ll = long long;
using pii = pair<int, int>;
using vi = vector<int>;

constexpr char nl = '\n';

void solve() {
    int n, k, x, ai;
    cin >> n >> k >> x;
    vi a;
    unordered_set<int> distinct;
    for (int i = 0; i < n; ++i) {
        cin >> ai;
        if (!distinct.count(ai)) {
            a.pb(ai);
            distinct.insert(ai);
        }
    }

    // tuple state: {dist to closest, left, right, loc}
    priority_queue<tuple<int, int, int, int>> pq;

    sort(a.begin(), a.end());
    int z = a.size();
    if (a[0] != 0) {
        pq.push({a[0], -1, a[0], 0});
    }
    if (a[z - 1] != x) {
        pq.push({x - a[z - 1], a[z - 1], -1, x});
    }
    for (int i = 1; i < z; ++i) {
        int l = a[i - 1], r = a[i];
        int d = (r - l) / 2, m = l + d;
        if (d > 0) {
            pq.push({d, l, r, m});
        }
    }

    vi ans;
    while (ans.size() < k && !pq.empty()) {
        auto [d, l, r, m] = pq.top();
        pq.pop();
        ans.pb(m);
        if (l == -1) {
            if (d > 1) {
                pq.push({d - 1, -1, r, m + 1});
            }
        } else if (r == -1) {
            if (d > 1) {
                pq.push({d - 1, l, -1, m - 1});
            }
        } else {
            if (m - l > 1) {
                pq.push({m - l - 1, l, -1, m - 1});
            }
            if (r - m > 1) {
                pq.push({r - m - 1, -1, r, m + 1});
            }
        }
    }
    for (int j = 0; ans.size() < k; ++j) {
        ans.pb(a[j]);
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
    cin.tie(nullptr);
    int t;
    cin >> t;
    while (t--)
        solve();
}
