namespace B5 {

    class Program {

        static void Main(string[] args){

            // Kilka obiektów do testów
            MenuItem menuItem1 = new MenuItem("Zupa pomidorowa", 5.0f);
            MenuItem menuItem2 = new MenuItem("Krupnik", 4.0f);
            MenuItem copiedItem = new MenuItem(menuItem2);

            // Wypisanie łącznej wartości potraw
            Console.WriteLine("Total order: " + MenuItem.TotalOrder);
            
            // Wypisanie informacji o wszystkich potrawach
            Console.WriteLine("Item 1: \n » Name: " + menuItem1.ItemName + "\n » Price: " + menuItem1.Price);
            Console.WriteLine("Item 2: \n » Name: " + menuItem2.ItemName + "\n » Price: " + menuItem2.Price);
            Console.WriteLine("CopiedItem: \n » Name: " + copiedItem.ItemName + "\n » Price: " + copiedItem.Price);
        }

    }
}