namespace B4;

 /*
  * Klasa Person zarządza danymi osobowymi dla uproszczenia kodu, gdyż każdy dokument jest na takie same dane osobowe,
  * więc wystarczy podać je tylko raz, by utworzyć obiekt Person i przekazać go do dowolnej liczby obiektów klasy Document.
  */
class Person {

    
    public required string Name {
        get;
        set;
    }
    public required string Surname {
        get;
        set;
    }

    public EyeColor EyeColor {
        get;
        set;
    }

}