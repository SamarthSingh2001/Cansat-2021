// @file sensor.h
// @author Joshua Tenorio

class Sensor {
protected:
float initValue;

public:
// initializes the sensor.
// @param samples The number of samples to take the average of
// @return 1 when initialize is successful, 0 when initialize is not successful
virtual int initialize(int samples);

// gets the current value of the sensor
// @return The current value of the sensor
virtual float getValue();

// resets the sensor to zero.
// @return 1 if successful, 0 if not successful
virtual int reset();
};
