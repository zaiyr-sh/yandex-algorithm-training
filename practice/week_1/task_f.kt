fun main() {
    val (a1, b1, a2, b2) = readLine()!!.split(' ').map(String::toInt)
    println(setTableDimensions(a1, b1, a2, b2))
}

fun setTableDimensions(a1: Int, b1: Int, a2: Int, b2: Int): String {
    var ans1 = 0
    var ans2 = 0
    var area = 0
    if (a1 >= a2 && b1 >= b2) {
        ans1 = a1
        ans2 = b1
        area = a1 * b1
    }
    if (a1 >= a2 && b1 >= b2) {
        if ((a1 * b1) < area) {
            ans1 = a1
            ans2 = b2
            area = a1 * b2
        } 
    }
    if (a1 <= a2 && b1 >= b2) {
        if ((a2 * b1) < area) {
            ans1 = a2
            ans2 = b1
            area = a2 * b1
        } 
    }
    if (a1 <= a2 && b1 <= b2) {
        if ((a2 * b2) < area) {
            ans1 = a2
            ans2 = b2
            area = a2 * b2
        } 
    }
    if (a1 >= b2 && a2 >= b1) {
        if ((a1 * a2) < area) {
            ans1 = a1
            ans2 = a2
            area = a1 * a2
        } 
    }
    if (a1 >= b2 && a2 <= b1) {
        if ((a1 * b1) < area) {
            ans1 = a1
            ans2 = b1
            area = a1 * b1
        } 
    }
    if (a1 <= b2 && a2 >= b1) {
        if ((a2 * b2) < area) {
            ans1 = a2
            ans2 = b2
            area = a2 * b2
        } 
    }
    if (a1 <= b2 && a2 <= b1) {
        if ((b1 * b2) < area) {
            ans1 = b1
            ans2 = b2
        } 
    }
    return "${ans1} ${ans2}"
}