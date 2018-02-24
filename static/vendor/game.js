socket.on('init_gamed', function (json) {
    $("#lblPlayer1Hand").empty()
    $("#lblPlayer2Hand").empty()
    $("#lblPlayer3Hand").empty()
    $("#lblPlayer4Hand").empty()
    a = 1
    while (a <= 4) {
        for (i in json['Hands'][a]) {
            console.log(a)
            switch (a) {
                case 1:
                    $("#lblPlayer1Hand").append(" " + json['Hands'][a][i]);
                    break;
                case 2:
                    $("#lblPlayer2Hand").append(" " + json['Hands'][a][i]);
                    break;
            }
        }
        a++
    }
});
socket.on('goFished', function (json) {
    a = 1
    while (a <= 4) {
        for (i in json['Hands'][a]) {
            console.log(a)
            switch (a) {
                case 1:
                    $("#lblPlayer1Hand").append(" " + json['Hands'][a][i])
                    break;
                case 2:
                    $("#lblPlayer2Hand").append(" " + json['Hands'][a][i])
                    break;
            }
        }
        a++
    }
});
$("#btnPlayer1GoFish").click(function () {
    foo = $("#txtPlayer1GoFish").val();
    msg = JSON.parse(JSON.stringify({'card': foo, 'id': playerID}));
    sendMessage('goFish', msg)
});
$("#btnPlayer2GoFish").click(function () {
    foo = $("#txtPlayer2GoFish").val();
    msg = JSON.parse(JSON.stringify({'card': foo}));
    sendMessage('goFish', msg)
});
$("#btnPlayer3GoFish").click(function () {
    foo = $("#txtPlayer3GoFish").val();
    msg = JSON.parse(JSON.stringify({'card': foo}));
    sendMessage('goFish', msg)
});
$("#btnPlayer4GoFish").click(function () {
    foo = $("#txtPlayer4GoFish").val();
    msg = JSON.parse(JSON.stringify({'card': foo}));
    sendMessage('goFish', msg)
});

socket.on('goFished', function (json) {
    console.log(json)
});


