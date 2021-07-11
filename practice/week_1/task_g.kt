fun main() {
    val (n, k, m) = readLine()!!.split(' ').map(String::toInt)
    println(getNumberOfDetails(n, k, m))
}

fun getNumberOfDetails(n: Int, k: Int, m: Int): Int {
    var details = 0
    fun calc(n: Int, k: Int, m: Int) {
        var _n = n 
        var details_per_blank = k / m
        var details_reminder = k % m
        while(_n >= k) {
            val blank = _n / k
            details += blank * details_per_blank
            _n = (_n % k) + (details_reminder * blank)
        }
    }
    if (m <= k) calc(n, k, m)
    return details
}