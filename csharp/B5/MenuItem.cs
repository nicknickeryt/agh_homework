namespace B5 {

    class MenuItem {

        // Statyczna wartość wszystkich zamówionych potraw
        public static float TotalOrder;

        // Nazwa potrawy
        public string ItemName {
            get;
            set;
        }

        // Cena potrawy
        public float Price {
            get;
            set;
        }

        // Konstruktor parametryczny tworzoący potrawę
        public MenuItem(string itemName, float price) {
            ItemName = itemName;
            Price = price;
            TotalOrder+=Price;
        }

        // Konstruktor kopiujący, przyjmuje jako argument potrawę i kopiuje jej właściwości do nowego obiektu
        public MenuItem(MenuItem menuItem) {
            ItemName = menuItem.ItemName;
            Price = menuItem.Price;
            TotalOrder+=Price;
        }

    }
}