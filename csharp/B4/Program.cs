//TODO Cleanup a bit
//TODO check everything
namespace B4;

class Program
{

    static void Main(string[] args)
    {

        Wallet wallet = new Wallet();

        wallet.Dowod.Imie = "Jan";
        wallet.Dowod.Nazwisko = "Kowalski";
        wallet.Dowod.SetEyeColor(EyeColor.BROWN);
        wallet.Dowod.ExpirationDate = 2030;

        wallet.Legitka.Imie = "Jan";
        wallet.Legitka.Nazwisko = "Kowalski";
        wallet.Legitka.SetEyeColor(EyeColor.BROWN);
        wallet.Legitka.ExpirationDate = 2019;

        wallet.CheckDate(2023);

    }

}
