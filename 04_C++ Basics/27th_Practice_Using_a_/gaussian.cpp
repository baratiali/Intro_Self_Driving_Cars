#include <math.h>       /* sqrt, exp */

// class declaration
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

//The first constructor function is for when you instantiate an object without specifying the average and variance.:
Gaussian::Gaussian() {
	mu = 0;
	sigma2 = 1;	
}

//The other constructor function specifies what to do when you do specify the average and variance:
Gaussian::Gaussian (float average, float sigma) {
	mu = average;
	sigma2 = sigma;
}
/*
Class Methods
And finally, the class methods define all of the functions that your class needs to have.

The rest of the code contains the definitions for all of the functions, also called methods, that your class has.

The get and set functions are specifically for getting variable values or changing the value of private variables. Again, we'll go into more detail about private and public later in the lesson.
*/
void Gaussian::setMu (float average) {
	mu = average;
}

void Gaussian::setSigma2 (float sigma) {
	sigma2 = sigma;
}


float Gaussian::getMu () {
	return mu;
}

float Gaussian::getSigma2() {
	return sigma2;
}

float Gaussian::evaluate(float x) {
	float coefficient;
	float exponential;

	coefficient = 1.0 / sqrt (2.0 * M_PI * sigma2);
	exponential = exp ( -0.5 * pow ((x - mu), 2) / sigma2 );
	return coefficient * exponential;
}

Gaussian Gaussian::mul(Gaussian other) {
	float denominator;
	float numerator;
	float new_mu;
	float new_var;

	denominator = sigma2 + other.getSigma2();
	numerator = mu * other.getSigma2() + other.getMu() * sigma2;
	new_mu = numerator / denominator;

	new_var = 1.0 / ( (1.0 / sigma2) + (1.0 / other.sigma2) );

	return Gaussian(new_mu, new_var);
}

Gaussian Gaussian::add(Gaussian other) {

	float new_mu;
	float new_sigma2;

	new_mu = mu + other.getMu();
	new_sigma2 = sigma2 + other.getSigma2();

	return Gaussian(new_mu, new_sigma2);
}