int counter = 0;
for (int X = 0; X <= K; ++X) {
    for (int Y = 0; Y <= K; ++Y) {
        for (int Z = 0; Z <= K; ++Z) {
            if (X + Y + Z == N) ++counter;
        }
    }
}
