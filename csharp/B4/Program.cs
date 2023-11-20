namespace B4;
 /*
  * Główna część programu.
  * Zawiera przykładowe dane i testuje klasy.
  */
class Program {

    static void Main(string[] args) {
        
        /*
         * Obiekt person przechowuje dane osobowe dla uproszczenia kodu.
         * Każdy dokument danej osoby ma bowiem te same dane, jedyną zmienną jest data ważności
         */
        Person person = new Person {Name="Jan", Surname="Kowalski", EyeColor=EyeColor.BROWN};

        // Utworzenie porfela z danymi osobowymi/
        Wallet wallet = new Wallet(person);

        // Ustawienie daty ważności dokumentów.
        wallet.IdCard.ExpirationDate = 2030;
        wallet.StudentIdCard.ExpirationDate = 2019;

        // Kilka dat do przetestowania 
        wallet.CheckDate(2023); // legitymacja wygasła
        wallet.CheckDate(2019); // nic nie wygasło
        wallet.CheckDate(2020); // legitymacja wygasła
        wallet.CheckDate(2029); // legitymacja wygasła
        wallet.CheckDate(2030); // legitymacja wygasła
        wallet.CheckDate(2031); // wszystko wygasło

    }

}
