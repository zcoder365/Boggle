function timer(){
    var sec = 180; // set seconds to 180 (180s = 3m)
    
    var timer = setInterval( function() {
        // update the timer on the page
        document.getElementById('timerDisplay').innerHTML=(sec%60)+':'+sec;
       
        sec--; // decrease the seconds by 1
    
        // if the timer goes below 0
        if (sec < 0) {
            // clear the interval
            clearInterval(timer);
        }
    
    }, 1000);

}