for (int k = i+1; k < j; ++k) {
    chmin(dp[i][j], dp[i][k] + dp[k][j] + s[i:j]);
}
