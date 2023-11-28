namespace B6
{
    class Ship
    {

        private int defaultShipMass = 50;
        private Engine defaultShipEngine = new Engine(Fuel.Diesel);

        public Engine Engine
        {
            get;
            set;
        }
        public int MasaStatku
        {
            get;
            set;
        }

        public Ship()
        {
            Engine = defaultShipEngine;
            MasaStatku = defaultShipMass;
        }

        public Ship(Engine engine, int masaStatku)
        {
            MasaStatku = masaStatku;
            if (masaStatku <= 0)
            {
                Console.WriteLine("Ship mass must be positive! Setting the default one (" + defaultShipMass + ")");
                MasaStatku = defaultShipMass;
            }
            Engine = engine;
        }

        public bool TravelOffer(Destination destination, Product p1, Product p2)
        {
            int sellPrice = p1.getCurrentValue() + p2.getCurrentValue();
            int totalMass = p1.Mass + p2.Mass;
            int travelPrice = Engine.TravelCost(destination.Distance, totalMass);

            bool isProfitable = sellPrice - travelPrice >= 1000 ? true : false;

            if (isProfitable)
            {
                Console.WriteLine("Destination accepted: " + destination.Name);

                Console.WriteLine("Transporting:");
                Console.WriteLine(p1.Name + ", " + p1.Mass + " tons");
                Console.WriteLine(p2.Name + ", " + p2.Mass + " tons");

                Console.Write("Travel time: " + Engine.TravelTime(destination.Distance, totalMass) + " hours, ");

                Console.Write("total value: " + sellPrice + ", ");

                Console.WriteLine("travel cost: " + travelPrice + "\n");
            }
            else
            {
                Console.WriteLine("Travelling to " + destination.Name + " is too expensive\n");
            }

            return isProfitable;

        }
    }
}