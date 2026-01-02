#include <bits/stdc++.h>

#define pb push_back

using namespace std;
using ll = long long;
using pii = pair<int, int>;
using vi = vector<int>;

constexpr char nl = '\n';

const int N = 2 * (int)1e5;
int t, n;
vector<int> group(N + 1), primeIdx(N + 1), primes;

void solve() {
    cin >> n;

    vector<int> a(n);
    iota(a.begin(), a.end(), 1);
    sort(a.begin(), a.end(), [&](const int& x, const int& y) {
        if (group[x] < group[y]) {
            return true;
        } else if (group[x] > group[y]) {
            return false;
        } else {
            int p1 = group[x];
            int k = primeIdx[p1] + 1;
            if (k < (int)primes.size()) {
                int p2 = primes[k];
                if (x == p1 * p2) {
                    return false;
                }
                if (y == p1 * p2) {
                    return true;
                }
            }
            return x < y ? true : false;
        }
    });

    int i = 0, j = (int)a.size() - 1;
    while (i <= j) {
        if (i == j) {
            cout << a[i] << nl;
            break;
        }
        if (i == j - 1) {
            cout << a[i] << ' ' << a[j] << nl;
            break;
        }
        cout << a[j] << ' ' << a[i] << ' ' << a[i + 1];
        i += 2;
        j -= 1;
        cout << (i <= j ? ' ' : nl);
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    group[1] = N;
    for (int i = 2; i <= N; ++i) {
        if (group[i]) {
            continue;
        }
        primeIdx[i] = (int)primes.size();
        primes.pb(i);
        group[i] = i;
        for (ll j = (ll)i * i; j <= N; j += i) {
            if (group[j]) {
                continue;
            }
            group[j] = i;
        }
    }

    cin >> t;
    while (t--) {
        solve();
    }
}
