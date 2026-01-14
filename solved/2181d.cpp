#include <bits/stdc++.h>

#define pb push_back
#define ppb pop_back

using namespace std;
using ll = long long;
using pii = pair<int, int>;
using vi = vector<int>;

constexpr char nl = '\n';

void solve() {
    int n, k;
    cin >> n;

    vi x1(n), x2(n);
    vector<vi> doors(n);
    for (int i = 0; i < n; ++i) {
        cin >> k; cin >> x1[i]; cin >> x2[i];
        doors[i] = vi(k);
        for (int j = 0; j < k; ++j) {
            cin >> doors[i][j];
        }
    }

    // Track space remaining on each layer after taking out walls and doors
    vi space(n);
    priority_queue<pii, vector<pii>, greater<pii>> pq;
    for (int i = 0; i < n; ++i) {
        int pre = x1[i];
        pq.push({pre, i});
        for (int j = 0; j < (int)doors[i].size(); ++j) {
            pre += doors[i][j];
            pq.push({pre, i});
        }
        space[i] = x2[i] - pre;
        if (space[i] == 0) {
            cout << 0 << nl;
            return;
        }
    }

    // Track right bounds across all layers to quickly find the min
    multiset<int> rightBounds;
    // Track the right bound on each layer
    vi layerRightBounds(n, -1);
    int ans = 0;
    while (!pq.empty()) {
        auto [left, layer] = pq.top();
        pq.pop();
        int right = left + space[layer];
        // Every layer should be represented at most once
        if (layerRightBounds[layer] != -1) {
            rightBounds.extract(layerRightBounds[layer]);
        }
        layerRightBounds[layer] = right;
        rightBounds.insert(right);
        if ((int)rightBounds.size() == n) {
            int size = *rightBounds.begin() - left;
            ans = max(ans, size);
        }
    }

    cout << ans << nl;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    solve();
}
