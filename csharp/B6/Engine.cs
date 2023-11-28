﻿namespace B6
{

    public enum Fuel
    {
        Diesel,
        Hydrogen,
        Nuclear
    }

    class Engine
    {
        // klasa reprezentujaca silnik statku

        // wlasciwosc - typ paliwa
        public Fuel EngineFuel { get; private set; }

        // konstruktor ustawiajacy typ paliwa
        public Engine(Fuel f)
        {
            EngineFuel = f;
        }

        // funkcja obliczajaca czas podrozy w zaleznosci od podanego dystansu i masy lodzi podwodnej
        // distance - podawany w km, mass - podawana w tonach, travelTime - zwracany w godzinach
        public int TravelTime(int distance, int mass)
        {
            int travelTime;
            switch (EngineFuel)
            {
                // tak bedzie dzialal nasz wymyslony silnik na diesel
                case Fuel.Diesel:
                    if (mass < 10)
                    {
                        travelTime = distance / 60;
                    }
                    else if (mass < 40)
                    {
                        travelTime = distance / (60 - (mass - 10));
                    }
                    else
                    {
                        travelTime = distance / 30;
                    }
                    break;
                // teraz silnik jadrowy
                case Fuel.Nuclear:
                    if (distance < 120)
                    {
                        travelTime = distance / 30;
                    }
                    else
                    {
                        if (mass < 50)
                        {
                            travelTime = (distance - 120) / 50 + 4;
                        }
                        else
                        {
                            travelTime = (distance - 120) / 40 + 4;
                        }
                    }
                    break;
                // i wreszcie wodorowy
                case Fuel.Hydrogen:
                    int velocity = 600 / (10 + mass);
                    if (velocity < 20) velocity = 20;
                    travelTime = distance / velocity;
                    break;
                default:
                    travelTime = -1;
                    break;
            }
            return travelTime;
        }

        // metoda obliczajaca koszt podrozy dla tych samych parametrow
        public int TravelCost(int distance, int mass)
        {
            // koszt podrozy zalezy od czasu podrozy
            int cost;
            int time = TravelTime(distance, mass);
            // a takze od ceny danego paliwa
            switch (EngineFuel)
            {
                case Fuel.Diesel:
                    cost = time * 100;
                    break;
                case Fuel.Nuclear:
                    cost = time * 15;
                    break;
                case Fuel.Hydrogen:
                    cost = time * 30;
                    break;
                default:
                    cost = -1;
                    break;
            }
            return cost;
        }
    }

}
