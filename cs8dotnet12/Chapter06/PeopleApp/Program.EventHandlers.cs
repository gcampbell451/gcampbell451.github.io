using Packt.Shared; // to use Person

// no namespace declaration so this extends the Program class in the null namespace

partial class Program
{
    // a method to handle the Shout event received by the harry object
    private static void Harry_Shout(object? sender, EventArgs e)
    {
        // if no sender, do nothing
        if (sender is null) return;

        // if sender is not a Person, do nothing
        if (sender is not Person p) return;

        WriteLine($"{p.Name} is this angry: {p.AngerLevel}.");
    }

    // another method to handle the event reeived by the harry object
    private static void Harry_Shout_2(object? sender, EventArgs e)
    {
        WriteLine("Stop it!");
    }
}