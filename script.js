// get the start timer button
let start = document.querySelector("#startTimer");

// add an event listener to the start timer button
start.addEventListener('click', function timer() {
    var sec = 180; // set seconds to 180 (180s = 3m)
    
    var timer = setInterval(function() {
        // update the timer on the page
        document.getElementById('timer').innerHTML = sec;
       
        sec--; // decrease the seconds by 1
    
        // if the timer reaches 0 or below
        if (sec < 0) {
            // clear the interval
            clearInterval(timer);
            document.getElementById('timer').innerHTML = "0"; // ensure it shows 0
        }
    
    }, 1000);
});
