using System;
using System.Collections.Generic;
using System.Text.Json;

namespace B8
{

    public enum StudentGroup
    {
        GROUP_1,
        GROUP_2,
        GROUP_3
    }
    class GradeSheet
    {
        private static string errorCode = "Deserialize » Cannot access file.";
        private JsonSerializerOptions opts = new JsonSerializerOptions() { WriteIndented = true };
        public string NameSurname { get; set; }
        public StudentGroup Group { get; set; }

        public Dictionary<string, float> GradeDictionary { get; set; }

        public double AverageGrade()
        {
            double sum = 0;
            foreach (KeyValuePair<string, float> kvp in GradeDictionary)
            {
                sum += kvp.Value;
            }
            return sum / GradeDictionary.Count;
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
                Console.WriteLine(errorCode);
            }
        }

        public static GradeSheet Deserialize(string filePath)
        {
            try {
                string jsonFromFile = File.ReadAllText(filePath);
                GradeSheet gradesFromJson = JsonSerializer.Deserialize<GradeSheet>(jsonFromFile);
                return gradesFromJson;
            } catch (Exception) {
                Console.WriteLine(errorCode);
            }
            return null;
        }
    }
}