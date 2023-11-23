namespace B6
{
    class Product {
        
        private int CurrentPrice;

        private int mass;

        public string Name {
            get;
        }

        public int Mass {
            get { return mass; }
            set {
                if (value >= 0) mass = value;
            }
        }

        public Product(string name) {
            Name = name;
            Mass = 0;
            CurrentPrice = WorldMarket.GetInitialPricePerKg();
        }

        public Product(string name, int mass) {
            Name = name;
            Mass = mass;
            CurrentPrice = WorldMarket.GetInitialPricePerKg();
        }

        public int getCurrentValue() {
            return WorldMarket.GetNewPricePerKg(CurrentPrice)*Mass;
        }

    }

}