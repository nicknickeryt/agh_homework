using System.Linq.Expressions;
using System.Reflection.Metadata.Ecma335;
using System.Runtime.CompilerServices;
using B6;

namespace B7
{
    class Program
    {
        static void Main(string[] args)
        {
            List<HighestPeak> list = Homework.CreateList();
            
            // A. (1 pkt) Proszę sprawdzić, jaki jest najwyższy szczyt Austrii i wyświetlić jego dane na ekranie.
            for(int i = 0; i < list.Count; i++)
            {
                if(list[i].Country.Equals("Austria")) list[i].ShowInfo();
            }

            // B. (1 pkt) Proszę sprawdzić, jaki szczyt znajduje się na przedostatniej pozycji listy i wyświetlić jego dane na ekranie.
            list[list.Count-2].ShowInfo();

            // C. (2 pkt) Proszę obliczyć średnią arytmetyczną wysokości szczytów zapisanych na liście i wyświetlić ją na ekranie.
            int sum = 0;

            for(int i = 0; i < list.Count; i++)
            {
                sum+=list[i].Elevation;
                //heightList.Add(list[i].Elevation);
            }

            Console.WriteLine(sum/list.Count);


            //D. (2 pkt) Proszę wypisać na ekranie wszystkie szczyty o wysokości pomiędzy 4000 metrów a 5000 metrów.
            for(int i = 0; i < list.Count; i++)
            {   
                int elevation = list[i].Elevation;
                if(elevation > 4000 && elevation < 5000){
                    list[i].ShowInfo();
                }
            }



            Dictionary<string, double> dictionary = Homework.CreateDictionary();

            //F. (1 pkt) Proszę odnaleźć kraj o liczbie mieszkańców 5.5 miliona i wyświetlić jego nazwę na ekranie.
            foreach (KeyValuePair<string, double> entry in dictionary) {
                if(entry.Value == 5.5) Console.WriteLine(entry.Key);    
            }

            //G. (1 pkt) Proszę dodać do słownika nowy fikcyjny kraj o wybranych przez siebie parametrach i wyświetlić na ekran nową ilość pozycji w słowniku.
            dictionary.Add("Yugoslavia", 10.5);
            Console.WriteLine(dictionary.Count);

            //H. (2 pkt) Proszę obliczyć średnią arytmetyczną populacji zapisanych w słowniku i wyświetlić ją na ekranie.
            dictionary.Remove("Yugoslavia"); // Usunięcie poprzednio dodanego kraju dla poprawnego wyniku zadania.

            double sumD = 0;
            foreach (KeyValuePair<string, double> entry in dictionary) {
                sumD+=entry.Value;
            }

            Console.WriteLine(sumD/dictionary.Count);

            //I. (2 pkt) Proszę wypisać na ekranie wszystkie kraje o populacji pomiędzy 10 milionów a 20 milionów
            foreach (KeyValuePair<string, double> entry in dictionary) {
                if(entry.Value > 10 && entry.Value < 20) {
                    Console.WriteLine(entry.Key);
                }
            }

            //J. (2 pkt) Proszę w jednej linijce wypisać na ekran sumę populacji wszystkich krajów bałtyckich (Lithuania, Latvia, Estonia).
            Console.WriteLine(dictionary["Lithuania"] + dictionary["Latvia"] + dictionary["Estonia"]);
        }
    }
}