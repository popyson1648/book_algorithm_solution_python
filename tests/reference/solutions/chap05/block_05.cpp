// a[i] を選ばない場合
chmin(dp[i+1][j], dp[i][j]);

// a[i] を選ぶ場合 (+1 は 1 個増やすことを意味する)
if (j >= a[i]) chmin(dp[i+1][j], dp[i][j-a[i]] + 1);
