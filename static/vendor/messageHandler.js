var socket = io.connect('http://' + document.domain + ":" + location.port)
var playerName;
var handShake;
var playerID;
var connPlayers;

$().ready(function () {
    $("#connect").click(function (){
        $("#result").text("Connecting...");
        playerName = $("#userN").val();
        handShake = JSON.parse(JSON.stringify({'userN':playerName}))
        sendMessage('handshake', handShake)
    });

    //Button or <a> Clicks to interface with the server

    // $("#joinGame").click(function () {
    //     msg = JSON.parse(JSON.stringify({'id': playerID, 'name': playerName}))
    //     sendMessage("join", msg);
    // })
    $("#joinGame").click(function () {
        msg = JSON.parse(JSON.stringify({'id':playerID, 'name':playerName}))
        sendMessage("join", msg)
    })
    $("#startGame").click(function () {
        console.log("I registered Joined!")
        sendMessage('init_game')
    })

    $("#disconnect").click(function () {
        msg = JSON.parse(JSON.stringify({'id': playerID}));
        sendMessage("d_conn", msg);
    })

    // Message handler is a bunch of socket.ons
    socket.on('handshook', function (json) {
        $("#result").text("Connected User: " + json.name);
		$("#connect").prop("disabled",true);
		$("#joinGame").prop("disabled",false);
		$("#startGame").prop("disabled",false);
        playerID = json.id
    });
    socket.on('disconnected', function (json) {
        $("#result").text("Disconnected " + json + " from server")
    });
    socket.on('joined', function (json) {
        var id = json['id'];
        sendMessage('get_players', id)

        if (id === playerID) {
            $("#joinGame").css("visibility", "hidden")
        }
    });
    // socket.on('got_players', function(json){
    //     $("#lblPlayer1").append(json[1])
    // });
    socket.on('got_players', function (json) {
        $("#lblPlayer1").empty()
        $("#lblPlayer2").empty()
        $("#lblPlayer3").empty()
        $("#lblPlayer4").empty()
        var a = 0;
        for (i in json) {
            switch (a) {
                case 0:
                    $("#lblPlayer1").append(json[1]);
                    break;
                case 1:
                    $("#lblPlayer2").append(json[2]);
                    break;
                case 2:
                    $("#lblPlayer3").append(json[3]);
                    break;
                case 3:
                    $("#lblPlayer4").append(json[4]);
                    break;
                default:
                    $("#result").text("There are too many players connected")
            }
            a++;
        }
    });
    socket.on('max_players', function (msg) {
        $("#result").text(msg)
    });
});

function sendMessage(method, msgArray) {
    socket.emit(method, msgArray);
}

//function addPlayer(name) {
//    $("#active-players").append('<div class="name">' + name + '</div>');
//}