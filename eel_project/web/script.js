//on click of button
document.querySelector("button").onclick = function () {
    eel.random_python()(function(number){
        document.querySelector(".random_number").innerHTML = number;
    })
}