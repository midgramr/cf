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
    string s, t;
    cin >> s >> t;
    unordered_map<char, int> cnt;
    for (auto c : s) {
        cnt[c] += 1;
    }
    for (auto c : t) {
        cnt[c] -= 1;
    }
    for (auto [_, num] : cnt) {
        if (num != 0) {
            cout << "NO" << nl;
            return;
        }
    }
    cout << "YES" << nl;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int q; cin >> q;
    while (q--) solve();
}
