namespace B6
{
    class Destination
    {
        public int Distance { get; set; }
        public string Name { get; set; }

        public Destination(int distance, string name)
        {
            Distance = distance;
            Name = name;
        }
    }
}