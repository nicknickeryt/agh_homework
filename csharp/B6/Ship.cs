namespace B6
{
    class Ship {

        private static int defaultShipMass = 50;

        public Engine Engine{
            get;
            set;
        }
        private int MasaStatku {
            get;
            set;
        }

        public Ship() {
            Engine = new Engine(Fuel.Diesel);
            MasaStatku = defaultShipMass;
        }

        public Ship(Engine engine, int masaStatku) {
            MasaStatku = masaStatku;
            if(masaStatku <=0){
                Console.WriteLine("Masa statku musi być dodatnia! Ustawianie domyślnej.");
                MasaStatku = defaultShipMass;
            } 
            Engine = engine;
        }

        public bool TravelOffer(Destination destination, Product productOne, Product productTwo) {
            int sellPrice = productOne.getCurrentValue() + productTwo.getCurrentValue();
            int totalMass = productOne.Mass + productTwo.Mass;
            int travelPrice = Engine.TravelCost(destination.Distance, totalMass);

            bool oplacalne = sellPrice - travelPrice >= 1000 ? true : false;

            if(oplacalne) {
                Console.WriteLine("Oferta zaakceptowana!");

                Console.WriteLine("Zawartość ładunku:");
                Console.WriteLine(productOne.Name + ", " + productOne.Mass);
                Console.WriteLine(productTwo.Name + ", " + productTwo.Mass);

                Console.WriteLine("Czas podróży:");
                Console.WriteLine(Engine.TravelTime(destination.Distance, totalMass));

                Console.WriteLine("Cena sprzedaży:");
                Console.WriteLine(sellPrice);

                Console.WriteLine("Koszty podróży:");
                Console.WriteLine(travelPrice);
            } else {
                Console.WriteLine("Oferta zbyt droga!");
            }

            return oplacalne;

        }
    }
}