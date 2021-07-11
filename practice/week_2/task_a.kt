// Дан список. Определите, является ли он монотонно возрастающим(то есть верно ли, 
// что каждый элемент этого списка больше предыдущего).

// Выведите YES, если массив монотонно возрастает и NO в противном случае.

fun main(){
    val input = readLine()!!
    val arr = input.split(" ").map { it.toInt() }
    println(isMonotonicallyIncreasing(arr))
}

fun isMonotonicallyIncreasing(arr: List<Int>): String {
    var i = 0
    while (i != arr.size - 1) {
        if (arr[i] >= arr[i + 1]) {
            return "NO"
        }
        i++
    }
    return "YES"
}