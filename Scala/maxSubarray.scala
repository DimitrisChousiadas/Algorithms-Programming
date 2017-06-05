// Kadane's Algorithm
// Given an array of integers, positive and negative, we want to find the maximum sum of any sub-array of the array.
// A sub-array is a set of contiguous elements of the array.
// For example, the array [−2, 1, −3, 4, −1, 2, 1, −5, 4] has a maximum sub-array sum of 6, which corresponds to the sub-array [4, -1, 2, 1].
// To do that we first observe that at a position i+1 of the array, the maximum sum of contiguous elements until the (i+1)th element
// is either the (i+1)th element itself, or the maximum sum of contiguous elements until i plus the (i+1)th element.
// As a result, we can traverse the array once and keep track of the current maximum sum until each point, as well as the global maximum sum sofar.
// Following, is a tail recursive implementation of the above algorithm, which takes O(n) time.

import scala.annotation.tailrec

object MaxSubarray extends App {
    
    @tailrec
    def maxSubarray (nums: List[Int], maxSofar: Int, maxUntilHere: Int) : Int = nums match {
        case Nil => maxSofar
        case h::t =>
            val newMaxUntilHere = math.max(maxUntilHere + h, h)
            // if maxUntilHere > 0 then add newMaxUntilHere = maxUntilHere + h else newMaxUntilHere = h
            val newMaxSofar = math.max(maxSofar, newMaxUntilHere)
            maxSubarray(t, newMaxSofar, newMaxUntilHere)
    }

    println("Enter the numbers:")
    val numbers = scala.io.StdIn.readLine.split("\\s+").map(_.toInt).toList
    println("The maximum sum of contiguous elements is:")
    println(maxSubarray(numbers.tail, numbers(0), numbers(0)))

}
