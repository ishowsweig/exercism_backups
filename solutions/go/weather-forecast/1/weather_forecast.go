// Package weather provides logic to output the weather forecast in a given location.
package weather

var (
    // CurrentCondition represents the current weather condition.   
    CurrentCondition string
    // CurrentLocation represents the location in which the weather is being requested.
	CurrentLocation  string
)

// Forecast returns a formatted string value representing the weather forecast of a given location.
func Forecast(city, condition string) string {
	CurrentLocation, CurrentCondition = city, condition
	return CurrentLocation + " - current weather condition: " + CurrentCondition
}
