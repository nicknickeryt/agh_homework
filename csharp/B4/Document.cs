namespace B4;

// Przykładowe kolory oczu
public enum EyeColor {
    BROWN,
    BLACK,
    BLUE,
    GREEN
}

class Document {

    private int expirationDate;

    public Document(Person person) {  
        Name = person.Name;
        Surname = person.Surname;
        EyeColor = person.EyeColor;
    }

    public string Name {
        get;
        set;
    }
    public string Surname {
        get;
        set;
    }

    public EyeColor EyeColor {
        get;
        set;
    }

     /*
      * Getter i setter dla expirationDate.
      * Sprawdza podaną wartość i, jeśli jest nierealistyczna, wypisuje błąd na ekran.
      */
    public int ExpirationDate {
        get {
            return expirationDate;
        }
        set {
            if(value < 1900 || value > 2100) { 
                Console.WriteLine("Podano niepoprawny rok."); 
            } else { 
                expirationDate = value; 
            }
        }
    }

}