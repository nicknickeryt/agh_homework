namespace B4;
class Wallet {

    private Document idCard;
    private Document studentIdCard;

    /*
     * Inicjalizacja portfela z argumentem tworzy dwa dokumenty z podanymi danymi osobowymi
     */ 
    public Wallet(Person person) {  
        idCard = new Document(person);
        studentIdCard = new Document(person);
    }

    public Document IdCard {
        get { return idCard; }
        set { idCard = value; }
    }

    public Document StudentIdCard {
        get { return studentIdCard; }
        set { studentIdCard = value; }
    }

    // Spawdzanie, czy dokumenty wygasły
    public void CheckDate(int year) {
        
        // Lista wiadomości do wypisania na koniec funkcji dla uproszczenia kodu.
        List<string> strings = new List<string>() {"Status dokumentów na rok " + year + ":"};

        if (year > idCard.ExpirationDate) strings.Add(" Dowod wygasl.");
        if (year > studentIdCard.ExpirationDate) strings.Add(" Legitymacja wygasla.");
        if(strings.Count == 1) strings.Add(" Wszystkie dokumenty są ważne.");

        foreach (String s in strings) {
            Console.WriteLine(s);
        }
    }

}