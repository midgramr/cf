#include <bits/stdc++.h>

#define pb push_back

using namespace std;
using ll = long long;
using pii = pair<int, int>;
using vi = vector<int>;
using pll = pair<ll, ll>;

constexpr char nl = '\n';

ll n, m, l, x, y;

double key(const pll &bus) {
    auto [s, t] = bus;
    return double(t - s) / double(x) + double(l - t) / double(y);
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> n >> m >> l >> x >> y;

    vector<pll> buses(n), people(m);
    for (auto &[s, t] : buses) {
        cin >> s >> t;
    }
    for (int i = 0; i < m; ++i) {
        cin >> people[i].first;
        people[i].second = i;
    }

    sort(buses.begin(), buses.end());
    sort(people.begin(), people.end());

    size_t i = 0, j = 0;
    set<double> availableBuses;
    vector<double> ans(m);
    for (auto [p, k] : people) {
        // Get only the window of buses that are relevant to the current person
        for (; j < buses.size() && buses[j].first <= p; ++j) {
            // If two buses have the same key, they're interchangeable
            availableBuses.insert(key(buses[j]));
        }
        for (; i < j && buses[i].second <= p; ++i) {
            availableBuses.erase(key(buses[i]));
        }
        double best = double(l - p) / double(y);
        if (!availableBuses.empty()) {
            double bestBus = *availableBuses.begin();
            best = min(best, bestBus);
        }
        ans[k] = best;
    }

    cout << setprecision(7);
    for (auto a : ans) {
        cout << fixed << a << nl;
    }

    return 0;
}
