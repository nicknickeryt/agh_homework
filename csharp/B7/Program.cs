using System.Reflection.Metadata.Ecma335;
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
            List<int> heightList;
            for(int i = 0; i < list.Count; i++)
            {
                heightList.Add(list[i].Elevation);
            }



            for(int i = 0; i < list.Count; i++)
            {
                
            }
        }
    }
}