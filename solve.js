

function main() {
    var n_temp = readLine().split(' ');
    var n = parseInt(n_temp[0]);
    var k = parseInt(n_temp[1]);
    a = readLine().split(' ');
    a = a.map(Number);

    var b = a.map(Number);

    var res = "";

    for (var i = 0; i < n; i++) {
        a[i] = b[(i + ((n + k) % n)) % n];
        res += a[i].toString();
        if (i < n - 1) {
            res += " ";
        }
    }
}


console.log(res)
