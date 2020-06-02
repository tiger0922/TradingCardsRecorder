const rows = [
    [' ', 'Nayeon', ' ', 'Jeongyeon', ' ', 'Momo', ' ', 'Sana', ' ', 'Jihyo', ' ', 'Mina', ' ', 'Dahyun', ' ', 'Chaeyoung', ' ', 'Tzuyu']
];

window.onload = function() {
    let csvlist = new Array(11);
    for (let i = 0; i < csvlist.length; i++) {
        csvlist[i] = new Array(18);
    }

    let btn = document.getElementById("submit_btn").onclick = function() {
        let csvContent = "data:text/csv;charset-utf8,";
        let list = document.getElementsByClassName("piece");
        for (let i = 0; i < csvlist.length; i++) {
            for (let j = 0; j < csvlist[0].length; j++) {
                if (j%2) {
                    csvlist[i][j] = list[i*9+Math.floor(j/2)].value;
                } else {
                    num = i*9+Math.floor(j/2)+1;
                    num = num.toString();
                    while(num.length < 3) {
                        num = '0' + num;
                    }
                    csvlist[i][j] = num;
                }
            }
        }
        rows.forEach(function(rowArray) {
            let row = rowArray.join(",");
            csvContent += row + "\r\n";
        });
        csvlist.forEach(function(rowArray) {
            let row = rowArray.join(",");
            csvContent += row + "\r\n";
        });
        let encodedUri = encodeURI(csvContent);
        window.open(encodedUri);
    }
}
