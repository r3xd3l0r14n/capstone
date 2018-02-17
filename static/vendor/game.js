//What this function should do is bring in json that represents a pre-shuffled 52 card deck and push that to cards.js
//to create the initial deck
// cards.init({table: "#card-table"})
//
// deck = new cards.Deck();
// deck.x -= 50;
//
// deck.addCards(cards.all)
// deck.render({immediate: true})

discardPile = new cards.Deck({faceUp: true});
discardPile.x += 50;

socket.on('init_gamed', function (json) {
    cards.init({table: "#card-table", deck: json.Deck})

    deck = new cards.Deck();
    deck.x -= 50;

    deck.addCards(cards.all)
    deck.render({immediate: true})


    p1hand = new cards.Hand({faceUp: false, y: 340})
    p4hand = new cards.Hand({faceUp: false, y: 60})
    p3hand = new cards.Hand({faceUp: false, x: 60})
    p2hand = new cards.Hand({faceUp: false, x: 540})

    deck.dealNew(5, [p1hand, p2hand, p3hand, p4hand], 50, function () {
        console.log("WE are empty or filled?")
    }, json.Hands);

    switch (playerID) {
        case 1:
            p1hand.faceUp = true
            break;
        case 2:
            p2hand.faceUp = true
            break;
        case 3:
            p3hand.faceUp = true
            break;
        case 4:
            p4hand.faceUp = true
            break;
    }
})