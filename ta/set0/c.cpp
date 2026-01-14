#include <bits/stdc++.h>

using namespace std;
using ll = long long;
using pii = pair<int, int>;

constexpr char nl = '\n';

void solve() {
    int m;
    char p;
    string res;

    vector<int> penalty(26);
    int totalPenalty = 0, totalSolved = 0;
    while (true) {
        cin >> m;
        if (m == -1) {
            break;
        }

        cin >> p >> res;
        int c = p - 'A';
        if (res == "right") {
            penalty[c] += m;
            totalPenalty += penalty[c];
            totalSolved++;
        } else {
            penalty[c] += 20;
        }
    }

    cout << totalSolved << ' ' << totalPenalty << nl;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    int t = 1;
    while (t--) {
        solve();
    }
}
