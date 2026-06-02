module LuciansLusciousLasagna

// TODO: define the 'expectedMinutesInOven' binding
let expectedMinutesInOven: int = 40
let preparationTimePerLayer: int = 2
// TODO: define the 'remainingMinutesInOven' function
let remainingMinutesInOven (minutesInOven: int): int = expectedMinutesInOven - minutesInOven
// TODO: define the 'preparationTimeInMinutes' function
let preparationTimeInMinutes (numberOfLayers: int): int = preparationTimePerLayer * numberOfLayers
// TODO: define the 'elapsedTimeInMinutes' function
let elapsedTimeInMinutes (numLayers: int) (actualMinutesInOven:int): int = preparationTimeInMinutes(numLayers) + actualMinutesInOven
