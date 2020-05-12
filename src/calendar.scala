    def dayOfProgrammer(year: Int): String = {
        if (year > 1918) {
            if (year % 400 == 0 || (year % 4 == 0 && year % 100 != 0)) {
                return "12.09." + year.toString
            } else {
                return "13.09." + year.toString
            }
        } else if (year < 1918) {
            if (year % 4 == 0) {
                return "12.09." + year.toString
            } else {
                return "13.09." + year.toString
            }
        } else {
            return "26.09." + year.toString
        }
    }