fun main(){
    var check:String = readLine()!!
    var first:String = readLine()!!
    var second:String = readLine()!!
    var third:String = readLine()!!
    checkPhoneNumberInAddressBook(check, first, second, third)
}

fun checkPhoneNumberInAddressBook(check_pn: String, first_pn: String, second_pn: String, third_pn: String) {
    val regex = "[\\(\\)\\-\\+]".toRegex()
    val arrayOfPhoneNumbers = arrayOf(check_pn, first_pn, second_pn, third_pn) 
    for (item in arrayOfPhoneNumbers.indices) {
        arrayOfPhoneNumbers[item] = arrayOfPhoneNumbers[item].replace(regex, "")
        if (arrayOfPhoneNumbers[item].length == 7) {
            arrayOfPhoneNumbers[item] = "495${arrayOfPhoneNumbers[item]}"
        }
        arrayOfPhoneNumbers[item] = arrayOfPhoneNumbers[item].slice(arrayOfPhoneNumbers[item].len() - 9..arrayOfPhoneNumbers[item].len())
    }
    val checkerNumber = arrayOfPhoneNumbers[0]
    for (item in 1..arrayOfPhoneNumbers.size - 1){
        if(checkerNumber == arrayOfPhoneNumbers[item]) {
            println("YES")
        } else {
            println("NO")
        }
    }
}

fun String.len() = this.length - 1