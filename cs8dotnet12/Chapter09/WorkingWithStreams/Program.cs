using Packt.Shared; // to use Viper
using System.Xml; // to use XmlWriter, etc

#region Writing to text streams

SectionTitle("Writing to text streams");

// define a file to write to 
string textFile = Combine(CurrentDirectory, "streams.txt");

// create a text file and return a helper writer
StreamWriter text = File.CreateText(textFile);

//  enumerate the strings, writing each one to the stream on a separate line
foreach (string item in Viper.Callsigns)
{
    text.WriteLine(item);
}
text.Close(); // to release unmanaged file resources

OutputFileInfo(textFile);

#endregion

#region Writing to XML streams

SectionTitle("Writing to XML streams");

// define a file path to write to 
string xmlFile = Combine(CurrentDirectory, "streams.xml");

// declare vars for the filestream and xml writer
FileStream? xmlFileStream = null;
XmlWriter? xml = null;

try {
    xmlFileStream = File.Create(xmlFile);

    // wrap the file stream in an xml writer helper and tell it to 
    // automatically indent nested elements
    xml = XmlWriter.Create(xmlFileStream, new XmlWriterSettings { Indent = true });

    // write the XML declaration
    xml.WriteStartDocument();

    // write a root element
    xml.WriteStartElement("callsigns");

    // enumerate the strings, writing each one to the stream
    foreach (string item in Viper.Callsigns)
    {
        xml.WriteElementString("callsign", item);
    }

    // write the close root element
    xml.WriteEndElement();
}
catch (Exception ex)
{
    // if the path doesn't exist the exception wil be caught
    WriteLine($"{ex.GetType()} says {ex.Message}");
}
finally
{
    if (xml is not null)
    {
        xml.Close();
        WriteLine("The XML writer's unmanaged resources have been disposed.");
    }

    if (xmlFileStream is not null)
    {
        xmlFileStream.Close();
        WriteLine("The file stream's unmanaged resources have been disposed.");
    }
}

OutputFileInfo(xmlFile);

#endregion

#region Compressing streams

SectionTitle("Compressing streams");
Compress(algorithm: "gzip");
Compress(algorithm: "brotli");

#endregion

