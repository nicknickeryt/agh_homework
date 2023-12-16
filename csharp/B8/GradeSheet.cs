using System;
using System.Collections.Generic;
using System.Text.Json;

namespace B8
{

    public enum Grupa
    {
        GRUPA_1,
        GRUPA_2,
        GRUPA_3
    }
    class GradeSheet
    {
        private JsonSerializerOptions opts = new JsonSerializerOptions() { WriteIndented = true };
        public string NameSurname { get; set; }
        public Grupa Group { get; set; }

        public Dictionary<string, float> GradeDictionary { get; set; }

        public double AverageGrade()
        {
            double sum = 0;
            int n = GradeDictionary.Count;
            foreach (KeyValuePair<string, float> kvp in GradeDictionary)
            {
                sum += kvp.Value;
            }
            return sum / n;
        }

        public void Serialize(string filePath)
        {
            string gradesToJson = JsonSerializer.Serialize(this, opts);
            try
            {
                File.WriteAllText(filePath, gradesToJson);
            }
            catch (Exception)
            {
                Console.WriteLine("Nie ma takiego pliku lub nie jest dostępny.");
            }
        }

        public static GradeSheet Deserialize(string filePath)
        {
            try {
                string jsonFromFile = File.ReadAllText(filePath);
                GradeSheet gradesFromJson = JsonSerializer.Deserialize<GradeSheet>(jsonFromFile);
                return gradesFromJson;
            } catch (Exception) {
                Console.WriteLine("Nie ma takiego pliku lub nie jest dostępny.");
            }
            return null;
        }
    }
}