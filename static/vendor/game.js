socket.on('init_gamed', function (json) {
    $("#lblPlayer1Hand").append(json.Hands[0])

    $("#btnPlayer1GoFish").click(function(){
        foo = $("#txtPlayer1GoFish").val();
        msg = JSON.parse(JSON.stringify({'card':foo})
        sendMessage('goFish', msg)
    });
});

