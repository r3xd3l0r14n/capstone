socket.on('init_gamed', function (json) {
    a = 1;
    for (c in json['Deck']) {
        $("#lblDeck").append(" " + json['Deck'][c]);
    }
    while (a <= 4) {
        for (i in json['Hands'][a]) {
            console.log(a);
            switch (a) {
                case 1:
                    $("#lblPlayer1Hand").append(" " + json['Hands'][a][i]);
                    break;
                case 2:
                    $("#lblPlayer2Hand").append(" " + json['Hands'][a][i]);
                    break;
                case 3:
                    $("#lblPlayer3Hand").append(" " + json['Hands'][a][i]);
                    break;
                case 4:
                    $("#lblPlayer4Hand").append(" " + json['Hands'][a][i]);
                    break;
            }
        }
        a++
    }
});
socket.on('goFished', function (json) {
    $("#lblPlayer1Hand").empty();
    $("#lblPlayer2Hand").empty();
    $("#lblPlayer3Hand").empty();
    $("#lblPlayer4Hand").empty();
    $("#lblDeck").empty();
    a = 1;
    for (c in json['Deck']) {
        $("#lblDeck").append(" " + json['Deck'][c]);
    }
    console.log(json['Scores']);
    while (a <= 4) {
        for (i in json['Hands'][a]) {

            switch (a) {
                case 1:
                    $("#lblPlayer1Hand").append(" " + json['Hands'][a][i]);
                    $("#lblPlayer1Score").empty().append(" " + json['Scores'][a]);
                    break;
                case 2:
                    $("#lblPlayer2Hand").append(" " + json['Hands'][a][i]);
                    $("#lblPlayer2Score").empty().append(" " + json['Scores'][a]);
                    break;
                case 3:
                    $("#lblPlayer3Hand").append(" " + json['Hands'][a][i]);
                    $("#lblPlayer3Score").empty().append(" " + json['Scores'][a]);
                    break;
                case 4:
                    $("#lblPlayer4Hand").append(" " + json['Hands'][a][i]);
                    $("#lblPlayer4Score").empty().append(" " + json['Scores'][a]);
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
    msg = JSON.parse(JSON.stringify({'card': foo, 'id': playerID}));
    sendMessage('goFish', msg)
});
$("#btnPlayer3GoFish").click(function () {
    foo = $("#txtPlayer3GoFish").val();
    msg = JSON.parse(JSON.stringify({'card': foo, 'id': playerID}));
    sendMessage('goFish', msg)
});
$("#btnPlayer4GoFish").click(function () {
    foo = $("#txtPlayer4GoFish").val();
    msg = JSON.parse(JSON.stringify({'card': foo, 'id': playerID}));
    sendMessage('goFish', msg)
});


