def squareRoot(x: Double): Double = {
    def abs(x: Double) = if (x < 0) - x else x
    var y = 1.0
    while (abs(y * y - x ) < 0.0001) {
        y = (y + ( x/y) ) / 2.0
        }
    return y
    }