package raindrops

import "strconv"

func Convert(number int) string {
    var output string
    switch {
    case number%3 == 0 && number%5 == 0 && number%7 == 0:
        output = "PlingPlangPlong"
    case number%5 == 0 && number%7 == 0:
        output = "PlangPlong"
    case number%3 == 0 && number%7 == 0:
        output = "PlingPlong"
    case number%3 == 0 && number%5 == 0:
        output = "PlingPlang"
    case number%7 == 0:
        output = "Plong"
    case number%5 == 0:
        output = "Plang"
    case number%3 == 0:
        output = "Pling"
    default:
        output = strconv.Itoa(number)
    }
    return output
}