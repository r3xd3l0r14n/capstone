var socket = io.connect('http://' + document.domain + ":" + location.port)
var playerName;
var handShake;
var playerID;
var connPlayers;

$().ready(function () {
    $('#card-table').hide()
    $("#player-names").hide()
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
        msg = JSON.parse(JSON.stringify({'id': playerID}));
        sendMessage("d_conn", msg);
    })

    // Message handler is a bunch of socket.ons
    socket.on('handshook', function (json) {
        $("#connect").addClass("active")
        $("#result").text("Connected User: " + json.name);
        $("#card-table").show()
        $("#player-names").show()
        playerID = json.id
    });
    socket.on('disconnected', function (json) {
        $("#card-table").hide();
        $("#result").text("Disconnected " + json + " from server")
    });
    socket.on('joined', function (json) {
        var id = json['id'];
        sendMessage('get_players', id)

        if (id == playerID) {
            $("a#join").css("visibility", "hidden")
        }
    })
    socket.on('got_players', function (json) {
        var a = 1;
        for (i in json){
            switch (a){
                case 1:
                    $("#lblPlayer1").append(json[1])
                    break;
                case 2:
                    $("#lblPlayer2").append(json[2])
                    break;
                case 3:
                    $("#lblPlayer3").append(json[3])
                    break;
                case 4:
                    $("#lblPlayer4").append(json[4])
                    break;
                default:
                    $("#result").text("There are too many players connected")
            }
            a++;
        }
    });
    socket.on('max_players', function (msg) {
        $("#result").text(msg)
    })


});

function sendMessage(method, msgArray) {
    socket.emit(method, msgArray);
}

//function addPlayer(name) {
//    $("#active-players").append('<div class="name">' + name + '</div>');
//}