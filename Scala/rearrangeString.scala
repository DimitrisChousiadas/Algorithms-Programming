/*
    Given a string with N characters, we want to find out if we can rearrange the characters in such a way,
    so that no two adjacent characters are the same.
    This is possible, if and only if no character appears more than (N+1)/2 times in the string.

    Given the string input, then, we first create a list with (character, frequency) pairs, with the frequency of
    appearance of each character, in descending order of the frequency.
    If the frequency of the head of the list is greater than (N+1)/2, the string cannot be rearranged.

    If, on the other hand, it is not, then we put all the pairs in a priority queue.
    Then, until the priority queue is empty, we perform the following two operations:
        - we dequeue the first element of the queue, that is the (char, freq) pair with the greates frequency,
          and we append the char to the partial result acc, which is a List[Char].
        - we dequeue, again, the first element of the queue and we append to the partial result the second character,
          which is, obviously, different than the first character. Thus, we make sure that we don't place two same characters
          next to each other.
        - then, we decrease the frequencies of these two characters by one and we place them back in the queue, in the same order that we dequeued them.
          This way, we make sure that, in case of ties, i.e. characters with the same frequency, we are not placing two same characters in a row.
          If any of the new frequencies is 0, we skip the enqueuing of the respective character, since we are done with it.
        - we repeat, until the queue is empty, at which moment we convert the acc into a string and we print it.
*/

import scala.annotation.tailrec
import scala.collection.mutable.PriorityQueue

object RearrangeString extends App {

    def ordering (el: (Char, Int)) : Int = el._2

    @tailrec
    def enqueueChars (freqs: List[(Char, Int)], q: PriorityQueue[(Char, Int)]) : PriorityQueue[(Char, Int)] = freqs match {
        case Nil => q
        case h::t =>
            q.enqueue(h)
            enqueueChars(t, q)
    }

    def rearrange (acc: List[Char], q: PriorityQueue[(Char, Int)], len: Int) : String = {
        if (q.isEmpty) acc.mkString
        else if (len == 1) (q.dequeue._1::acc).mkString
        else {
            val (ch1, counter1) = q.dequeue
            val (ch2, counter2) = q.dequeue
            var l = len
            if (counter1 > 1) q.enqueue((ch1, counter1-1)) else l = l - 1
            if (counter2 > 1) q.enqueue((ch2, counter2-1)) else l = l - 1
            rearrange(ch2::ch1::acc, q, l)
        }
    }

    println("Enter the string that you want to rearrange:")

    val charLs = scala.io.StdIn.readLine.toList // the list of characters in the input string
    val freqs = charLs.groupBy(ch => ch).toList.map( el => (el._1, el._2.length)).sortWith(_._2 > _._2)

    // freqs is a list with (character, frequency) pairs, sorted in descending order of frequency.
    // If no character appears more than (n+1)/2 times in the string, where n is the length of the string,
    // then there is a way to rearrange the string, so that no two adjacent characters are the same.

    if (freqs(0)._2 > (charLs.length + 1)/2) println("The string cannot be rearranged!")
    else {
        println("The string can be rearranged!")
        val q = enqueueChars(freqs, new PriorityQueue[(Char, Int)]()(Ordering.by(ordering)))
        println(rearrange(List(), q, q.length))
    }

}
