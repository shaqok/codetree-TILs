const fs = require("fs");
const input = fs.readFileSync(0).toString().trim().split('\n');
const [s_code, m_point, time] = input[0].split(' ');
// Please Write your code here.

class SecretCode {
    constructor(code, place, time) {
        this.code = code;
        this.place = place;
        this.time = time;
    }

    print_info() {
        console.log("secret code : " + this.code);
        console.log("meeting point : " + this.place);
        console.log("time : " + this.time);
    }
}

let secretCode = new SecretCode(s_code, m_point, time);
secretCode.print_info();