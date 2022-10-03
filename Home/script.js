

//the text below lets javascript know how much time the timer is supposed to start with
const startingMinutes = 0;
let time = startingMinutes * 60;

const CountUpEl = document.getElementById('CountUp');

// setInterval repeatedly calls a function or executes a code snippet, with a fixed time delay between each call
setInterval(updateCountUp, 1000);

//the function below tells javascript how it's supposed to update the numbers
// The Math.floor() function always rounds down and returns the largest integer less than or equal to a given number.
function updateCountUp() {
    const minutes = Math.floor(time / 60);
    let seconds = time % 60;
    //makes sure that when the timer starts it starts at 0: 00 instead of 0: 0
    seconds = seconds < 10 ? '0' + seconds : seconds;
    
    

    CountUpEl.innerHTML = `${minutes}: ${seconds}`;
    time++;
}
