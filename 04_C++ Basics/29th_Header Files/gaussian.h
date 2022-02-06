/*
You were introduced to header files in the previous lesson. Header files allowed you to put function declarations in a separate file. 
Ultimately, using and including header files makes it easier to re-use functions in different parts of your program. Furthermore, 
if the class declaration changes, you only have to change the declaration in one place.

For classes, header files serve the exact same purpose. When you use the Gaussian class in main.cpp, you can simply include the header file at the top include "gaussian.h".
 That gives main.cpp access to the Gaussian class.

Likewise, for gaussian.cpp, you can include the header file as well rather than writing out the entire declaration.


*/


class Gaussian
{
	private:
		float mu, sigma2;

	public:
		
		// constructor functions
		Gaussian ();
		Gaussian (float, float);

		// change value of average and standard deviation 
		void setMu(float);
		void setSigma2(float);

		// output value of average and standard deviation
		float getMu();
		float getSigma2();

		// functions to evaluate 
		float evaluate (float);
		Gaussian mul (Gaussian);
		Gaussian add (Gaussian);
};