    def getMoneySpent(keyboards: Array[Int], drives: Array[Int], b: Int): Int = {
        /*
         * Write your code here.
         */
         val cross = keyboards.flatMap(x => drives.map(y => (x, y)))
         val lessThan = cross.filter(_ <= b)
         if lessThan.size == 0 return -1
         return lessThan.max
    }