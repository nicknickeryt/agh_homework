// Its ok ig
class Wallet
{

    private Document dowod = new Document();
    private Document legitka = new Document();

    public Document Dowod
    {
        get { return dowod; }
        set { dowod = value; }
    }

    public Document Legitka
    {
        get { return legitka; }
        set { legitka = value; }
    }

    public void CheckDate(int year)
    {
        if (year > dowod.ExpirationDate) Console.WriteLine("Dowod wygasl");
        if (year > legitka.ExpirationDate) Console.WriteLine("Legitka wygasla");
    }
}