function showAllWinner() {
    let s = "";
    for (let prize in winNo1) {
        s += "<div class='col-6 col-sm-4 col-md-3'>";
        s += '<div class="logo div">';
        let logo = logo_mapping[prize];
        s += `<img src="img/${logo}" alt="" class="img-fluid">`;
        s += "</div>";

        s += `<div class="winner-list container" id="${prize}">`;
        let prize_name = name_mapping[prize];
        let winner = winNo1[prize];
        s += `<p>${prize_name}</p>`;
        let winner_div = winner.map(x => `<div class="winner"> ${x} </div>`);
        s += winner_div.join("");
        s += "</div></div>";
    }
    console.log(s);
    document.getElementById("winner_list").innerHTML = s;
}