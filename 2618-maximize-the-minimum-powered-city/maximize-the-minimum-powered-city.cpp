class Solution {
public:
    bool is(vector<long long> &a, int r, long long k, long long m) {
        long long h, sum = 0, ans = 0;
        if (r == 0) {
            for (auto &i : a) {
                if (i < m)
                    ans += m - i;
                if (ans > k)
                    return false;
            }
            return true;
        }
        queue<long long> q;
        h = r * 2;
        while (h--)
            q.push(0);
        for (auto &i : a) {
            h = i + sum;
            if (h >= m)
                q.push(0);
            else {
                ans += (m - h);
                q.push(m - h);
                sum += (m - h);
            }
            if (ans > k)
                return false;
            h = q.front();
            q.pop();
            sum -= h;
        }
        return true;
    }

    long long maxPower(vector<int> &num, int r, long long k) {
        long long l = 0, h = 2e10, m, ans, n = num.size(), sum = 0;
        vector<long long> a(n);
        for (int i = 0; i <= r; i++)
            sum += num[i];
        for (int i = 0; i < n; i++) {
            a[i] = sum;
            if (i + r + 1 < n)
                sum += num[i + r + 1];
            if (i >= r)
                sum -= num[i - r];
        }
        while (l <= h) {
            m = l + (h - l) / 2;
            if (!is(a, r, k, m))
                h = m - 1;
            else {
                ans = m;
                l = m + 1;
            }
        }
        return ans;
    }
};