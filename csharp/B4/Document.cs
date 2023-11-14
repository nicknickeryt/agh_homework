public enum EyeColor
{
    BROWN,
    BLACK,
    BLUE,
    GREEN
}

//TODO Imie, Nazwisko can be null

class Document
{

    public string Imie
    {
        get;
        set;
    }
    public string Nazwisko
    {
        get;
        set;
    }

    private EyeColor eyeColor;

    public EyeColor GetEyeColor()
    {
        return eyeColor;
    }
    public void SetEyeColor(EyeColor color)
    {
        eyeColor = color;
    }

    public int ExpirationDate
    {
        get;
        set;
    }


}