import java.util.Scanner

fun main(){ 
    val reader = Scanner(System.`in`)
    val a:Int = reader.nextInt()
    val b:Int = reader.nextInt()
    val c:Int = reader.nextInt()
    println(solveEquation(a, b, c))
}

fun solveEquation(a: Int, b: Int, c: Int): Any {
    if (a == 0 && b == 0 && c == 0 || (a == 0 && b == c * c)) return "MANY SOLUTIONS"
    if (c < 0 || (a == 0 && b != c * c) || ((c * c - b) % a != 0)) return "NO SOLUTION"
    return (c * c - b) / a
}