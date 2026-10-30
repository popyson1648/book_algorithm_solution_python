// a[i] を選ばない場合
if (dp[i][j]) dp[i+1][j] = true;

// a[i] を選ぶ場合
if (j >= a[i] && dp[i][j-a[i]]) dp[i+1][j] = true;
