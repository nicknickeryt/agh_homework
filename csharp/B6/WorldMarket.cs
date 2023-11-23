using System;

namespace B6
{
    class WorldMarket {
        public static int GetInitialPricePerKg() {
            return new Random().Next(100, 1000);
        }

        public static int GetNewPricePerKg(int currentPrice) {
            return currentPrice + new Random().Next(-50, 200);
        }
    }
}