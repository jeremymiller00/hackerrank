    def divisibleSumPairs(n: Int, k: Int, ar: Array[Int]): Int = {

        var result = 0
        val end = ar.size - 1
        for (i <- 0 to (end - 1)) {
            for (j <- (i+1) to (ar.size - 1)) {
                if ( (ar(i) + ar(j)) % k == 0 ) {
                    result += 1
                } 
            }
        }
        return result

    }