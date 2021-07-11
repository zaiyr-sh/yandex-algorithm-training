import java.util.Scanner

fun main() {
    val reader = Scanner(System.`in`)
    val a:Int = reader.nextInt()
    val b:Int = reader.nextInt()
    val c:Int = reader.nextInt()
    val d:Int = reader.nextInt()
    val e:Int = reader.nextInt()
    println(checkHoleSize(a, b, c, d, e))
}

fun checkHoleSize(a: Int, b: Int, c: Int, d: Int, e: Int): String {
    if ((a <= d && b <= e) || (b <= d && a <= e)) return "YES"
    else if ((b <= d && c <= e) || (c <= d && b <= e)) return "YES"
    else if ((c <= d && a <= e) || (a <= d && c <= e)) return "YES"
    return "NO"
}