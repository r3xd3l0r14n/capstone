
var socket = io.connect('http://'+document.domain+ ":"+location.port)
var playerName;
var playerID;

$().ready(function () {
    $("a#connect").click(function (event) {
        playerName = $("#username").val()
        $("#result").text("Connecting...");

        socket.emit('my event', {data: 'I\'m a message'})
        socket.on('my response', function (msg) {
            //msg = JSON.stringify(['new_player', playerName])
            $('#result').text(msg.data)
        })

        // socket.onopen = openHandler;
        // socket.onmessage = messageHandler;
        // socket.onerror = function (e) {
        //     $("#result").text(e.message);
        // };
    });

    $("#btnJoin").click(function () {
        sendMessage(["join"]);
    })

});

function sendMessage(msgArray) {
    var msg = JSON.stringify(msgArray);
    socket.send(msg);
}

function openHandler(e) {
    $("#result").text("connected to server");
    playerName = $('#userName').val();

    sendMessage(["new_player", playerName]);

    $("#card-table").show();

    $(document).bind("keydown", keyhandler);
}

function messageHandler(e) {
    json = JSON.parse(e.data);
    if (!(json[0] instanceof Array))
        json = [json];

    for (var i = 0; i < json.length; i++) {
        var args = json[i];
        var cmd = json[i][0]
        switch (cmd) {
            case("handshake"):
                $("#connect").addClass("active")
                $("#result").text("Connected User: " + args[1]);
                $("#card-table").show()
                playerID = args[2];
                break
            case("p_joined"):
                var id = args[1];
                var name = args[2];
                addPlayer(id, name);

                if (id == playerID) {
                    $("a#join").css("visibility", "hidden")
                }
                break;
            case("disconnect"):
                $("#connect").classList.remove("active")
                $("#result").text("Disconnected")
                $("#card-table").hide()
                break;
        }
    }
}

function addPlayer(id, name) {
    $("#active-players").append('<div id="player' + id + '">'
        + '<div class="name">' + name + '</div>');
}