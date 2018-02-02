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

    $("a#join").click(function () {
        msg = JSON.parse(JSON.stringify({'id':playerID,'name':playerName}))
        sendMessage("join", msg);
    })

    // Message handler is a bunch of socket.ons
    socket.on('handshook', function (json) {
        $("#connect").addClass("active")
        $("#result").text("Connected User: " + json.name);
        $("#card-table").show()
        playerID = json.id
    })
    socket.on('joined', function (json) {
        var id = json['id'];
        var name = json['name'];
        sendMessage('get_players', id)

        if (id == playerID) {
            $("a#join").css("visibility", "hidden")
        }
    })
    socket.on('got_players', function (json) {
        for(i = 0; i < json.length; i++){
            addPlayer(json[i])
        }
    })
    socket.on('max_players', function(msg){
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

            case("p_joined"):

                break;
            case("disconnect"):
                $("#connect").classList.remove("active")
                $("#result").text("Disconnected")
                $("#card-table").hide()
                break;
        }
    }
}

function addPlayer(name) {
    $("#active-players").append('<div class="name">' + name + '</div>');
}