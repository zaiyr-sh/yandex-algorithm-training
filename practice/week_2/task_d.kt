// Дан список чисел. Определите, сколько в этом списке элементов, 
// которые больше двух своих соседей и выведите количество таких элементов.

fun main(){
    val input = readLine()!!
    val arr = input.replace(" ", "").map { Character.getNumericValue(it) }
    println(countElements(arr))
}

fun countElements(arr: List<Int>): Int {
    var i = 0
    var count = 0
    while (i != arr.size - 2) {
        if (arr[i] < arr[i + 1] && arr[i + 1] > arr[i + 2]) {
            count++
        }
        i++
    }
    return count
}