// get the start timer button
let start = document.querySelector("#startTimer");

// add an event listener to the start timer button
start.addEventListener('click', timer());

// have the function for the timer
function timer(){
    var sec = 180; // set seconds to 180 (180s = 3m)
    
    var timer = setInterval( function() {
        // update the timer on the page
        document.getElementById('timerDisplay').innerHTML=sec;
       
        sec--; // decrease the seconds by 1
    
        // if the timer goes below 0
        if (sec < 0) {
            // clear the interval
            clearInterval(timer);
        }
    
    }, 1000);

}