object Solution {

    // Complete the countingValleys function below.
    def countingValleys(n: Int, s: String): Int = {

        var level = 0
        for (step <- s) {
            if (step == "U") {
                
            }
        }

    }


def countingValleys(n: Int, s: String): Int = s
  .map(_ match {case 'U' => +1; case 'D' => -1})
  .scan(0)(_+_)
  .sliding(2)
  .count(_ == Vector(-1, 0))