﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace B6
{
    class Homework
    {
        public static List<HighestPeak> CreateList()
        {
            List<HighestPeak> highestPeaksOfEurope = new List<HighestPeak>()
            {
                new HighestPeak("Albania", "Korab", 2764),
                new HighestPeak("Andorra", "Coma Pedrosa", 2942),
                new HighestPeak("Austria", "Grossglockner", 3798),
                new HighestPeak("Belarus", "Dzyarzhynskaya Hara", 345),
                new HighestPeak("Belgium", "Signal de Botrange", 694),
                new HighestPeak("Bosnia and Herzegovina", "Maglić", 2386),
                new HighestPeak("Bulgaria", "Musala", 2925),
                new HighestPeak("Croatia", "Dinara", 1831),
                new HighestPeak("Cyprus", "Chionistra", 1952),
                new HighestPeak("Czechia", "Sněžka", 1603),
                new HighestPeak("Denmark", "Møllehøj", 171),
                new HighestPeak("Estonia", "Suur Munamägi", 318),
                new HighestPeak("Finland", "Halti", 1324),
                new HighestPeak("France", "Mont Blanc", 4809),
                new HighestPeak("Germany", "Zugspitze", 2962),
                new HighestPeak("Greece", "Olympos", 2917),
                new HighestPeak("Hungary", "Kékes", 1014),
                new HighestPeak("Iceland", "Hvannadalshnúkur", 2110),
                new HighestPeak("Ireland", "Carrauntoohil", 1041),
                new HighestPeak("Italy", "Monte Bianco", 4809),
                new HighestPeak("Kosovo", "Maja e Njeriut", 2658),
                new HighestPeak("Latvia", "Gaiziņkalns", 312),
                new HighestPeak("Liechtenstein", "Vorder Grauspitz", 2599),
                new HighestPeak("Lithuania", "Aukštojas", 294),
                new HighestPeak("Luxembourg", "Kneiff", 560),
                new HighestPeak("Malta", "Ta' Dmejrek", 253),
                new HighestPeak("Moldova", "Dealul Bălănești", 430),
                new HighestPeak("Monaco", "Chemin des Révoires", 163),
                new HighestPeak("Montenegro", "Zla Kolata", 2534),
                new HighestPeak("Netherlands", "Vaalserberg", 321),
                new HighestPeak("North Macedonia", "Korab", 2764),
                new HighestPeak("Norway", "Galdhøpiggen", 2469),
                new HighestPeak("Poland", "Rysy", 2499),
                new HighestPeak("Portugal", "Serra da Estrela", 1993),
                new HighestPeak("Romania", "Vârful Moldoveanu", 2544),
                new HighestPeak("Russia", "Elbrus", 5642),
                new HighestPeak("San Marino", "Monte Titano", 749),
                new HighestPeak("Serbia", "Midžor", 2169),
                new HighestPeak("Slovakia", "Gerlach", 2655),
                new HighestPeak("Slovenia", "Triglav", 2864),
                new HighestPeak("Spain", "Mulhacén", 3479),
                new HighestPeak("Sweden", "Kebnekaise", 2104),
                new HighestPeak("Switzerland", "Dufourspitze", 4634),
                new HighestPeak("Ukraine", "Hoverla", 2061),
                new HighestPeak("United Kingdom", "Ben Nevis", 1345),
            };
            return highestPeaksOfEurope;
        }
		
		public static Dictionary<string, double> CreateDictionary()
		{
			Dictionary<string, double> countryPopulationsEurope = new Dictionary<string, double>()
			{
				{ "Albania", 2.9 },
				{ "Andorra", 0.1 },
				{ "Austria", 8.8 },
				{ "Belarus", 9.5 },
				{ "Belgium", 11.3 },
				{ "Bosnia and Herzegovina", 3.5 },
				{ "Bulgaria", 7.1 },
				{ "Croatia", 4.3 },
				{ "Cyprus", 1.2 },
				{ "Czechia", 10.6 },
				{ "Denmark", 5.7 },
				{ "Estonia", 1.3 },
				{ "Finland", 5.5 },
				{ "France", 67.3 },
				{ "Germany", 82.8 },
				{ "Greece", 10.8 },
				{ "Hungary", 9.8 },
				{ "Iceland", 0.4 },
				{ "Ireland", 4.8 },
				{ "Italy", 60.6 },
				{ "Kosovo", 1.9 },
				{ "Latvia", 1.9 },
				{ "Liechtenstein", 0.1 },
				{ "Lithuania", 2.8 },
				{ "Luxembourg", 0.6 },
				{ "Malta", 0.4 },
				{ "Moldova", 3.4 },
				{ "Monaco", 0.1 },
				{ "Montenegro", 0.6 },
				{ "Netherlands", 17.3 },
				{ "North Macedonia", 2.1 },
				{ "Norway", 5.3 },
				{ "Poland", 38.4 },
				{ "Portugal", 10.4 },
				{ "Romania", 19.6 },
				{ "Russia", 144.5 },
				{ "San Marino", 0.1 },
				{ "Serbia", 7.0 },
				{ "Slovakia", 5.4 },
				{ "Slovenia", 2.0 },
				{ "Spain", 46.7 },
				{ "Sweden", 10.1 },
				{ "Switzerland", 8.4 },
				{ "Ukraine", 42.4 },
				{ "United Kingdom", 66.0 },
			};
			return countryPopulationsEurope;
		}
		
    }
}
