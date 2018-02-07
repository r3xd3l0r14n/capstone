$("#start-game").click(function () {
    sendMessage('init_game')
})
//What this function should do is bring in json that represents a pre-shuffled 52 card deck and push that to cards.js
//to create the initial deck
socket.on('init_gamed', function(json){
    cards.init({table: "#card-table"}, json)
})