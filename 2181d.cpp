#include <bits/stdc++.h>

#define pb push_back
#define ppb pop_back

using namespace std;
using ll = long long;
using pii = pair<int, int>;
using vi = vector<int>;

constexpr char nl = '\n';

void print(const vi& vec) {
    cout << "[";
    for (int i = 0; i < (int)vec.size(); ++i) {
        cout << vec[i] << ", ";
    }
    cout << "]" << nl;
}

void solve() {
    int n, k, x1, x2;
    cin >> n;

    vector<vi> layers(n), layersPre(n), layersSuf(n);
    vi layerSpace(n);
    int lo = int(1e9), loIdx = -1;
    int l = 0, r = int(1e9);
    for (int i = 0; i < n; ++i) {
        cin >> k >> x1 >> x2;
        l = max(l, x1), r = min(r, x2);

        layers[i] = vi(k);
        for (int j = 0; j < k; ++j) {
            cin >> layers[i][j];
        }

        layersPre[i] = vi(k + 1);
        layersPre[i][0] = x1;
        for (int j = 0; j < k; ++j) {
            layersPre[i][j + 1] = layers[i][j] + layersPre[i][j];
        }

        layersSuf[i] = vi(k + 1);
        layersSuf[i][k] = x2;
        for (int j = k - 1; j >= 0; --j) {
            layersSuf[i][j] = layers[i][j] + layersSuf[i][j + 1];
        }

        int empty = x2 - layersPre[i][k];
        layerSpace[i] = empty;
        if (empty < lo) {
            lo = empty;
            loIdx = i;
        } else if (empty == lo && k < (int)layers[loIdx].size()) {
            loIdx = i;
        }
    }

    if (lo == 0) {
        cout << 0 << nl;
        return;
    }

    int ans = 0;
    int leftBound, rightBound, layerBound;
    bool skip;

    // Check possible left boundaries
    vi* layer = &layersPre[loIdx];
    int space = layerSpace[loIdx];
    for (int j = 0; j < (int)layer->size(); ++j) {
        leftBound = (*layer)[j];
        rightBound = leftBound + space;
        skip = false;
        for (int i = 0; i < n; ++i) {
            if (i == loIdx) {
                continue;
            }
            auto it = upper_bound(layersPre[i].begin(), layersPre[i].end(), leftBound);
            if (it == layersPre[i].begin()) {
                skip = true;
                break;
            }
            layerBound = *(it - 1);
            rightBound = min(rightBound, layerBound + layerSpace[i]);
        }
        if (!skip) {
            ans = max(ans, rightBound - leftBound);
        }
    }

    // Check possible right boundaries
    layer = &layersSuf[loIdx];
    for (int j = 0; j < (int)layer->size(); ++j) {
        rightBound = (*layer)[j];
        leftBound = rightBound - space;
        skip = false;
        for (int i = 0; i < n; ++i) {
            if (i == loIdx) {
                continue;
            }
            auto it = lower_bound(layers[i].begin(), layers[i].end(), rightBound);
            if (it == layers[i].end() || (*it != rightBound && it == layers[i].end() - 1)) {
                skip = true;
                break;
            }
            layerBound = (*it == rightBound) ? rightBound : *(it + 1);
            leftBound = max(leftBound, layerBound + layerSpace[i]);
        }
        if (!skip) {
            ans = max(ans, rightBound - leftBound);
        }
    }

    cout << ans << nl;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    solve();
}
