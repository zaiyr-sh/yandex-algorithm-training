// Дан список, заполненный произвольными целыми числами. 
// Найдите в этом списке два числа, произведение которых максимально. 
// Выведите эти числа в порядке неубывания.
// Список содержит не менее двух элементов. Числа подобраны так, что ответ однозначен.
// Решение должно иметь сложность O(n), где n - размер списка.

import java.util.Collections

fun main(){
    val input = readLine()!!
    val arr = input.split(" ").map { it.toInt() }
    println(findTwoNumbers(arr))
}

fun findTwoNumbers(arr: List<Int>): String {
    Collections.sort(arr)
    var len = arr.size - 1
    if(arr[0] * arr[1] > arr[len] * arr[len - 1]) {
        return "${arr[0]} ${arr[1]}"
    }
    return "${arr[len - 1]} ${arr[len]}"
}
