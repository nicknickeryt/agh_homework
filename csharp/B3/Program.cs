using System;

namespace zadanie_b3;

class Program
{
    static void Main(string[] args)
    {
        DummyFourArgs(1, 2, 3, 4);
        Console.WriteLine(DummyDouble(1.0, 2.0));
        Console.WriteLine(DummyBool("agh", "agh"));
        Console.WriteLine(DummyString("a", "b"));
        Console.WriteLine(DummyE2(2));
        Console.WriteLine(PoleProstF1(1, 2, 3));
        Console.WriteLine(ObjetoscProstF2(1, 2, 3));
        Console.WriteLine(RecSum(5));

        Console.WriteLine(SumNum(40)); //sumNum(40) - test


        // Wywolanie funkcji #IsPrime dla liczb 2-100
        for (int i = 2; i <= 100; i++)
        {
            if (IsPrime(i)) Console.WriteLine(i);
        }

    }
    // A. (1 pkt) Dowolna funkcja przyjmująca cztery argumenty.
    static void DummyFourArgs(int a, int b, int c, int d)
    {
    }

    // B. (1 pkt) Dowolna funkcja o sygnaturze double NazwaFunkcji(double, double).
    static double DummyDouble(double a, double b)
    {
        return a * b;
    }

    // C. (1 pkt) Dowolna funkcja o sygnaturze bool NazwaFunkcji(string, string).
    static bool DummyBool(string a, string b)
    {
        return a == b;
    }

    // D. (1 pkt) Dowolna funkcja o sygnaturze string NazwaFunkcji(string, string).
    static string DummyString(string a, string b)
    {
        return a + b;
    }

    // E. (2 pkt) Dowolne dwie funkcje, z których jedna wywołuje w środku drugą oraz
    // wykorzystuje do czegoś wynik.
    static int DummyE1(int n)
    {
        return n * n;
    }

    static int DummyE2(int n)
    {
        if (n <= 0) return 1;
        return DummyE1(n - 1) * n;
    }

    // F. (2 pkt) Zestaw dwóch funkcji obliczających pole powierzchni i objętość dla wybranej
    // bryły geometrycznej.

    static int PoleProstF1(int a, int b, int h)
    {
        return 2 * a * h + 2 * b * h + 2 * a * b;
    }

    static int ObjetoscProstF2(int a, int b, int h)
    {
        return a * b * h;
    }

    // G. (3 pkt) Dowolna funkcja wykorzystująca do czegoś rekurencję, inna niż przykład z
    // instrukcji.
    static int RecSum(int n)
    {
        if (n == 0) return 0;
        return n + RecSum(n - 1);
    }
    // H. (3 pkt) Funkcja double Solution(double a, double b, double c), która zwróci dowolne
    // rozwiązanie równania kwadratowego ax2 + bx + c = 0. Jeżeli równanie nie ma
    // rzeczywistych rozwiązań, należy zwrócić wartość Double.NaN (skrót od Not a
    // Number).

    static double Solution(double a, double b, double c)
    {
        double delta = b * b - 4 * a * c;
        if (delta < 0) return Double.NaN;
        delta = Math.Sqrt(delta);

        List<double> solutions = new List<double>();
        solutions.Add((-b - delta) / (2 * a));
        if (delta > 0) solutions.Add((-b - delta) / (2 * a));

        return solutions[0];
        //return solutions[1];
    }

    // I. (4 pkt) Funkcja sumująca liczby od 1 do 40 podzielne przez 7, używająca rekurencji.
    // Odpowiedź: 105.
    static int SumNum(int n)
    {
        if (n < 7) return 0;
        if (n == 7) return 7;
        if (n % 7 != 0) n -= n % 7;

        if (n % 7 == 0)
        {
            return n + SumNum(n - 7);
        }
        return 0;
    }

    // Dodatkowa funkcja sprawdzajaca czy dana liczba jest pierwsza
    static bool IsPrime(int a)
    {
        for (int i = a - 1; i > 1; i--)
        {
            if (a % i == 0) return false;
        }
        return true;
    }
}

