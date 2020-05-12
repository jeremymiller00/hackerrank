    def bonAppetit(bill: Array[Int], k: Int, b: Int) {
        val annaTotal = (bill.patch(k, Nil, 1).sum / 2).toInt
        if (annaTotal == b) {
            println("Bon Appetit")
        } else {
            println( (b - annaTotal).toString)
        }
    }