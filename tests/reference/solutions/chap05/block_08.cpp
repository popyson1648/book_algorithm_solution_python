dp[i+1][j] |= dp[i][j];
dp[i+1][j] |= dp[i+1][j-a[i]];
