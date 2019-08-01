function factorial() {
    num = parseInt(document.getElementById("num").value)

    res = 1
    for (let i = 2; i <= num; i++) {
        res *= i

    }
    message = "Factorial of" + num + "is" + res
    document.getElementById("res").innerHTML = "<h2>" + message + "</h2>"
}
function digits() {

}
function palindrome() {

}
function reverseOfnum() {

}