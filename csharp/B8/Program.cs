namespace B8
{
    class Program
    {
        static void Main(string[] args)
        {
            // Inicjalizacja, przykładowy obiekt GradeSheet
            GradeSheet gradeSheet = new GradeSheet();

            gradeSheet.NameSurname = "Jaś Kowalski";
            gradeSheet.GradeDictionary = new Dictionary<string, float>{
                {"analiza", 1},
                {"algebra", 5}
                };
            gradeSheet.Group = StudentGroup.GROUP_3;

            Console.WriteLine(gradeSheet.NameSurname);
            Console.WriteLine(gradeSheet.Group);
            Console.WriteLine(gradeSheet.AverageGrade());

            string fileName = @"/home/nick/Dokumenty/AGH/infa/agh_homework/csharp/B8/testGradeSheet.json";
            string wrongFileName = @"wrongFileName.json";


            gradeSheet.Serialize(fileName);

            // Deserializacja do nowego obiektu
            GradeSheet gradeSheet1 = GradeSheet.Deserialize(fileName);


            // Sprawdzenie czy nie jest null (null, jeśli nie można odczytać pliku)
            if (gradeSheet1 != null)
            {
                Console.WriteLine(gradeSheet1.NameSurname);
                Console.WriteLine(gradeSheet1.Group);
                Console.WriteLine(gradeSheet1.AverageGrade());
            }

            // Próba odczytania pliku, który nie istnieje
            GradeSheet gradeSheet2 = GradeSheet.Deserialize(fileName);
        }
    }
}