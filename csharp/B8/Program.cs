namespace B8
{
    class Program
    {
        static void Main(string[] args)
        {
            GradeSheet gradeSheet = new GradeSheet();

            gradeSheet.NameSurname = "Jaś Kowalski";
            gradeSheet.GradeDictionary = new Dictionary<string, float>{ {"analiza", 1} };
            gradeSheet.Group = Grupa.GRUPA_3;
            Console.WriteLine(gradeSheet.AverageGrade());

            gradeSheet.Serialize("/home/nick/Dokumenty/AGH/infa/agh_homework/csharp/B8/testowyJson.json");

            GradeSheet gradeSheet1 = GradeSheet.Deserialize("/home/nick/Dokumenty/AGH/infa/agh_homework/csharp/B8/testowyJson.json");


            Console.WriteLine(gradeSheet1.AverageGrade());
            Console.WriteLine(gradeSheet1.NameSurname);
            Console.WriteLine(gradeSheet1.Group);
        }
    }
}