    def divisibleSumPairs(n: Int, k: Int, ar: Array[Int]): Int = {

      val indexPairs = ar.indices.flatMap(i => ar.indices.slice(i + 1, ar.length).map(j => (i, j)))

      val divisible = indexPairs.count(pair => (ar(pair._1) + ar(pair._2)) % divisor == 0)        
      return divisible
    }
