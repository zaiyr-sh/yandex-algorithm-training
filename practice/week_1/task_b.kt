import java.util.Scanner

fun main(){
    val reader = Scanner(System.`in`)
    val a:Int = reader.nextInt()
    val b:Int = reader.nextInt()
    val c:Int = reader.nextInt()
    if (a < b + c && b < a + c && c < a + b) {
        println("YES")
        return
    }
    println("NO")
}