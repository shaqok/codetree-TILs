const fs = require("fs");
const input = fs.readFileSync(0).toString().trim().split('\n');

const n = Number(input[0]);
const forecasts = input.slice(1, n + 1).map(line => line.split(' '));

// Please Write your code here.
class Forecast {
    constructor(date, day, status) {
        this.date = date;
        this.day = day;
        this.status = status;
        this.newDate = this.date.split('-').join('')
    }

    print_info() {
        console.log(this.date, this.day, this.status);
    }
}

let system = [];

for (let [date, day, status] of forecasts) {
    const forecast = new Forecast(date, day, status);
    system.push(forecast);
}

system.sort((prev, cur) => prev.newDate - cur.newDate);
system = system.filter((forecast) => forecast.status == 'Rain');
system[0].print_info();

