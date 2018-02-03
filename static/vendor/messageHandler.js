var socket = io.connect('http://' + document.domain + ":" + location.port)
var playerName;
var handShake;
var playerID;
var connPlayers;

$().ready(function () {
    $('#card-table').hide()
    $("a#connect").click(function () {
        $("#result").text("Connecting...");
        playerName = $('#userN').val();
        handShake = JSON.parse('{"userN":"' + playerName + '","starStatus":false}')
        sendMessage('handshake', handShake)
    });

    //Button or <a> Clicks to interface with the server

    $("a#join").click(function () {
        msg = JSON.parse(JSON.stringify({'id': playerID, 'name': playerName}))
        sendMessage("join", msg);
    })

    $("a#disconnect").click(function () {
        msg = JSON.parse(JSON.stringify({'id': playerID}))
        sendMessage("d_conn", msg);
    })

    // Message handler is a bunch of socket.ons
    socket.on('handshook', function (json) {
        $("#connect").addClass("active")
        $("#result").text("Connected User: " + json.name);
        $("#card-table").show()
        playerID = json.id
    })
    socket.on('disconnected', function (json) {
        $("#card-table").hide()
        $("#result").text("Disconnected " + json + " from server")
    })
    socket.on('joined', function (json) {
        var id = json['id'];
        sendMessage('get_players', id)

        if (id == playerID) {
            $("a#join").css("visibility", "hidden")
        }
    })
    socket.on('got_players', function (json) {
        $("#active-players").empty()
        $("#active-players").text("Active Players:")
        for (i in json) {
            addPlayer(json[i])
        }
    })
    socket.on('max_players', function (msg) {
        $("#result").text(msg)
    })


});

function sendMessage(method, msgArray) {
    //var msg = JSON.stringify(msgArray);
    socket.emit(method, msgArray);
}

function openHandler(e) {
    $("#result").text("connected to server");
    playerName = $('#userName').val();


    $("#card-table").show();

    $(document).bind("keydown", keyhandler);
}                                                                                                                                                                                                                                                                                                                                    