    def migratoryBirds(arr: Array[Int]): Int = {
        val srtd = arr.sorted 
        val counts = srtd.distinct.map(x => { (x, srtd.filter(_ == x).size) } )
        val maxCount = counts.map(p => p._2).max
        val candidates = counts.filter(p => {p._2 == maxCount})
        val result = candidates.map(c => c._1).min
        return result
    }