﻿using static System.Console;

namespace CallStackExceptionHandlingLib;

    public class Processor
    {
        public static void Gamma() // public so it can be called from outside.
        {
        WriteLine("In Gamma");
        Delta();
        }

        private static void Delta() // private so it cn only be called internally
        {
        WriteLine("In Delta");
        File.OpenText("bad file path");
        }
    }

