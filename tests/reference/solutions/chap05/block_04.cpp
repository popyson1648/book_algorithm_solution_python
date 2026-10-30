for (int i = 0; i < N; ++i) {
    for (int j = 0; j <= W; ++j) {
        for (int k = 0; k <= K; ++k) {
            // a[i] を選ばない場合
            if (dp[i][j][k])
                dp[i+1][j][k] = true;
                
            // a[i] を選ぶ場合
            if (j >= a[i] && k >= 1 && dp[i][j-a[i]][k-1])
                dp[i+1][j][k] = true;
        }
    }
}
