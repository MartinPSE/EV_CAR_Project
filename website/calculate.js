// Calculate Distance with conditions
function PriceCalc(){
    var dis = parseFloat(document.getElementById('getdistance').textContent) // just use
    
    var cc = parseInt(document.getElementsByClassName('ch1-header__title ch1-value')[0].innerHTML) // 1000/ 1600/ 2000/ 2100 more
        cclist = [1000, 1600, 2000, 2100]
    var carkinds = document.getElementsByClassName('dropp-header__title js-value')[0].innerHTML; // 가솔린 / 디젤
        fuellist = ['가솔린','디젤']
    var perpeople = parseInt(document.getElementsByClassName('dropp-header__title people-value')[0].innerHTML) // 1~4명
    var perweek = parseInt(document.getElementsByClassName('dropp-header__title week-value')[0].innerHTML) // 1~7번
    
    distance = dis*perweek*4 // 거리 * 주당 횟수 * 4주(1달 기준)
    
    // 1000CC 일때
    if (cc == cclist[0]) {
        if(carkinds == fuellist[0]){
            price = distance / 16 * 1610
        }
        else if (carkinds == fuellist[1]) {
            price = '유종을 가솔린으로 선택하세요'
            alert(price)
        }
    }
    // 1600CC 일때
    else if (cc == cclist[1]) {
        if(carkinds == fuellist[0]){
            price = distance / 13.7 * 1610
        }
        else {
            price = distance / 18.4 * 1410
        }
    }
    // 2000CC 일때
    else if (cc == cclist[2]) {
        if(carkinds == fuellist[0]){
            price = distance / 12.3 * 1610
        }
        else {
            price = distance / 16.1 * 1410
        }
    }
    // 2100CC 이상
    else if (cc == cclist[3]) {
        if(carkinds == fuellist[0]){
            price = distance / 11.2 * 1610
        }
        else {
            price = distance / 14.8 * 1410
        }
    }

    var carpoolprice = Math.floor(price.toFixed(1)/10/perpeople)*10

    document.getElementById('price').innerHTML = carpoolprice.toLocaleString()+'원';
}

function Compare() {
    var dis = parseFloat(document.getElementById('getdistance').textContent);
    var perweek = parseInt(document.getElementsByClassName('dropp-header__title week-value')[0].innerHTML);

    if (dis<=10){
        compare = 1250
    }
    else{
        compare = 1350 + parseInt((dis-10)/5)*100
    }

    var lastprice = compare * 4 * perweek

    document.getElementById('trans').innerHTML = lastprice.toLocaleString()+'원';
}