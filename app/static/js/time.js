/** Check for current time **/
function checkTime(i) {
    if (i < 10) {
        i = "0" + i;
    }
    return i;
}

/** Starts the live current time display **/
function startTime() {
    var today = new Date();
    var hour = today.getHours();
    var minute = today.getMinutes();
    var second = today.getSeconds();
    // pad minutes and seconds with additional 0 below 10
    minute = checkTime(minute);
    second = checkTime(second);
    document.getElementById('time').innerHTML = hour + ":" + minute + ":" + second;
    t = setTimeout(function () {
        startTime()
    }, 500);
}

/** Count up timer since page load (display as # minutes ago) **/
function pageLoadTimer(){
    var minutesLabel = document.getElementById("minutes");
    var totalSeconds = 0;
    setInterval(setTime, 1000);

    function setTime()
    {
        ++totalSeconds;

        minutes = (parseInt(totalSeconds/60));
        if (minutes === 0) {
            minutesLabel.innerHTML = 'just now';
        } else if (minutes === 1) {
            minutesLabel.innerHTML = '1 minute ago';
        } else {
            minutesLabel.innerHTML = minutes + ' minutes ago';
        }
    }
}

/** Sets display for next hour range (i.e. Current hour 1300, returns '1400 to 1500') **/
function getNextHour(){
    var currentTime = new Date(); //Current time
    var currentHr = currentTime.getHours();

    document.getElementById('nextHour').innerHTML = (currentHr + 1) + ':00 and ' + (currentHr + 2) + ':00';
}
