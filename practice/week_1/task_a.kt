fun main(){
    val (tRoom, tCond) = readLine()!!.split(' ').map(String::toInt)
    val conditioner = readLine()!!
    println(setupTemperature(conditioner, tRoom, tCond))
}

fun setupTemperature(conditioner: String, tRoom:Int, tCond: Int): Int {
    return when(conditioner) {
        "heat" -> {
            if (tRoom < tCond) tCond
            else tRoom
        }
        "freeze" -> {
            if (tRoom > tCond) tCond
            else tRoom
        }
        "auto" -> tCond
        else -> tRoom
    }
}