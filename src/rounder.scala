def rounder(g: Int): Int = {
    // If distance to next multiple of five is < 2, round up
    val ones = List(3,4,8,9)
    if (ones.contains(g % 10)) {
        if ( ((g % 10) == 3 ) || ((g % 10) == 8) ) {
            return g + 2
        } else if ( ((g % 10) == 4) || ((g % 10) == 9) ) {
            return g + 1
        }
    }
    return g
}

def roundGrades(grades: Array[Int]): Array[Int] = {
    grades.map(x => if (x > 37) rounder(x) else x)
}

rounder(94)
rounder(38)
rounder(123432)
rounder(1)

roundGrades(Array(53, 56, 5))