#include <bits/stdc++.h>
#include <numbers>

#define pb push_back

using namespace std;
using namespace numbers;
using ll = long long;
using pii = pair<int, int>;
using pdd = pair<double, double>;
using vi = vector<int>;

constexpr char nl = '\n';

struct Point {
    ll x, y;
};

// Cross product of BA and BC
ll cross(Point a, Point b, Point c) {
    return (a.x - b.x) * (c.y - b.y) - (a.y - b.y) * (c.x - b.x);
}

double norm(Point a, Point b) {
    return sqrt(pow(b.x - a.x, 2) + pow(b.y - a.y, 2));
}

double norm2(pdd a, pdd b) {
    return sqrt(pow(b.first - a.first, 2) + pow(b.second - a.second, 2));
}

// Assume no complex roots, since secant line is guaranteed to intersect circle
pdd solveQuad(double a, double b, double c) {
    double conj = sqrt(b * b - 4 * a * c), den = 2 * a;
    return {(-b - conj) / den, (-b + conj) / den};
}

vector<Point> hull(vector<Point> &pts) {
    // Get bottom-left most point
    Point p0 = pts[0];
    for (auto point : pts) {
        if (point.y < p0.y || (point.y == p0.y && point.x < p0.x)) {
            p0 = point;
        }
    }

    // Sort pts by polar angle with p0
    sort(pts.begin(), pts.end(), [&p0](const Point &a, const Point &b) {
        ll dir = cross(a, p0, b);
        if (dir > 0) {
            // counterclockwise
            return true;
        } else if (dir < 0) {
            // clockwise
            return false;
        } else {
            // If points collinear, break ties by distance to p0
            return norm(a, p0) < norm(b, p0);
        }
    });

    // Compute the hull
    vector<Point> stk{p0};
    int n = (int)pts.size();
    for (int i = 1; i < n; ++i) {
        Point &a = pts[i];
        while (stk.size() > 1) {
            int m = (int)stk.size();
            Point &b = stk[m - 1], &c = stk[m - 2];
            if (cross(c, b, a) < 0) {
                break;
            }
            stk.pop_back();
        }
        stk.pb(a);
    }

    return stk;
}

double solve() {
    ll n, r, x, y;
    vector<Point> points;

    cin >> n >> r;

    for (int i = 0; i < n; ++i) {
        cin >> x >> y;
        points.pb({x, y});
    }

    vector<Point> cvx = hull(points);

    double semiArea = pi * (r * r) / 2;
    if (cvx.size() < 3) {
        return semiArea;
    }

    // Iterate through adjacent points on the hull
    int m = (int)cvx.size();
    double maxChord = 0;
    for (int i = 0; i < m; ++i) {
        Point &p1 = cvx[i], &p2 = cvx[(i + 1) % m], &p3 = cvx[(i + 2) % m];

        // Represent line in the form ax + by = c
        double a, b, c;
        // Edge case: secant line is vertical
        if (p1.x == p2.x) {
            a = 1, b = 0, c = p1.x;
        } else {
            // Find the containing line
            double slope = double(p2.y - p1.y) / (p2.x - p1.x),
                   intercept = p1.y - slope * p1.x;
            a = -slope, b = 1, c = intercept;
        }

        // Edge case: secant line separates hull inside circular segment
        if ((a * p3.x + b * p3.y > c) != (0 > c)) {
            return semiArea;
        } else {
            double chordLen;
            if (p1.x == p2.x) {
                chordLen = 2 * sqrt(r * r - pow(c / a, 2));
            } else {
                auto [x1, x2] =
                    solveQuad(1 + pow(a / b, 2), -2 * a * c / (b * b),
                              pow(c / b, 2) - r * r);
                double y1 = (-a * x1 + c) / b, y2 = (-a * x2 + c) / b;
                chordLen = norm2({x1, y1}, {x2, y2});
            }
            maxChord = max(maxChord, chordLen);
        }
    }
    double theta = 2 * asin(maxChord / (2 * r));
    return r * r / 2.0 * (theta - sin(theta));
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    printf("%.7f\n", solve());
}
