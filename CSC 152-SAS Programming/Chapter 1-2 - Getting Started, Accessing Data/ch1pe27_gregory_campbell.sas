** Compute Body Mass Index using pounds and inches;
DATA bodymass;
	Gender = 'Male';	* type Char;
	Weight = 170;		* type Numeric;
	Height = 68;		* type Numeric;
	BMI = (Weight / Height ** 2) * 703;	 * type Numeric;
	* for this example the bmi is 22.804930796;
Proc print;
Run;