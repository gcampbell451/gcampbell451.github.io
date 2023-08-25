* name must be read in as character, all other variables are numeric;
data mountains;
infile "~/sasuser.v94/Chapter2/Mountains.dat" ENCODING=wlatin1;
input Name & $ heightM & COMMA4. heightFT & COMMA5. FirstAscent & ProminenceM COMMA6.;
run;

proc print data = mountains;
run;