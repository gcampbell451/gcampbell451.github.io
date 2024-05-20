using Packt.Shared; // to use Viper
using System.IO.Compression; // to use BrotliStream, BZipStream
using System.Xml;
using System.Xml.Schema; // to use XmlWriter, XmlReader

partial class Program
{
    private static void Compress(string algorithm = "gzip")
    {
        // define a file path using the algorithm as file extension
        string filePath = Combine(
            CurrentDirectory, $"streams.{algorithm}");

        FileStream file = File.Create(filePath);
        Stream compressor;
        if (algorithm == "gzip")
        {
            compressor = new GZipStream(file, CompressionMode.Compress);
        }
        else
        {
            compressor = new BrotliStream(file, CompressionMode.Compress);
        }

        using (compressor)
        {
            using (XmlWriter xml = XmlWriter.Create(compressor))
            {
                xml.WriteStartDocument();
                xml.WriteStartElement("callsigns");
                foreach (string item in Viper.Callsigns)
                {
                    xml.WriteElementString("callsign", item);
                }
            }
        } // also closes the underlying stream

        OutputFileInfo(filePath);

        // read the compressed file
        WriteLine("Reading the compressed XML file:");
        file = File.Open(filePath, FileMode.Open);
        Stream decompressor;
        if (algorithm == "gzip")
        {
            decompressor = new GZipStream(file, CompressionMode.Decompress);
        }
        else
        {
            decompressor = new BrotliStream(file, CompressionMode.Decompress);
        }

        using (decompressor) 
        using (XmlReader reader = XmlReader.Create(decompressor))
        
        while (reader.Read())
        {
            // check if we are on an element node named callsign
            if ((reader.NodeType == XmlNodeType.Element) && (reader.Name == "callsign"))
                {
                    reader.Read(); // move to the text inside element
                    WriteLine($"{reader.Value}"); // read its value
                }

            // alternative syntax with proterty pattern matching:
            // if (reader is { NodeType: XmlNodeType.Element, Name: "Callsign" })
        }
    }
}